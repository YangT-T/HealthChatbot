from langchain.globals import set_llm_cache
import os
from dotenv import find_dotenv, load_dotenv
load_dotenv(find_dotenv())
DASHSCOPE_API_KEY=os.environ["DASHSCOPE_API_KEY"]
from langchain_community.llms.tongyi import Tongyi





def tongyiChat(input,sideInfo,task):
    llm=Tongyi(api_key=DASHSCOPE_API_KEY)
    result=llm.invoke(input)
    return result