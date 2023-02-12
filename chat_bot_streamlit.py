import openai
import streamlit as st

st.set_page_config(page_title="ChatGPT", page_icon="🤖")

openai.api_key = "******"

def get_response(prompt):
    request = openai.Completion.create(
        engine = 'text-davinci-003',
        prompt = prompt,
        max_tokens = 1024,
        # top_p = 1,
        n=1,
        stop = 'None',
        temperature=0.6,
    )
    feedback = request.choices[0].text
    return feedback

user_input = st.empty().text_input(label="请输入你要提问的问题, 输入完成后按回车键提交！")
record = []
if len(user_input) > 0:
    with st.spinner("请稍后，chatgpt🤖正在准备答案"):
        st.info(get_response(user_input))