import streamlit as st
from google import genai
from dotenv import load_dotenv
import os

load_dotenv()
API_KEY = os.getenv("GEMINI_API_KEY")

client = genai.Client(api_key=API_KEY)

if 'page' not in st.session_state:
    st.session_state.page = 0
if 'responses' not in st.session_state:
    st.session_state.responses = {}

def next_page():
    st.session_state.page += 1

def prev_page():
    st.session_state.page -= 1

def page_personal():
    st.title("Student Mental Health & Lifestyle Assessment")
    st.subheader("Step 1: Personal Information")

    with st.form("form_personal"):
        age = st.number_input("Age", min_value=15, max_value=40)
        gender = st.selectbox("Gender", ["Male", "Female", "Non-binary", "Prefer not to say"])
        living_area = st.selectbox("Where do you currently live?",
                                   ["On-campus", "Off-campus (shared)", "Off-campus (alone)", "With family"])
        submitted = st.form_submit_button("Next")
        if submitted:
            st.session_state.responses.update({
                "age": age,
                "gender": gender,
                "living_area": living_area,
            })
            next_page()

def page_lifestyle():
    st.subheader("Step 2: Lifestyle Metrics")

    with st.form("form_lifestyle"):
        st.markdown("###Sleep Habits")
        sleep_hours = st.slider("Average sleep per night (hours)", 0, 12, 7)
        sleep_quality = st.selectbox("How would you rate your sleep quality?", ["Poor", "Fair", "Good", "Excellent"])
        sleep_consistency = st.selectbox("Is your sleep schedule consistent?", ["Yes", "No"])

        st.markdown("###Diet & Nutrition")
        meals = st.selectbox("How many meals do you eat daily?", ["1", "2", "3", "More than 3"])
        diet_quality = st.selectbox("How would you rate your overall diet?", ["Poor", "Average", "Healthy"])
        caffeine = st.selectbox("Do you consume caffeine daily (coffee, energy drinks)?", ["No", "Yes"])

        st.markdown("###Physical Activity")
        exercise_freq = st.selectbox("How often do you exercise?", ["Never", "1–2x/week", "3–5x/week", "Daily"])
        sedentary_time = st.slider("Average hours spent sitting per day", 0, 16, 6)

        st.markdown("###Digital Behavior")
        screen_time = st.slider("Total screen time per day (hours)", 0, 16, 6)
        social_media_time = st.slider("Social media usage per day (hours)", 0, 12, 3)
        screen_before_sleep = st.selectbox("Do you use screens right before sleeping?", ["Yes", "No"])

        col1, col2 = st.columns([1,1])
        if col1.form_submit_button("Back"):
            prev_page()
        if col2.form_submit_button("Next"):
            st.session_state.responses.update({
                "sleep_hours": sleep_hours,
                "sleep_quality": sleep_quality,
                "sleep_consistency": sleep_consistency,
                "meals": meals,
                "diet_quality": diet_quality,
                "caffeine": caffeine,
                "exercise_freq": exercise_freq,
                "sedentary_time": sedentary_time,
                "screen_time": screen_time,
                "social_media_time": social_media_time,
                "screen_before_sleep": screen_before_sleep
            })
            next_page()

def page_academic():
    st.subheader("Step 3: Academic & Routine Metrics")

    with st.form("form_academic"):
        st.markdown("###Academic Load")
        courses = st.slider("Number of enrolled courses", 1, 10, 5)
        study_hours = st.slider("Average study hours per day", 0, 12, 3)
        academic_stress = st.select_slider("How much academic stress do you feel?",
                                           options=["None", "Low", "Moderate", "High", "Extreme"])

        st.markdown("###Time Management")
        routine_regular = st.selectbox("Do you follow a daily routine?", ["Yes", "No", "Sometimes"])
        procrastination = st.selectbox("Do you frequently procrastinate?", ["Never", "Sometimes", "Often", "Always"])
        productive_hours = st.slider("How many productive hours do you have per day?", 0, 12, 4)

        col1, col2 = st.columns([1,1])
        if col1.form_submit_button("Back"):
            prev_page()
        if col2.form_submit_button("Next"):
            st.session_state.responses.update({
                "courses": courses,
                "study_hours": study_hours,
                "academic_stress": academic_stress,
                "routine_regular": routine_regular,
                "procrastination": procrastination,
                "productive_hours": productive_hours,
            })
            next_page()

