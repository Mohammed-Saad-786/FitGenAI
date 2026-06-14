from sklearn.feature_extraction.text import TfidfVectorizer
import pickle
import os

documents = []

for file in ["data/workouts.txt", "data/meals.txt"]:
    with open(file, "r", encoding="utf-8") as f:
        documents.append(f.read())

vectorizer = TfidfVectorizer()

vectors = vectorizer.fit_transform(documents)

os.makedirs("rag_store", exist_ok=True)

with open("rag_store/vectorizer.pkl", "wb") as f:
    pickle.dump(vectorizer, f)

with open("rag_store/documents.pkl", "wb") as f:
    pickle.dump(documents, f)

print("✅ RAG Store Created")