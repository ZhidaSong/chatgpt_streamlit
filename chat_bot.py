# chat_bot.py
 
import openai
import streamlit as st
from streamlit_chat import message
 
#申请的api_key
openai.api_key = "******" 

# model：模型名词
# prompt：您对机器人提出的问题
# temperature：温度参数，该参数控制生成文本的随机性级别。较高的温度参数会导致更多变化且可能不太连贯的响应，而较低的t温度参数会产生更可预测且可能更连贯的响应。
# max_tokens：应答语句的长度 

def generate_response(prompt):
    completion=openai.Completion.create(
        model='text-davinci-003',
        prompt=prompt,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.6
    )
    message=completion.choices[0].text
    return message
 
st.markdown("#### 我是ChatGPT聊天机器人，请不要输入任何个人隐私！")
if 'generated' not in st.session_state:
    st.session_state['generated'] = []
if 'past' not in st.session_state:
    st.session_state['past'] = []
user_input=st.text_input("请输入您的问题:",key='input')
if user_input:
    output=generate_response(user_input)
    st.session_state['past'].append(user_input)
    st.session_state['generated'].append(output)
if st.session_state['generated']:
    for i in range(len(st.session_state['generated'])-1, -1, -1):
        message(st.session_state["generated"][i], key=str(i))
        message(st.session_state['past'][i], 
                is_user=True, 
                key=str(i)+'_user')