import streamlit as st
import pandas as pd
import joblib


# -------------------------
# Load trained AI model
# -------------------------

model = joblib.load("TractionScore_AI.pkl")


# -------------------------
# Page setup
# -------------------------

st.set_page_config(
    page_title="TractionScore AI",
    page_icon="🧬"
)


st.title("TractionScore AI")

st.write(
"""
### Screening tool for clinically significant traction alopecia

This research prototype uses patient-reported hair-care practices 
to estimate the likelihood of clinically significant traction alopecia.
"""
)


# -------------------------
# Patient questions
# -------------------------


age = st.number_input(
    "How old are you (years)?",
    min_value=5,
    max_value=100,
    value=25
)


hairstyle_days = st.number_input(
    "On average, how many days do you keep one hairstyle before changing it?",
    min_value=0,
    max_value=365,
    value=14
)


relaxer_answer = st.radio(
    "Do you currently use chemical hair relaxers or perm texturizers?",
    [
        "No",
        "Yes"
    ]
)


if relaxer_answer == "Yes":
    relaxer_use = 1
else:
    relaxer_use = 0



relaxer_frequency = st.number_input(
    "How many times per year do you chemically relax or touch up your hair?",
    min_value=0,
    max_value=30,
    value=0
)


age_first_relaxed = st.number_input(
    "At what age did you first start chemically relaxing your hair?",
    min_value=0,
    max_value=100,
    value=0
)


professional_stylist = st.number_input(
    "Out of your last 10 hairstyles, how many were done by a professional stylist?",
    min_value=0,
    max_value=10,
    value=5
)


headgear_hours = st.number_input(
    "Average weekly hours wearing tight headgear?",
    min_value=0,
    max_value=168,
    value=0
)


heat_styling_monthly = st.number_input(
    "How many times per month are heat styling tools applied?",
    min_value=0,
    max_value=100,
    value=0
)



symptom_answer = st.radio(
    "After hairstyles, do you experience pain, tenderness, severe itching, pimples, or sores?",
    [
        "No",
        "Yes"
    ]
)


if symptom_answer == "Yes":
    scalp_symptoms = 1
else:
    scalp_symptoms = 0



pain_duration_days = st.number_input(
    "If you experience pain, how many days does discomfort last?",
    min_value=0,
    max_value=365,
    value=0
)



# -------------------------
# Prediction
# -------------------------


if st.button("Calculate TractionScore"):


    patient_data = pd.DataFrame({

        "age":[age],

        "hairstyle_days":[hairstyle_days],

        "relaxer_use":[relaxer_use],

        "relaxer_frequency":[relaxer_frequency],

        "age_first_relaxed":[age_first_relaxed],

        "professional_stylist":[professional_stylist],

        "headgear_hours":[headgear_hours],

        "heat_styling_monthly":[heat_styling_monthly],

        "scalp_symptoms":[scalp_symptoms],

        "pain_duration_days":[pain_duration_days]

    })


    prediction = model.predict(patient_data)[0]


    probability = model.predict_proba(patient_data)[0][1]


    st.divider()

    st.subheader("TractionScore AI Result")


    st.write(
        f"Estimated probability: {probability*100:.1f}%"
    )


    if prediction == 1:


        st.error(
        "Higher likelihood of clinically significant traction alopecia."
        )


        st.subheader("Hair health recommendations")

        st.markdown(
        """
        - Avoid hairstyles that cause pain or scalp tenderness.
        - Reduce prolonged tight hairstyles.
        - Alternate protective hairstyles.
        - Allow recovery periods between styles.
        - Reduce frequent chemical relaxing.
        - Minimize excessive heat exposure.
        - Seek professional evaluation if thinning progresses.
        """
        )


    else:


        st.success(
        "Lower likelihood of clinically significant traction alopecia."
        )


        st.subheader("Hair health recommendations")

        st.markdown(
        """
        - Continue gentle hair-care practices.
        - Avoid painful hairstyles.
        - Monitor for changes in hair density.
        - Maintain scalp health.
        """
        )


st.caption(
"TractionScore AI is a research prototype and does not replace medical evaluation."
)
