import requests
import os
import json
import numpy as np
import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
import joblib


# Step 1: Create Embedding

def create_embedding(text_list):
    r = requests.post("http://localhost:11434/api/embed", json={
        "model": "bge-m3",
        "input": text_list
    })
    embedding = r.json()["embeddings"]
    return embedding



# Step 2: Load JSON files and store chunks

jsons = os.listdir("jsons")
my_dicts = []
chunk_id = 0

for json_file in jsons:
    with open(f"jsons/{json_file}") as f:
        content = json.load(f)

    if isinstance(content, dict) and "chunks" in content:
        chunks = content["chunks"]
    elif isinstance(content, list):
        chunks = content
    else:
        print(f"Skipping {json_file}, unexpected format")
        continue

    print(f"Creating Embeddings for {json_file}")
    embeddings = create_embedding([c['text'] for c in chunks])

    for i, chunk in enumerate(chunks):
        chunk['chunk_id'] = chunk_id
        chunk['embedding'] = embeddings[i]
        chunk_id += 1
        my_dicts.append(chunk)

df = pd.DataFrame.from_records(my_dicts)


# Step 3: Ask Question

incoming_query = input("Ask a Question: ")
question_embedding = create_embedding([incoming_query])[0]

similarities = cosine_similarity(np.vstack(df['embedding']), [question_embedding]).flatten()

top_results = 3
max_indx = similarities.argsort()[::-1][0:top_results]
new_df = df.loc[max_indx]
print("\n🔎 Retrieved Context:")
print(new_df[["title", "number", "text"]])


#
# Step 4: Generate Final Answer using LLM
# 
context = "\n".join(new_df["text"].values)

payload = {
    "model": "llama3.1",
    "prompt": f"Answer the question based on the context below:\n\nContext:\n{context}\n\nQuestion: {incoming_query}\n\nAnswer:"
}

r = requests.post("http://localhost:11434/api/generate", json=payload, stream=True)

print("\n💡 Final Answer:\n")

for line in r.iter_lines():
    if line:
        data = json.loads(line.decode("utf-8"))
        if "response" in data:
            print(data["response"], end="", flush=True)

# 
# Define inference function (moved OUTSIDE loop)
# 
def inference(prompt):
    r = requests.post('http://localhost:11434/api/generate', json={
        #'model': ' deepseek-r1',
        'model':'llama3.2',
        'prompt': prompt,
        'stream': False
    })
    response = r.json()
    print(response)
    return response


# Save embeddings
joblib.dump(df, "embedding.joblib")
print(" Embeddings saved to embedding.joblib")

new_df = df.iloc[max_indx]

prompt = f'''I am teaching a data science course. Here are video chunks containing video title, video number, start time in seconds, end time in seconds, and the text:

{new_df[['title','number','start','end','text']].to_json(orient='records')}
-------------------------

{incoming_query}
User asked this question related to the video chunks. You must answer in a human way|(dont menstion the above format.its just for you) where and how much content is taught (which video and what timestamp) and guide the user to go to that particular video. If the user asks an unrelated question, tell him you can only answer questions related to the courses.'''

with open('prompt.txt', 'w') as f:
    f.write(prompt)

response = inference(prompt)['response']
print( response)

with open('response.txt', 'w') as f:
    f.write(str(response))

for index, item in new_df.iterrows():
    print(index, item['chunk_id'], item['number'], item['text'], item['start'], item['end'])



# def get_answer(query: str) -> str:
#     # Step 1: Load embeddings / vector DB
#     # Step 2: Retrieve top matching chunks
#     # Step 3: Send query + chunks to LLM
#     # Step 4: Return final answer
    
#     # Example (dummy return for now):
#     return "This is the AI answer for: " + query
 
# from read_chunks import get_answer

# print(get_answer("What is RAG?"))