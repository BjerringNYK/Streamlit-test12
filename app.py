import streamlit as st 

st.title('Lav din egen sætning')
sentences1 = st.text_input('insert sentences 1:')
sentences2 = st.text_input('insert sentences 2:')
if st.button('Submit'):
    st.write('Sentences1 is:', sentences1)
    st.write('Sentences2 is:', sentences2)

