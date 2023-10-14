import chromadb

def create_vector_db():
    chroma_client = chromadb.Client()
    collection = chroma_client.create_collection(name="my_collection")

    collection.add(
        documents = ["My name is David", "My name is not David"],
        metadatas = [{"source": "name is true"}, {"source": "name is false"}],
        ids = ["id1", "id2"]
    )

    return collection

def query_db():
    pass

if __name__ == "__main__":
    collection = create_vector_db()

    results = collection.query(
        query_texts=["What is my name?"],
        n_results=2
    )

    print(results)