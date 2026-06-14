import pickle
from sklearn.metrics.pairwise import cosine_similarity

with open("rag_store/vectorizer.pkl", "rb") as f:
    vectorizer = pickle.load(f)

with open("rag_store/documents.pkl", "rb") as f:
    documents = pickle.load(f)

def retrieve_context(query):

    query_vector = vectorizer.transform([query])

    doc_vectors = vectorizer.transform(documents)

    similarities = cosine_similarity(
        query_vector,
        doc_vectors
    )

    best_index = similarities.argmax()

    return documents[best_index]