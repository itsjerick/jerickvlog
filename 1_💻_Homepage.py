import streamlit as st 

st.set_page_config(
    page_title="Multipage App",
    page_icon="👋",
)

st.sidebar.success("Select a page above")

# app.py
import streamlit as st

def main():
    st.title("Welcome to Jerick Homepage!👋")
    st.write("This is my Blog Website Activity for Programming Logic and Design Subject")
    
    # Add other components as needed
    st.header("About Me")
    st.write("I am Jerick C. Jualo, a Bachelor of Science in Computer Engineering 1-A student")
    
    st.header("My Pages")
    st.write("Here are the pages of this website:")
    st.markdown("- Page 1: [My Profile](#)")
    st.markdown("- Page 2: [My Hoobies](#)")
    st.markdown("- Page 3: [My Family](#)")
    
    st.header("Contact Me")
    st.write("Feel free to reach out to me:")
    st.markdown("- Email: [jerickjualo4@gmail.com](mailto:jerickjualo4@gmail.com)")
    st.markdown("- LinkedIn: [Your LinkedIn Profile](#)")
    
    # You can add more sections or customize as per your needs

if __name__ == "__main__":
    main()
