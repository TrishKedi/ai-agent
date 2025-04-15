from rag_chroma import load_vector_store, get_similar_docs
from langchain.chat_models import ChatOpenAI
from langchain.schema import HumanMessage, SystemMessage

vectorstore = load_vector_store()

def plan_week(userquery):
    docs = get_similar_docs(vectorstore, userquery)

    preferences = "\n---\n".join([f"{doc.metadata['title']}: {doc.page_content}" for doc in docs])

    systemPrompt = ("You are a helpful weekly planning assistant. Based on the user's preferences and the current command, "
        "generate a structured weekly plan in markdown table format (days vs activities). Include only activities relevant to the command.\n")

    prompt = f"""
        User's Weekly Planning Request:
        "{userquery}"

        User Preferences from Notes:
        {preferences}

        Generate a weekly plan starting from Monday to Sunday.
        """
    
    llm = ChatOpenAI(temperature=0.7)
    response = llm([
        SystemMessage(content=systemPrompt),
        HumanMessage(content=prompt)
    ])

    return response.content