# from dotenv import load_dotenv
# load_dotenv()

# from langchain.llms import openai
from langchain_openai import ChatOpenAI
import streamlit as st
import time

llm = ChatOpenAI()

st.title('인공지능 시인')
contents = st.text_input('시의 주제를 제시해 주세요')

if st.button('시 작성 요청하기'):
    with st.spinner('시 작성 중......'):
        result = llm.invoke(contents + '에 대한 시를 써 줘')
        st.write(result)
    