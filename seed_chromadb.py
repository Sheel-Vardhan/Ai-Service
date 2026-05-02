import chromadb

# Create ChromaDB client
client = chromadb.PersistentClient(path="./chroma_db")

# Create or get collection
collection = client.get_or_create_collection(
    name="audit_knowledge"
)

# 10 audit domain knowledge documents
documents = [
    "Tax compliance requires timely filing of returns and supporting documents.",

    "Weak internal controls increase the risk of fraud and financial misstatements.",

    "Missing audit evidence can lead to qualified audit opinions.",

    "Delayed compliance reporting may result in regulatory penalties.",

    "Segregation of duties helps prevent unauthorized transactions.",

    "Risk assessments should be updated regularly during audits.",

    "Data retention policies help maintain regulatory compliance.",

    "External audits improve transparency and accountability.",

    "Proper documentation improves audit traceability.",

    "Cybersecurity controls protect sensitive financial data."
]

# Unique IDs
ids = [f"doc_{i}" for i in range(10)]

# Add documents to ChromaDB
collection.add(
    documents=documents,
    ids=ids
)

print("✅ 10 documents inserted into ChromaDB successfully!")