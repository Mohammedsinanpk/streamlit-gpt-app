import streamlit as st
from openai import OpenAI
user= OpenAI(api_key="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")
userrole = "user"
input_text= st.text_input("try searching something")
button = st.button("search")
if button:
    response = user.chat.completions.create(
        model = "gpt-3.5-turbo",
        messages= [
            {"role": userrole, "content": input_text}
        ]
    )
    st.write(response.choices[0].message.content)