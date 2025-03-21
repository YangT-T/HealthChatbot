from Services.ClassificationService import classifyEnquiry
from Services.RetrieveService import retrieveInfo
from Services.ChainService import tongyiChat
from Services.RecommendService import recommend


def handleEnquiry(input, history):
    # Classify the enquiry for further process
    task=classifyEnquiry(input=input)
   
    # Retrieve related information
    sideInfo=retrieveInfo(input=input,task=task)
    
    # Form the prompt and call LLM
    result=tongyiChat(input=input,sideInfo=sideInfo,task=task)
    
    # Futher analyze
    recommendation= recommend(input)
    
    return result,recommendation