# app.py

import streamlit as st
from modules.resume_parser import extract_text_from_pdf
from modules.skill_extractor import extract_skills
from modules.question_generator import generate_questions
from modules.evaluator import evaluate_answers
from streamlit_option_menu import option_menu
import base64              # For video
from modules.aptitude_generator import generate_aptitude_questions      # Aptitude Test



with st.sidebar:
    menu_bar=option_menu(
    menu_title="MENU",
    options=("Home","Practice Zone","Aptitude Test","HelpBot","AboutUs"),
    icons=("house","mortarboard","robot","info-circle"),
    # icons=("house","mortarboard","bar-chart","robot","info-circle"),
    menu_icon="menu-button-wide",
    default_index=0,
    )






if menu_bar=="Home":

#     # Title shows lot more big text but html doesnt

#     st.markdown(
#     """
#     <h1 style='font-size:38px; margin-bottom:0;'>
#          AI-Powered Interview Preparation System
#     </h1>
#     """,
#     unsafe_allow_html=True
# )

    # Tagline :


    st.markdown("""
    <h1 style='text-align: center;'>🎯 AI-Powered Adaptive Interview Preparation System</h1>
    <h3 style='text-align: center; color: gray;'>
    Practice smarter. Crack interviews faster with AI.
    </h3>
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
    st.header("📖 About the Project")

    st.markdown("""
    The **AI-Powered Adaptive Interview Preparation System** is an intelligent career-readiness solution
    built to address the limitations of traditional interview preparation methods.

    Unlike generic platforms, this system personalizes the learning experience by analyzing user resumes,
    identifying domain-specific skills, and generating customized technical, HR, and aptitude interview questions.

    It functions as a complete interview ecosystem where users can:
    - Upload resumes for skill-based profiling  
    - Practice personalized mock interviews  
    - Strengthen aptitude and reasoning  
    - Receive AI-powered feedback  
    - Track growth through analytics dashboards
    """)




    

























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
        skills = extract_skills(resume_text)

        # Show extracted skills
        st.subheader("💻 Extracted Skills")

        if skills:
            for skill in skills:
                st.write(f"✅ {skill}")
        else:
            st.warning("No predefined skills found.")

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

                st.success(
                    f"Your Score: {score}/{len(valid_questions)}"
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
        ["Quantitative Aptitude", "Logical Reasoning", "Verbal Ability"]
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

                st.success(f"Your Score: {score}/{len(valid_questions)}")

                st.subheader("Results")

                for result in results:
                    st.write(result)

            else:
                st.error("Some questions are invalid. Please regenerate.")






















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
    st.title("About")
