# hobbies_page.py
import streamlit as st
import PIL as Image
def main():


    # Main content
    st.markdown("<h1 style='text-align: center; color: red;'>My Hobbies</h1>", unsafe_allow_html=True)
    st.markdown("I'm a passionate bookworm, music enthusiast, and TV show aficionado. Whether I'm lost in the pages of a novel, grooving to a favorite tune, or binge-watching compelling series, these hobbies are my go-to for relaxation and inspiration. Join me in the world of stories, melodies, and captivating narratives!")
    # Hobbies
    st.header("Hobbies")
    
    st.write("In my free time, I enjoy the following hobbies:")
    
    st.markdown("Coding and Programming💻")
    st.markdown("- Reading Books like Lightnovels and Webnovels📚")
    st.markdown("- Watching K-Dramas📺")
    st.markdown("- Practicing Guitar🎸")
    st.markdown("- Sleeping and Lazing around🛌😪")
    st.header("Reading Books:")
    st.markdown("Reading is my cherished hobby, offering endless joy and intellectual growth. The magic of words on a page transports me to diverse worlds, from gripping mysteries to heartwarming romances. This versatile pastime is not just an escape but a journey of self-discovery. The tangible feel of a book and the act of turning its pages create a sensory experience that contrasts beautifully with our screen-dominated world. In essence, reading is more than a hobby; it's a lifelong passion shaping my thoughts and enriching my life.")
    st.markdown("<h1 style='text-align: left; color: yellow;'>Favorite Books</h1>", unsafe_allow_html=True)
    st.markdown("<h20 style='text-align: right; color: black;'>Here some of my favorite books:</h20>", unsafe_allow_html=True)
    st.markdown("<h20 style='text-align: right; color: black;'>:book: *Mother of Learning* by nobody103</h20>", unsafe_allow_html=True)
    st.markdown("<h20 style='text-align: right; color: black;'>:book: *Renegade Immortal* by Er Gen</h20>", unsafe_allow_html=True)
    st.markdown("<h20 style='text-align: right; color: black;'>:book: *The Desolate Era* by I Eat Tomatoes</h20>", unsafe_allow_html=True)
        
    st.image("books.jpg",width=400  )
    st.header("Listening to Music")
    st.markdown("Listening to music isn't just a hobby; it's a soul-soothing journey that adds rhythm to my life. Whether I'm discovering new artists or revisiting classics, each note becomes a soundtrack to my emotions. It's more than melodies; it's a cherished ritual that weaves harmony into the fabric of my everyday existence.")
    st.markdown("<h1 style='text-align: left; color: green;'>Favorite Music</h1>", unsafe_allow_html=True)
    st.write("Here's my favorite Artist:")
    st.markdown("🎸- New Jeans")
    st.markdown("🎺- Joji")
    st.markdown("☁️- JVKE")
    st.markdown("🎤- Arthur Miguel")
    st.image("musics.jpg",width=400)
    st.header("Watching K-Dramas")
    st.markdown("Immersing myself in the world of K-dramas has become a cherished hobby that transcends mere entertainment. The captivating narratives, rich cultural tapestry, and compelling characters transport me to a realm where emotions unfold in every scene.Watching K-dramas isn't just a pastime; it's a delightful journey into storytelling, cultural exploration, and the joy of connecting with narratives that resonate on a deeply personal level.")
    st.markdown("<h1 style='text-align: left; color: blue;'>Favorite Dramas</h1>", unsafe_allow_html=True)
    st.markdown("<h20 style='text-align: right; color: black;'>Here are some of my Favorite Movies and TV Shows:</h20>", unsafe_allow_html=True)
    st.markdown("<h20 style='text-align: right; color: black;'>🍉*Twinkling Watermelon*</h20>", unsafe_allow_html=True)
    st.markdown("<h20 style='text-align: right; color: black;'>🌞*My Beloved Summer*</h20>", unsafe_allow_html=True)
    st.markdown("<h20 style='text-align: right; color: black;'>✈️*Crash Landing On You*</h20>", unsafe_allow_html=True)
    st.image("kdrama.jpg",width=400)
    # You can add more sections or customize as per your needs

if __name__ == "__main__":
    main()
