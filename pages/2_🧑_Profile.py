# styled_profile_app.py
import streamlit as st
import PIL as Image
def main():
    st.markdown("<h1 style='text-align: center; color: black;'>Title Page</h1>", unsafe_allow_html=True)
    
    # Add styled profile picture with a smaller width
    st.image("profile1.jpg", caption="Jerick C. Jualo", width=250)
    
    st.header("About Me🧑‍🦰:")
    st.write("I'm Jerick C. Jualo, a 19 Year Old BSCpE Student. Born and raised in Quezon CIty and Caloocan City, I find joy in the simple things life has to offer. Whether it's exploring new places, diving into a good book, or spending quality time with family and friends, I believe in cherishing each moment. As I navigate through life, I'm fueled by curiosity, a passion for Lightnovles, Musics, K-Drama and the unwavering support of those around me. Join me on this journey of discovery, growth, and shared experiences.")
   
    # Basic Information
    st.header("Basic Information📰")
    st.write("**Name:** Jerick C. Jualo")
    st.write("**Age:** 19")
    st.write("**Location:** Surigao City, Philippines")
    
    # Skills
    st.header("Skills🤹")
    st.write("Communication Skill")
    st.write("Collaboration Skill")
    st.write("Other Skills: Self Management, Study Skills")
    
    # Education
    st.header("Education🏫🎒")
    st.subheader("Elementary School: Bagumbong Elementary School")
    st.image("ES.jpg", caption="Bagumbong Elementary School")
    st.write("In elementary school, every day felt like a vibrant adventure of friendships, laughter, and the joy of learning. From mastering multiplication tables to the thrill of the schoolyard, those early years shaped the foundation of who I am today, leaving me with cherished memories that continue to influence my journey.")
    st.subheader("High School: Bagumbong High School, Placer National High School")
    st.image("HS.jpg", caption="Bagumbong High School Main")
    st.image("HS1.jpg", caption="Placer National High School")
    st.write("High school was a time of challenges and growth, filled with academic pursuits, friendships, and defining moments. From exams to personal triumphs, those years shaped my identity and prepared me for what lay ahead.")
    st.subheader("University: Surigao Del Norte State University")
    st.write("Year: 1st Year - 2023")
    st.image("COL.jpg", caption="Surigao Del Norte State University")
    st.write("College was a transformative journey of academic exploration, personal growth, and forming lasting connections. From late-night study sessions to moments of triumph, it shaped my identity, fostering resilience and a love for lifelong learning.")
    
    
    st.header("My Inspiration In Life💞")
    st.subheader("My Family👨‍👩‍👧‍👦")
    st.write("My family is my inspiration, and I aspire to give back to them now that I've grown up. They are the reason I keep moving forward, and caring for them is my way of expressing gratitude for the support and love they've given me throughout the years.")
    st.image("album1.jpg")
    st.image("album2.jpg", caption="Jualo Family")
    st.header("My Strengths and Weaknesses")
    st.subheader("Strengths💪:")
    st.write("1. *Adaptability:* I excel in adapting to new situations and finding effective solutions in dynamic environments.")
    st.write("2. *Communication:* With a strong ability to convey ideas clearly, I foster open and effective communication within teams.")
    st.write("3. *Analytical Thinking:* My analytical mindset allows me to approach challenges methodically, breaking them down for strategic problem-solving.")
    st.write("4. *Collaboration:* I thrive in collaborative settings, valuing diverse perspectives and working cohesively toward common goals.")
    st.write("5. *Creativity:* A creative thinker, I enjoy bringing innovative approaches to projects, generating fresh ideas and perspectives.")
    st.subheader("Weaknesses😩:")
    st.write("1. *Perfectionism:* At times, my desire for perfection may lead to spending more time on a task than necessary.")
    st.write("2. *Delegating Tasks:* I'm working on improving my ability to delegate tasks, as I tend to take on too much responsibility.")
    st.write("3. *Impatience:* Occasionally, impatience arises when faced with delays, and I'm actively working on maintaining a more patient mindset.")
    st.write("4. *Public Speaking:* While I am comfortable communicating one-on-one, I am working on enhancing my public speaking skills for larger audiences.")
    st.write("5. *Balancing Workload:* Striking the right balance between work and personal life is an ongoing challenge, and I'm committed to improving this aspect of my time management.")
    # Contact Information
    st.header("Contact Information📄:")
    st.write("Email: jerickjualo4@gmail.com")
    st.write("Facebook: Jerick Castro Jualo")
    
    # You can add more sections or customize as per your needs

if __name__ == "__main__":
    main()
