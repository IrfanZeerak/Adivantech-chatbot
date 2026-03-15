from langchain.chat_models import ChatOpenAI
from langchain.schema import HumanMessage

llm = ChatOpenAI(model="gpt-3.5-turbo")

def get_response(user_message):

    response = llm([
        HumanMessage(content=user_message)
    ])

    return response.content