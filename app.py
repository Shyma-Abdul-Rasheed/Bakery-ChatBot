import streamlit as st
from libs.menu_loader import load_menu
from libs.llm_utils import send_message_to_llm,start_session


st.title("HOME BAKERY AI ASSISTANT")
st.header("Serving in Dubai and Sharjah")

menu=load_menu()

if 'history' not in st.session_state:
    start_session()
    welcome_message=f"""
Welcome to Home Bakery! 🧁🍰🎂
I am your friendly virtual assistant. I can help you view our menu, select items, and place orders.

Here's your menu:
{menu}

Please type your message below to get started!
"""
    st.session_state['history'] = [{"role":"ai","content":welcome_message}]

prompt=st.chat_input("Enter your message : ")
if(prompt):
    st.session_state['history'].append({"role":"user","content":prompt})
    llm_response=send_message_to_llm(prompt)
    st.session_state['history'].append({"role":"ai","content":llm_response})

for m in st.session_state['history']:
    with st.chat_message(m["role"]):
        st.markdown(m["content"])


