import chromadb

client = chromadb.PersistentClient(path="./chroma_db")

collection = client.get_collection("audit_knowledge")

data = collection.get()

print(data)