import streamlit as st

st.title("Мини Google Form")
st.write("Моля, попълни въпросите по-долу и натисни 'Изпрати'.")

st.divider()
q1 = st.radio(
    "1. Обичаш ли Python?",
    ("да", "не")
)
q2 = st.number_input(
    "2. Въведи число:",
    step=1
)
q3 = st.number_input(
    "3. Колко е 5 × 5?",
    step=1
)
q4 = st.selectbox(
    "4. Кой език използваме в този проект?",
    ("Python", "Java", "C++", "JavaScript")
)
q5 = st.slider(
    "5. Колко ти харесва този формуляр? (1-10)",
    1, 10
)

st.divider()
if st.button("Изпрати"):
    st.subheader("Резултати")
    if q1 == "да":
        st.success("Супер!")
    else:
        st.warning("Ще го харесаш!")
    if q2 > 10:
        st.success("Голямо число")
    else:
        st.info("Малко число")
    if q3 == 25:
        st.success("Вярно! Браво!")
    else:
        st.error("Грешно. Правилният отговор е 25.")
    if q4 == "Python":
        st.success("Правилен избор!")
    else:
        st.error("Не съвсем. Правилният отговор е Python.")
    if q5 >= 8:
        st.success("Радваме се, че ти харесва!")
    elif q5 >= 5:
        st.info("Благодарим за обратната връзка!")
    else:
        st.warning("Ще се постараем да го подобрим!")
    st.balloons()
        st.error("3️ Грешно. Правилният отговор е 25.")
    st.balloons()
