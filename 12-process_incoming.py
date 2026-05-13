import pandas as pd
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
import joblib
import requests


def create_embedding(text_list):
    r = requests.post("http://localhost:11434/api/embed", json={
        "model": "bge-m3", 
        "input": text_list
    })

    embedding = r.json()["embeddings"]
    return embedding



df = joblib.load('embeddings.joblib')


incoming_query = input("Ask a Question: ")
question_embedding = create_embedding([incoming_query])[0]



# Find similarities of question_embeddin with other embeddings
similarities = cosine_similarity(np.vstack(df['embedding']), [question_embedding]).flatten()



top_results = 30
max_indx = similarities.argsort()[::-1][0:top_results]

new_df = df.loc[max_indx]


for index, item in new_df.iterrows():
    print(index, item["title"], item["number"], item["text"], item["start"], item["end"])




