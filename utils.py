import os
import google.generativeai as genai
from langchain.memory import ConversationBufferMemory
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.chains import ConversationChain
from config import GOOGLE_GENAI_API_KEY, MODEL_NAME  

# Setting up the system prompt
SYS_PROMPT = """You are a helpful data science tutor.
                You can only resolve data-science related queries.
                If someone asks you queries that are not relevant to data science, 
                politely tell them to ask relevant queries only."""

# Initializing Gemini model
def initialize_gemini():
    # Configure the Google Generative AI with the API key
    genai.configure(api_key=GOOGLE_GENAI_API_KEY)

    # Initialize the GoogleGenerativeAI model
    llm = ChatGoogleGenerativeAI(model=MODEL_NAME, google_api_key=GOOGLE_GENAI_API_KEY)

    # Fix memory key to 'history' to match ConversationChain expectations
    memory = ConversationBufferMemory(
        memory_key="history",  # Fixing memory key
        return_messages=True
    )

    # Initialize conversation chain with memory and system prompt
    conversation = ConversationChain(
        llm=llm,
        memory=memory,
        verbose=True
    )

    # Inject the system prompt at the beginning of the conversation
    conversation.memory.save_context(
        {"input": SYS_PROMPT}, 
        {"output": "Understood. Ready to answer data science questions!"}
    )

    return conversation