def page_emotional():
    st.subheader("Step 4: Emotional & Social Well-being")

    with st.form("form_emotional"):
        st.markdown("###Mood & Mental State")
        mood_level = st.slider("Rate your average mood (1 = bad, 10 = great)", 1, 10, 6)
        mental_health_score = st.slider("Rate your overall mental health (1 = poor, 10 = excellent)", 1, 10, 5)
        anxiety_level = st.select_slider("How often do you feel anxious?",
                                         ["Never", "Rarely", "Sometimes", "Often", "Always"])

        st.markdown("###Social Connection")
        loneliness = st.selectbox("Do you feel lonely?", ["Never", "Rarely", "Sometimes", "Often", "Always"])
        social_time = st.slider("Hours spent with friends/family per week", 0, 40, 5)
        has_support = st.selectbox("Do you have someone to talk to about problems?", ["Yes", "No", "Sometimes"])

        col1, col2 = st.columns([1,1])
        if col1.form_submit_button("Back"):
            prev_page()
        if col2.form_submit_button("Next"):
            st.session_state.responses.update({
                "mood_level": mood_level,
                "mental_health_score": mental_health_score,
                "anxiety_level": anxiety_level,
                "loneliness": loneliness,
                "social_time": social_time,
                "has_support": has_support
            })
            next_page()

def page_environment():
    st.subheader("Step 5: Environment, Health, and Financial Factors")

    with st.form("form_environment"):
        st.markdown("###Living Environment")
        roommate_conflict = st.selectbox("Do you have conflicts with roommates?", ["No", "Occasionally", "Frequently"])
        noise_level = st.selectbox("Is your environment noisy?", ["Quiet", "Sometimes noisy", "Very noisy"])
        comfort = st.selectbox("Do you feel comfortable and safe in your space?", ["Yes", "No", "Sometimes"])

        st.markdown("###Financial Stress")
        part_time = st.selectbox("Do you work a part-time job?", ["No", "Yes"])
        work_hours = st.slider("How many hours/week do you work (if applicable)?", 0, 40, 0)
        financial_stress = st.selectbox("Do you feel financial pressure?", ["No", "Somewhat", "Yes"])

        st.markdown("###Physical Health & Habits")
        chronic_conditions = st.selectbox("Do you have any chronic illnesses?", ["No", "Yes"])
        checkups = st.selectbox("Do you get regular health check-ups?", ["Yes", "No"])
        substance_use = st.selectbox("Do you use any substances (alcohol, tobacco, drugs)?", ["No", "Sometimes", "Frequently"])

        col1, col2 = st.columns([1,1])
        if col1.form_submit_button("Back"):
            prev_page()
        if col2.form_submit_button("Next"):
            st.session_state.responses.update({
                "roommate_conflict": roommate_conflict,
                "noise_level": noise_level,
                "comfort": comfort,
                "part_time": part_time,
                "work_hours": work_hours,
                "financial_stress": financial_stress,
                "chronic_conditions": chronic_conditions,
                "checkups": checkups,
                "substance_use": substance_use
            })
            next_page()

def page_result():
    st.subheader("Mental Health Summary")

    with st.spinner("Analyzing your data ."):
        prompt = f"""
            You are an expert mental health counselor.

            A university student completed this survey:

            {st.session_state.responses}

            Please provide:
            - A concise summary of the student's current mental health condition.
            - 2-3 personalized suggestions to improve their lifestyle or well-being.
            - Any critical concerns visible in the data.
            - Talk like a professional adviser rather than talking like an AI. Don't start like Alright, Sure, Great. Start like Hii dear, Hey dude someting like this so that user feels like they are consulting from a doctor rather than an AI
            - Use specific and accurate points rather than larger paragraph so that student don't get bored and can easily read and understand what a counsellor wants to say.
            - Talk like a counsellor, use easy language rather than more complex words.
            """

        try:
            response = client.models.generate_content(
                model="gemini-2.5-pro",
                contents=[prompt]
            )
            st.markdown("###Feedback Report")
            st.write(response.text)
        except Exception as e:
            st.error(f"Error calling Gemini API: {e}")

    if st.button("Back"):
        prev_page()


PAGES = [
    page_personal,
    page_lifestyle,
    page_academic,
    page_emotional,
    page_environment,
    page_result
]

PAGES[st.session_state.page]()
