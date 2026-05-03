# app.py

import streamlit as st
from modules.resume_parser import extract_text_from_pdf
from modules.skill_extractor import extract_skills_db
from modules.question_generator import generate_questions
from modules.evaluator import evaluate_answers
from streamlit_option_menu import option_menu
import base64              # For video
from modules.aptitude_generator import generate_aptitude_questions      # Aptitude Test
import time



# Performance tracker 



if "technical_score" not in st.session_state:
    st.session_state.technical_score = 0

if "aptitude_score" not in st.session_state:
    st.session_state.aptitude_score = 0

if "progress_history" not in st.session_state:
    st.session_state.progress_history = []
















# Performance tracker

if "technical_score" not in st.session_state:
    st.session_state.technical_score = 0

if "aptitude_score" not in st.session_state:
    st.session_state.aptitude_score = 0

if "progress_history" not in st.session_state:
    st.session_state.progress_history = []

# NEW OPTIONAL METRICS
if "total_tests" not in st.session_state:
    st.session_state.total_tests = 0

if "best_score" not in st.session_state:
    st.session_state.best_score = 0





























































with st.sidebar:
    menu_bar=option_menu(
    menu_title="MENU",
    options=("Home","Resume Vision","Practice Zone","Aptitude Test","Dashboard","HelpBot","AboutUs"),
    icons=( "house","file-earmark-person","laptop","patch-question","bar-chart-line","robot","info-circle"),
    menu_icon="menu-button-wide",
    default_index=0,
    )






if menu_bar=="Home":

# 🎯 AI-Powered Adaptive Interview Preparation System
    # Tagline :


