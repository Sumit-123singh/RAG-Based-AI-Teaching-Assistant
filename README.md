# RAG-Based-AI-Teaching-Assistant
"An AI-powered teaching assistant that uses Retrieval-Augmented Generation (RAG) to process video lectures, convert them into transcripts, generate embeddings, and provide accurate answers to user queries."

🚀 Features

Convert video lectures to searchable text
Generate embeddings for semantic search
Interactive Q&A with your educational content
Easy-to-use pipeline for processing your data
Customizable prompt engineering

⚙️ Installation & Setup

### 1️⃣ Clone the repo

git clone https://github.com/yourusername/rag-teaching-assistant.git
cd rag-teaching-assistant


2️⃣ Install dependencies

We recommend using virtualenv or conda.
pip install -r requirements.txt
Main packages:

numpy
pandas
scikit-learn
joblib
requests

3️⃣ Install & run Ollama

Download and install Ollama.
Pull the required models:

ollama pull bge-m3     # For embeddings
ollama pull llama3.2   # For answering queries

🛠️ Steps to Use (Complete Workflow)

Step 1 - Collect your videos
Move all your video files into the videos/ folder.

Step 2 - Convert to MP3

Convert all the video files to MP3:
python process_video.py
All MP3 files will be saved inside audios/.

Step 3 - Convert MP3 to JSON

Convert all the MP3 files into transcript JSON:
python sts.py
This will generate JSON transcript chunks in the jsons/ folder.

Step 4 - Convert JSON files to Vectors

Generate embeddings and save them into a joblib file:
python preprocess_json.py
This will create embedding.joblib.

Step 5 - Prompt generation & Query the Assistant

Load embeddings, create a prompt, and feed it into the LLM:
python read_chunks.py
Now you can ask any question about your videos, and the AI will retrieve the correct timestamps and give a human-like answer.

🧑‍🏫 Example Usage

Ask a Question: What are curated data science packages?
Output:
🔎 Retrieved Context:
Video: 1_1. Installing Anaconda
Time: 79s – 81s
Text: "You get to see around 300 curated data science packages."

💡 Final Answer:
Around 300 curated data science packages are included. You can review this at timestamp 79s – 81s in "Installing Anaconda".


📂 Project File Structure

'''text
RAG-Based Project/
│
├── venv/                   # 🐍 Virtual environment for dependencies
│
├── audios/                 # 🎵 Extracted audio files (MP3 format)
├── videos/                 # 🎥 Original video lectures (input source)
├── jsons/                  # 📑 JSON chunks after speech-to-text (transcripts)
│
├── output.json             # Consolidated JSON output (optional)
├── embedding.joblib        # Vector embeddings stored for retrieval
│
├── process_video.py        # 🎥 Converts videos → MP3 (audio extraction)
├── process_incoming.py     # 📨 Handles incoming user queries
├── read_chunks.py          # 🔎 Main RAG pipeline (retrieval + LLM response)
├── sts.py                  # 🗣️ Speech-to-text pipeline (MP3 → JSON)
│
├── prompt.txt              # 📝 Last generated prompt (for debugging/inspection)
├── response.txt            # 💡 Last model response (LLM answer)
├── requirements.txt        # 📦 Python dependencies for the project
├── README.md               # 📘 Project documentation
'''


📌 Notes

Ensure Ollama server is running before use:
ollama serve
Modify read_chunks.py to adjust the number of top retrieved results (top_results).
This project works completely offline once the required models are downloaded.

⚡ Testing note: Initially, I tried processing 20 videos, but my laptop struggled due to heating (GPU temperature reached ~70°C) and it took ~3 hours to load all chunks.
For smoother testing, I used only 3 videos, and the pipeline worked perfectly.
Depending on your hardware specifications, you can scale up the number of videos accordingly.

## 🚀 Future Enhancements

1. 🔎 **Advanced Retrieval** – Use FAISS/ChromaDB for faster and more accurate semantic search.  
2. 📝 **Summarization & Notes** – Auto-generate concise video summaries, key points, and quizzes for quick revision. 3. 🖥️ **User-Friendly GUI** – Provide a smooth interface (Streamlit/Gradio) where users can upload videos, view transcripts, and interact in a chat-style Q&A.  
4. 🤖 **GPT-5 Integration** – Add support for GPT-5 (and other top LLMs) for more accurate and context-aware answers.  


👨‍💻 Author

Sumit Singh  
AI/ML Enthusiast | Backend developer




