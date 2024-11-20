from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.embeddings import HuggingFaceEmbeddings


embeddings = HuggingFaceEmbeddings(model="sentence-transformers/all-mpnet-base-v2")
query_result = embeddings.aembed_query("hello")
print(query_result)