# Simple Professional Interactive Title

    st.markdown(""" 
    <style>
    .simple-hero-card {
        background: linear-gradient(135deg, #203a43, #2c5364);
        padding: 25px;
        border-radius: 18px;
        text-align: center;
        margin-top: 10px;
        margin-bottom: 20px;
        box-shadow: 0 6px 18px rgba(0,0,0,0.18);
    }

    .simple-hero-title {
        font-size: 34px;
        font-weight: 800;
        color: white;
        margin-bottom: 8px;
    }

    .simple-hero-subtitle {
        font-size: 16px;
        color: #dcdcdc;
        font-style: italic;
    }
    </style>

    <div class="simple-hero-card">
        <div class="simple-hero-title">🎯 AI-Powered Adaptive Interview Preparation System</div>
        <div class="simple-hero-subtitle">
            Practice smarter • Build confidence • Crack interviews faster
        </div>
    </div>
    """, unsafe_allow_html=True)















    # Project snapshot

    st.subheader("Project Snapshot")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.info("""
        🎯 **Mission**  
        Deliver personalized interview preparation powered by AI
        """)

    with col2:
        st.success("""
        💡 **Core Idea**  
        Resume → Skill Extraction → AI Questions → Practice → Analytics
        """)

    with col3:
        st.warning("""
        🌍 **Target Users**  
        Students • Freshers • Graduates • Professionals
        """)










   

    # Video code

    # Read video file
    video_path = "assets/video_interview.mp4"

    with open(video_path, "rb") as video_file:
        video_bytes = video_file.read()

    video_base64 = base64.b64encode(video_bytes).decode()

    # Auto-play HTML
    st.markdown(
        f"""
        <style>
        .video-container {{
            width: 100%;
            border-radius: 18px;
            overflow: hidden;
            margin-top: 10px;
            box-shadow: 0 4px 18px rgba(0,0,0,0.25);
        }}
        .video-container video {{
            width: 100%;
            height: auto;
            display: block;
        }}
        </style>

        <div class="video-container">
            <video autoplay loop muted playsinline>
                <source src="data:video/mp4;base64,{video_base64}" type="video/mp4">
            </video>
        </div>
        """,
        unsafe_allow_html=True
    )
   


    st.markdown("---")



    # =========================================================
    # ABOUT THE PROJECT
    # =========================================================
    # ==========================================
    # INTERACTIVE WELCOME / OVERVIEW SECTION
    # ==========================================

    st.markdown("""
    <style>
    .overview-card {
        background: linear-gradient(135deg, #f8fbff, #eaf3ff);
        padding: 30px;
        border-radius: 20px;
        box-shadow: 0 8px 20px rgba(0,0,0,0.12);
        margin-top: 20px;
        margin-bottom: 30px;
    }

    .overview-title {
        text-align: center;
        font-size: 34px;
        font-weight: 800;
        color: #203a43;
        margin-bottom: 20px;
    }

    .highlight-box {
        background: white;
        padding: 18px;
        border-radius: 15px;
        box-shadow: 0 4px 12px rgba(0,0,0,0.08);
        text-align: center;
        transition: 0.3s;
        height: 100%;
    }

    .highlight-box:hover {
        transform: translateY(-6px);
        box-shadow: 0 8px 18px rgba(0,0,0,0.18);
    }

    .highlight-title {
        font-size: 20px;
        font-weight: 700;
        color: #0f2027;
        margin-bottom: 8px;
    }

    .highlight-desc {
        font-size: 15px;
        color: #555;
    }
    </style>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="overview-card">
        <div class="overview-title">🚀 Journey to Interview Success</div>
    </div>
    """, unsafe_allow_html=True)

    st.write("""
    ### This platform helps you prepare smarter by combining:
    - **Resume Analysis** → Understand profile quality & ATS readiness  
    - **Technical Practice** → Personalized interview questions from your skills  
    - **Aptitude Training** → Quantitative + logical reasoning improvement  
    - **Performance Dashboard** → Compare strengths & weaknesses  
    - **AI HelpBot** → Instant career and interview support  
    """)

    # Interactive Metric Cards
    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.markdown("""
        <div class="highlight-box">
            <div class="highlight-title">📄 Resume Ready</div>
            <div class="highlight-desc">Analyze and strengthen your professional profile</div>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("""
        <div class="highlight-box">
            <div class="highlight-title">💻 Technical Growth</div>
            <div class="highlight-desc">Skill-based AI interview preparation</div>
        </div>
        """, unsafe_allow_html=True)

    with col3:
        st.markdown("""
        <div class="highlight-box">
            <div class="highlight-title">🧠 Aptitude Mastery</div>
            <div class="highlight-desc">Boost reasoning and placement confidence</div>
        </div>
        """, unsafe_allow_html=True)

    with col4:
        st.markdown("""
        <div class="highlight-box">
            <div class="highlight-title">📊 Smart Analytics</div>
            <div class="highlight-desc">Track performance and career readiness</div>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("---")

    # Interactive Expanders
    st.subheader("🎯 Explore What You Can Do")

    with st.expander("📄 Resume Vision"):
        st.write("Upload your resume to evaluate ATS score, profile quality, and missing career sections.")

    with st.expander("💻 Practice Zone"):
        st.write("Generate technical interview questions based on your extracted skills.")

    with st.expander("🧠 Aptitude Test"):
        st.write("Practice quantitative aptitude and logical reasoning for placement success.")

    with st.expander("📈 Dashboard"):
        st.write("Compare Practice Zone and Aptitude performance to identify strengths and weaknesses.")

    with st.expander("🤖 HelpBot"):
        st.write("Ask interview questions, coding doubts, aptitude concepts, and career guidance.")


    





elif menu_bar=="Resume Vision":
    st.title("📄 Resume Viewer & Analyzer")
    st.subheader("Upload your resume and analyze its content")

    # Upload Resume
    uploaded_file = st.file_uploader(
        "Upload Your Resume (PDF Only)",
        type=["pdf"]
    )

    if uploaded_file:

        # ==================================
        # STEP 1: Extract Full Resume Text
        # ==================================
        resume_text = extract_text_from_pdf(uploaded_file)

        # ==================================
        # STEP 2: Extract Skills
        # ==================================







        # skills = extract_skills_db(resume_text)











        # ==================================
        # STEP 3: Resume Score Logic
        # ==================================
        score = 0
        feedback = []

        # Contact Info
        if "@" in resume_text:
            score += 10
        else:
            feedback.append("Add email address.")

        if "linkedin" in resume_text.lower():
            score += 5
        else:
            feedback.append("Add LinkedIn profile.")

        if "github" in resume_text.lower():
            score += 5
        else:
            feedback.append("Add GitHub profile.")









        # Skills
        # if len(skills) >= 5:
            # score += 20
        # elif len(skills) >= 3:
            # score += 15
        # else:
        #     score += 5
            # feedback.append("Add more technical skills.")









        # Education
        if "education" in resume_text.lower():
            score += 15
        else:
            feedback.append("Add education section.")

        # Projects
        if "project" in resume_text.lower():
            score += 15
        else:
            feedback.append("Add project section.")

        # Experience
        if "experience" in resume_text.lower() or "internship" in resume_text.lower():
            score += 15
        else:
            feedback.append("Add internship/experience.")

        # Certifications
        if "certification" in resume_text.lower() or "certifications" in resume_text.lower():
            score += 15
        else:
            feedback.append("Add certifications.")

        # ==================================
        # STEP 4: Display Resume Score
        # ==================================
        st.success(f"📊 Resume Score: {score}/100")

        st.progress(score)

        # ==================================
        # STEP 5: Show Detected Skills
        # ==================================







        # st.subheader("💻 Detected Skills")

        # if skills:
        #     for skill in skills:
        #         st.write(f"✅ {skill}")










        # else:
        #     st.warning("No predefined skills detected.")










        # ==================================
        # STEP 6: Missing Sections / Feedback
        # ==================================
        st.subheader("📌 Improvement Suggestions")

        if feedback:
            for item in feedback:
                st.warning(item)
        else:
            st.success("Excellent Resume! Your resume looks strong.")

        # ==================================
        # STEP 7: Resume Summary
        # ==================================
        st.subheader("📝 Resume Summary")






        st.info(
            # f"This resume contains {len(skills)} detected technical skills "





            f"Overall ATS-style score : {score}/100."
        )



        # ==================================
        # STEP 8: View Full Resume
        # ==================================
        with st.expander("📃 View Full Resume Content"):
            st.write(resume_text)



































elif menu_bar=="Practice Zone":

    # Title

    st.title("🧠 Mock Practice ")
    # st.subheader("Upload Resume • Extract Skills • Practice MCQs")




    st.write("")
    st.write("")

    # Upload Resume
    uploaded_file = st.file_uploader("Upload Your Resume (PDF)", type=["pdf"])    

    # Session state for questions
    if "questions" not in st.session_state:
        st.session_state.questions = []




    # If resume uploaded
    if uploaded_file:
    
        # Step 1: Extract text from PDF
        resume_text = extract_text_from_pdf(uploaded_file)

        # Step 2: Extract skills
        skills = extract_skills_db(resume_text)

        # Show extracted skills
        st.subheader("💻 Extracted Skills")

        if skills:
            for skill in skills:
                st.write(f"✅ {skill}")
        else:
            st.warning("No skills found.")

        # Step 3: Generate questions
        if skills and st.button("Generate Questions"):

            with st.spinner("Please wait...."):
                st.session_state.questions = generate_questions(skills)



                                                         
                







    # Store user answers
    user_answers = []

    # Step 4: Show questions safely
    if st.session_state.questions:

        st.subheader("Interview Questions")

        for i, q in enumerate(st.session_state.questions):

            # Safe check for correct format
            if isinstance(q, dict) and "question" in q and "options" in q:

                st.write(f"Q{i+1}: {q['question']}")

                selected_answer = st.radio(
                    "Choose your answer:",
                    q["options"],
                    key=f"question_{i}"
                )

                user_answers.append(selected_answer)

            else:
                st.warning(f"Question {i+1} format error.")

        # Step 5: Submit Answers
        if st.button("Submit Test"):

            # Filter only valid questions
            valid_questions = [
                q for q in st.session_state.questions
                if isinstance(q, dict)
                and "question" in q
                and "correct_answer" in q
            ]

            if valid_questions and len(user_answers) == len(valid_questions):

                score, results = evaluate_answers(
                    valid_questions,
                    user_answers
                )
                
                # Convert to percentage
                technical_percent = int((score / len(valid_questions)) * 100)

                # Store technical score
                st.session_state.technical_score = technical_percent

                # Track total tests
                st.session_state.total_tests += 1

                # Best score tracker
                if technical_percent > st.session_state.best_score:
                    st.session_state.best_score = technical_percent

                # Progress history
                st.session_state.progress_history.append({
                    "type": "Technical",
                    "score": technical_percent
                })

                # Show result
                st.success(
                    f"Your Score: {score}/{len(valid_questions)} ({technical_percent}%)"
                )

                st.subheader("Results")

                for result in results:
                    st.write(result)

            else:
                st.error("Some questions are invalid. Please regenerate.")









elif menu_bar=="Aptitude Test":
    st.title("🧠 Aptitude Test")

    # Category Selection
    category = st.selectbox(
        "Choose Aptitude Category",
        ["Quantitative Aptitude", "Logical Reasoning"]
    )

    # Session state
    if "aptitude_questions" not in st.session_state:
        st.session_state.aptitude_questions = []

    # Generate Questions Button
    if st.button("Generate Questions"):

        with st.spinner("Loading...."):
            st.session_state.aptitude_questions = generate_aptitude_questions(category)

    # Store answers
    user_answers = []

    # Show Questions
    if st.session_state.aptitude_questions:

        st.subheader("Generated Questions")

        for i, q in enumerate(st.session_state.aptitude_questions):

            if isinstance(q, dict) and "question" in q and "options" in q:

                st.write(f"Q{i+1}: {q['question']}")

                selected_answer = st.radio(
                    "Choose your answer:",
                    q["options"],
                    key=f"aptitude_{i}"
                )

                user_answers.append(selected_answer)

        # Submit
        if st.button("Submit"):

            valid_questions = [
                q for q in st.session_state.aptitude_questions
                if isinstance(q, dict)
                and "question" in q
                and "correct_answer" in q
            ]

            if valid_questions and len(user_answers) == len(valid_questions):

                score, results = evaluate_answers(
                    valid_questions,
                    user_answers
                )

                # st.success(f"Your Score: {score}/{len(valid_questions)}")





                aptitude_percent = int((score / len(valid_questions)) * 100)

                # Save aptitude score
                st.session_state.aptitude_score = aptitude_percent

                # Track history
                st.session_state.total_tests += 1

                if aptitude_percent > st.session_state.best_score:
                    st.session_state.best_score = aptitude_percent

                st.session_state.progress_history.append({
                    "type": "Aptitude",
                    "score": aptitude_percent
                })

                st.success(f"Your Score: {score}/{len(valid_questions)} ({aptitude_percent}%)")


























                st.subheader("Results")

                for result in results:
                    st.write(result)

            else:
                st.error("Some questions are invalid. Please regenerate.")













elif menu_bar=="Dashboard":
    import plotly.express as px
    import pandas as pd

    st.title("📊 Performance Dashboard")
    st.subheader("AI-Based Comparative Performance Analysis")

    # =========================
    # SCORES
    # =========================
    technical_score = st.session_state.get("technical_score", 0)
    aptitude_score = st.session_state.get("aptitude_score", 0)

    overall_score = int((technical_score + aptitude_score) / 2)

    # =========================
    # TOP METRICS
    # =========================
    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric("🎯 Overall Score", f"{overall_score}%")

    with col2:
        stronger_area = "Practice Zone" if technical_score > aptitude_score else "Aptitude Test"
        st.metric("💪 Stronger Area", stronger_area)

    with col3:
        weaker_area = "Practice Zone" if technical_score < aptitude_score else "Aptitude Test"
        st.metric("⚠️ Weak Area", weaker_area)

    st.progress(overall_score)

    st.markdown("---")

    # =========================
    # DATAFRAME
    # =========================
    performance_data = pd.DataFrame({
        "Category": ["Practice Zone", "Aptitude Test"],
        "Score": [technical_score, aptitude_score]
    })

    # =========================
    # BAR CHART
    # =========================
    st.subheader("📈 Practice Zone vs Aptitude Comparison")

    fig_bar = px.bar(
        performance_data,
        x="Category",
        y="Score",
        text="Score",
        title="Performance Comparison"
    )

    st.plotly_chart(fig_bar, use_container_width=True)

    # =========================
    # PIE CHART
    # =========================
    st.subheader("🥧 Performance Distribution")

    fig_pie = px.pie(
        performance_data,
        names="Category",
        values="Score",
        title="Score Distribution"
    )

    st.plotly_chart(fig_pie, use_container_width=True)

    # =========================
    # STRENGTHS & WEAKNESSES
    # =========================
    st.subheader("💪 Strengths & Weaknesses Analysis")

    col1, col2 = st.columns(2)

    with col1:
        st.success("Your Strengths")

        if technical_score >= 70:
            st.write("✅ Strong technical/problem-solving skills")

        if aptitude_score >= 70:
            st.write("✅ Good aptitude and reasoning ability")

        if technical_score < 70 and aptitude_score < 70:
            st.write("⚠️ No strong area yet — keep practicing")

    with col2:
        st.warning("Areas to Improve")

        if technical_score < 70:
            st.write("⚠️ Improve coding, technical MCQs, and resume-based questions")

        if aptitude_score < 70:
            st.write("⚠️ Improve quantitative aptitude, logical reasoning, and verbal ability")

    st.markdown("---")

    # =========================
    # FINAL ANALYSIS
    # =========================
    st.subheader("🤖 AI Career Readiness Analysis")

    if overall_score >= 80:
        st.success("🚀 Excellent! You are highly interview-ready.")

    elif overall_score >= 60:
        st.info("📘 Good progress. Focus on weaker section to become placement ready.")

    else:
        st.error("⚠️ You need more structured preparation in both sections.")

    # =========================
    # PERSONALIZED RECOMMENDATION
    # =========================
    if technical_score > aptitude_score:
        st.info("💡 Recommendation: You are stronger technically. Focus more on aptitude rounds for placements.")

    elif aptitude_score > technical_score:
        st.info("💡 Recommendation: You are good at aptitude. Improve technical interviews for better hiring chances.")

    else:
        st.info("💡 Balanced profile. Continue improving both equally.")

            












elif menu_bar=="HelpBot":

    # Chatbot Section Title
    st.markdown("""
        <style>
        .chatbot-container {
            text-align: center;
            padding: 25px;
            margin-top: 20px;
            margin-bottom: 30px;
            background: linear-gradient(135deg, #0f2027, #203a43, #2c5364);
            border-radius: 18px;
            box-shadow: 0 8px 25px rgba(0,0,0,0.25);
        }

        .chatbot-title {
            font-size: 42px;
            font-weight: 800;
            color: white;
            margin-bottom: 10px;
            letter-spacing: 1px;
        }

        .chatbot-subtitle {
            font-size: 18px;
            color: #dcdcdc;
            font-style: italic;
            margin-top: 0;
        }
        </style>

        <div class="chatbot-container">
            <div class="chatbot-title">🤖 AI Interview Assistant</div>
            <div class="chatbot-subtitle">
                Your personal AI-powered guide for coding, aptitude, and interview success.
            </div>
        </div>
        """, unsafe_allow_html=True)













    from langchain_community.chat_models import ChatOllama
    from langchain_community.llms import Ollama
    from langchain_core.prompts import ChatPromptTemplate
    from langchain_core.output_parsers import StrOutputParser
    from langchain_core.runnables import RunnablePassthrough, RunnableLambda
    import streamlit as st


    llm = Ollama(model="llama3.2")
    chat = ChatOllama(model="llama3.2")


    file_text = ""


    def fake_retriever(query: str) -> str:
        global file_text
        if file_text:
            return file_text[:1000]   # limit context
        return "No file uploaded. Answer from general knowledge."

    rag_prompt = ChatPromptTemplate.from_template(
        """Use only the following context to answer the question.
        Context: {context}
        Question: {question}
        Answer:"""
    )


    rag_chain = (
        RunnablePassthrough.assign(
            context=RunnableLambda(lambda x: fake_retriever(x["question"]))
        )
        | rag_prompt
        | chat
        | StrOutputParser()
    )


    def ask_rag(question):
        return rag_chain.invoke({"question": question})


    st.set_page_config(layout="wide")



    if "messages" not in st.session_state:
        st.session_state.messages = []


    for msg in st.session_state.messages:
        with st.chat_message(msg["role"]):
            st.markdown(msg["content"])


    
    user_input = st.chat_input("Ask Anything....")

    if user_input:
        
        st.session_state.messages.append({"role": "user", "content": user_input})

        with st.chat_message("user"):
            st.markdown(user_input)

        
        with st.chat_message("assistant"):
            with st.spinner("Thinking..."):
                response = ask_rag(user_input)
                st.markdown(response)

        
        st.session_state.messages.append({"role": "assistant", "content": response})

    





































elif menu_bar=="AboutUs":

    st.title("ℹ️ About Us")

    st.subheader("🎯 AI-Powered Adaptive Interview Preparation System")

    st.write("""
    The AI-Powered Adaptive Interview Preparation System is a smart career-readiness platform
    designed to help students, freshers, graduates, and professionals prepare for interviews
    in a more personalized and effective way.
    """)

    st.markdown("---")

    # ==========================================
    # WHO WE ARE
    # ==========================================
    st.header("🚀 Who We Are")

    st.write("""
    We aim to transform traditional interview preparation by combining Artificial Intelligence,
    resume analysis, technical practice, aptitude training, and performance analytics
    into one complete system.
    """)

    st.markdown("---")

    # ==========================================
    # OUR MISSION
    # ==========================================
    st.header("🌟 Our Mission")

    st.write("""
    Our mission is to bridge the gap between learning and hiring by providing users with:
    """)

    st.write("✅ Resume Analysis for ATS readiness")
    st.write("✅ Skill-based Technical Interview Practice")
    st.write("✅ Aptitude & Logical Reasoning Preparation")
    st.write("✅ Performance Dashboard for growth tracking")
    st.write("✅ AI HelpBot for interview and career guidance")

    st.markdown("---")

    # ==========================================
    # KEY FEATURES
    # ==========================================
    st.header("💡 Key Features")

    col1, col2 = st.columns(2)

    with col1:
        st.info("""
        📄 Resume Vision  
        Upload and analyze your resume to improve profile strength
        """)

        st.info("""
        💻 Practice Zone  
        Practice technical questions based on your skills
        """)

    with col2:
        st.info("""
        🧠 Aptitude Test  
        Improve quantitative aptitude and logical reasoning
        """)

        st.info("""
        📊 Dashboard  
        Track strengths, weaknesses, and interview readiness
        """)

    st.markdown("---")

    # ==========================================
    # TARGET USERS
    # ==========================================
    st.header("🌍 Who Can Use This Platform?")

    st.write("🎓 Students preparing for placements")
    st.write("💼 Freshers starting career journeys")
    st.write("📚 Graduates improving interview skills")
    st.write("🚀 Professionals upgrading opportunities")

    st.markdown("---")

    # ==========================================
    # TECHNOLOGY
    # ==========================================
    st.header("🛠️ Technologies Used")

    st.write("""
    Python • Streamlit • Resume Parsing • Skill Extraction • AI Models • Performance Analytics
    """)

    st.markdown("---")

    # ==========================================
    # VISION
    # ==========================================
    st.header("🏆 Our Vision")

    st.success("""
    To make interview preparation smarter, personalized, and accessible for everyone.
    """)

    st.markdown("---")

    st.subheader("🌟 Prepare Better Today. Succeed Bigger Tomorrow.")
