from langchain_google_genai import ChatGoogleGenerativeAI


def create_llm():
    return ChatGoogleGenerativeAI(
        model="gemini-3.1-flash-lite",
        temperature=0
    )