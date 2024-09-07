import streamlit as st
from langchain.chains.conversation.base import ConversationChain
from langchain.memory import ConversationBufferMemory
from streamlit import session_state
from AI_Invoke import AI_Invoke


#大标题
st.title("Yoby's daugther")

#侧边栏
with st.sidebar:
    openai_api_key = st.text_input( "请输入你的api秘钥", type = "password")
    st.markdown("[获取api秘钥](https://platform.openai.com/account/api-keys)")

#记忆
if "memory" not in st.session_state:
    st.session_state["memory"] = ConversationBufferMemory(
        return_messages = True
    )

    st.session_state["message"] = [{
        "role":"ai",
        "content":"你好呀，我是一个由我爸创造的聊天机器人灵魂"
    }]

#聊天信息输出
for message in st.session_state["message"]:
    st.chat_message(message["role"]).write(message["content"])

#信息输入框
prompt = st.chat_input()
if prompt:
    #api检测
    if not openai_api_key:
        st.info("请输入你的api秘钥")
        st.stop()

    st.session_state["message"].append({
        "role":"human",
        "content":prompt
    })
    st.chat_message("human").write(prompt)

    #调用ai，回答并存储记忆
    response = AI_Invoke(prompt , openai_api_key , st.session_state["memory"])
    st.session_state["message"].append({
        "role":"ai",
        "content":response
    })
    st.chat_message("ai").write(response)


