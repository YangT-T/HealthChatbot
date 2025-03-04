from langchain.vectorstores import FAISS
from langchain.embeddings.huggingface import HuggingFaceEmbeddings
import os
from openai import OpenAI
from dotenv import find_dotenv, load_dotenv
load_dotenv(find_dotenv())
DASHSCOPE_API_KEY=os.environ["DASHSCOPE_API_KEY"]
from langchain_community.llms.tongyi import Tongyi
import numpy as np

# 配置API密钥
client = OpenAI(api_key=DASHSCOPE_API_KEY,base_url="https://dashscope.aliyuncs.com/compatible-mode/v1")

# 读取txt文件并获取每行文本
def load_texts(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        texts = [line.strip() for line in f.readlines() if line.strip() and len(line)<1000]
    return texts


# 创建FAISS索引
def create_faiss_index(texts):
    huggingface_ef=HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2") 

    vector_db=FAISS.from_texts(texts=texts,embedding=huggingface_ef)
    
    return vector_db

# 示例用法
file_path =  "../ExampleData/DialMed.txt"  
texts = load_texts(file_path)

vector_db = create_faiss_index(texts[:10])

vector_db.save_local("../KnowledgeBase/DailMed")





