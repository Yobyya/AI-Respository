from langchain_openai import ChatOpenAI
from langchain.chains import ConversationChain

def AI_Invoke( prompt, openai_api_key, memory):
    model = ChatOpenAI(
        model = "gpt_3.5_turbo",
        openai_api_key = openai_api_key
    )
    chain = ConversationChain(
        mll = model,
        memory = memory
    )

    response = chain.invoke({"user":prompt})

    return response["response"]
