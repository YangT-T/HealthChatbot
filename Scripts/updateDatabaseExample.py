from langchain.vectorstores import FAISS
from langchain.embeddings.huggingface import HuggingFaceEmbeddings
from dotenv import find_dotenv, load_dotenv
load_dotenv(find_dotenv())

def load_texts(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        texts = [line.strip() for line in f.readlines() if line.strip() and len(line)<1000]
    return texts

def create_faiss_index(texts):
    huggingface_ef=HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2") 

    vector_db=FAISS.from_texts(texts=texts,embedding=huggingface_ef)
    
    return vector_db

file_path =  "./Data/ExampleData/DialMed.txt"  
texts = load_texts(file_path)

vector_db = create_faiss_index(texts)

vector_db.save_local("./KnowledgeBase/DailMed")





