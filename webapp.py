import main as mn
import streamlit as st

def main():

    st.set_page_config(page_title="swapnil", page_icon=":tada:", layout="wide")
    st.subheader("hi i am swapnil")

    html_temp = """
    
    <body style="background-color:red;">
    """

    st.markdown(html_temp, unsafe_allow_html=True)

    if st.button("Recognise"):
        mn()

if __name__ == "__main__":
    main()