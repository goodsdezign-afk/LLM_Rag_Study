from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough
from src.config.config import CONFIG

def initalize_llm(model_name=None):
    model_name = model_name or CONFIG['model_name']
    return ChatGroq(
        groq_api_key = CONFIG['groq_api_key'],
        model_name = model_name,
        temperature = CONFIG['temperature'],
        max_tokens = CONFIG['max_tokens'], 
    )

llm = initalize_llm()

# RAG prompt
rag_prompt = ChatPromptTemplate.from_template(
    """
    다음 컨텍스트를 바탕으로 질문에 답하세요 : {context} 

    질문 : {question}

    답변을 한국어로 제공해 주세요.   
    """
)

def create_rag_chain():
    global llm
    rag_chain = (
        {"context":lambda x: x["context"], "question":lambda x: x["question"]}
        | rag_prompt
        | llm
        | StrOutputParser()
    )
    return rag_chain

rag_chain = create_rag_chain()

def change_model(model_name):
    global llm, rag_chain
    llm = initalize_llm(model_name)
    rag_chain = create_rag_chain()
    return f"model changed to {model_name}"

def process_with_rag(question, context):
    return rag_chain.invoke({"question": question, "context": context})