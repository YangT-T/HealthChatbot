from langchain.vectorstores import FAISS
from langchain.embeddings.huggingface import HuggingFaceEmbeddings




def retrieveInfo(input, task):
    
    embeddings=HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
    
    vector_db=FAISS.load_local("../KnowledgeBase/DailMed",embeddings,allow_dangerous_deserialization=True)
    
    query_text = "皮炎"

    retriever = vector_db.as_retriever(k=4)
    
    docs = retriever.invoke(query_text)

    print("相似文本:", docs)
    
    return docs