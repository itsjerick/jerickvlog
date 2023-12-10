# hobbies_page.py
import streamlit as st
import PIL as Image
def main():

    # Main content
    st.markdown("<h1 style='text-align: center; color: black;'>Jualo Family</h1>", unsafe_allow_html=True)
    st.markdown("In our family, each member plays a unique role that weaves together the tapestry of our shared journey. From the unwavering support of my parents to the camaraderie with my siblings, our household is a harmonious blend of diverse personalities and shared experiences. We navigate life's ups and downs together, finding strength in each other's company. Laughter echoes through our home, and the bonds forged over time create a strong foundation of love and understanding. Our family is not just a unit; it's a source of comfort, joy, and the unwavering assurance that, no matter what, we are in this together.")
    # Hobbies
    st.markdown("Here's are my Family's Members")
    st.header("Mother")  
    st.write("Here are some of my Mother's basic information")
    st.markdown("Name: Janeth Jualo")
    st.markdown("- Occupation: Housewife")
    st.markdown("- Age:")
    st.markdown("- Birthday:")
    st.markdown("- Role in the Family: My mother is the heart of a family, providing love, guidance, and emotional support. My Mother role involves shaping values, fostering resilience, and creating our warm family dynamic. In partnership with my father, she leaves a lasting impact on the collective journey of our family.")
    st.image("mama.jpg", width=250)
    cols1, cols2 = st.columns(2)
    with cols2:
        # Favorite Books
        st.markdown("<h1 style='text-align: right; color: black;'>Father</h1>", unsafe_allow_html=True)
        st.markdown("<h20 style='text-align: right; color: black;'>Here are some of my Father's basic information</h20>", unsafe_allow_html=True)
        st.markdown("<h20 style='text-align: right; color: black;'>Name: Romualdo Jualo</h20>", unsafe_allow_html=True)
        st.markdown("<h20 style='text-align: right; color: black;'>- Occupation: Tricyle Driver</h20>", unsafe_allow_html=True)
        st.markdown("<h20 style='text-align: right; color: black;'>- Age:</h20>", unsafe_allow_html=True)
        st.markdown("<h20 style='text-align: right; color: black;'>- Birthday:</h20>", unsafe_allow_html=True)
        st.markdown("<h20 style='text-align: right; color: black;'>- Role in the Family:My Father role in our family is a vital source of support, guidance, and security. Beyond providing, he shapes the values and character of me and my brother, fostering a nurturing environment through love and responsibility. In partnership with my mother, father plays a crucial role in instilling discipline and resilience, leaving a lasting impact on our family's journey.</h20>", unsafe_allow_html=True)
    with cols1:
        st.image("papa.jpg",width=250)
    cols3, cols4 = st.columns(2)
    with  cols3:
         st.header("Brother")
         st.write("Here are some of my Brother's basic information")
         st.markdown("Name: Jerome Jualo")
         st.markdown("- Occupation: N/A /Currently Studying")
         st.markdown("- Age:23")
         st.markdown("- Birthday: September 25 2001")
         st.markdown("- Role in the Family: My brother brings companionship and support to the family, sharing experiences and creating a sense of unity through laughter and shared memories. His role is one of camaraderie, understanding, and contributing to the family's collective history.")
    with cols4:
        st.image("kuya.jpg")
   

    
    st.markdown("<h1 style='text-align: center; color: black;'>Family Pictures</h1>", unsafe_allow_html=True)
    st.image("album1.jpg")
    st.image("album2.jpg")
if __name__ == "__main__":
    main()
