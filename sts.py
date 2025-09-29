import whisper
import json

# Load model
model = whisper.load_model("large-v2")

# Transcribe and translate
result = model.transcribe(
    r"C:\Users\hp\OneDrive\Desktop\RAG -Based Project\audios\1_1. Installing Anaconda  @unlocked_coding.mp4.mp3",
    language='hi',
    task='translate',
    word_timestamps=False
)

# Collect all segments
chunks = []
for segment in result['segments']:
    chunks.append({
        'start': segment['start'],
        'end': segment['end'],
        'text': segment['text']
    })

# Print chunks for debugging
print(chunks)

# Save all chunks into JSON (only once)
with open('output.json', 'w', encoding='utf-8') as f:
    json.dump(chunks, f, ensure_ascii=False, indent=4)

print("Transcription saved to output.json")
