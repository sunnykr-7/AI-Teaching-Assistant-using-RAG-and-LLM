# RAG-based-AI-Teaching-Assistant

### NOTE - Dataset consists of educational AI/ML/Python tutorial videos converted into audio for transcription and retrieval.

## The Live Project is on my laptop, I will soon upload Google Drive Video Related to the project video demo soon..


# 1 - Architecture Flow

Videos → Audio → Whisper Transcription →
Chunking → Embeddings →
Cosine Similarity Retrieval →
Prompt Engineering →
LLM Response

# 2 - Tech Stack
- Python
- Whisper
- Ollama
- Llama 3.2
- BGE-M3
- Pandas
- Scikit-learn
- Joblib

# 3 - Features
- Timestamp-aware retrieval
- Semantic search
- Course-specific Q&A
- Local LLM inference
- Quick Response From LLM



# HOW TO USE THIS RAG AI TEACHING ASSISTANT ON OUR OWN DATA


## Step 1 - Collect your videos
Move all your video files to the videos folder

## Step 2 - Convert to mp3
Convert all the video files to mp3

## Step 3 - Convert mp3 to json 
Convert all the mp3 files to json

## Step 4 - Convert the json files to Vectors
We convert the json files to a dataframe with Embeddings and save it as a joblib pickle

## Step 5 - Prompt generation and feeding to LLM.

Read the joblib file and load it into the memory. Then create a relevant prompt as per the user query and feed it to the LLM.

---------------------------------------- T H E - E N D --------------------------------------------
