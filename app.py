import streamlit as st

st.title(" Мини Google Form")
st.write("Моля, попълни въпросите по-долу и натисни 'Изпрати'.")
st.divider()
q1 = st.radio(
    "1️ Обичаш ли Python?",
    ("да", "не")
)
q2 = st.number_input(
    "2️ Въведи число:",
    step=1
)
q3 = st.number_input(
    "3️ Колко е 5 × 5?",
    step=1
)
st.divider()
if st.button(" Изпрати"):
    st.subheader(" Резултати")
    if q1 == "да":
        st.success("1️ Супер!")
    else:
        st.warning("1️ Skill Issue!")
    if q2 > 10:
        st.success("2️ Голямо число")
    else:
        st.info("2️ Малко число")
    if q3 == 25:
        st.success("3️ Вярно! Браво!")
    else:
        st.error("3️ Грешно. Правилният отговор е 25.")
    st.balloons()
