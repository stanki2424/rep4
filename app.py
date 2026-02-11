import streamlit as st

# Заглавие и описание
st.title(" Мини Google Form")
st.write("Моля, попълни въпросите по-долу и натисни 'Изпрати'.")

st.divider()

# Въпрос 1
q1 = st.radio(
    "1️ Обичаш ли Python?",
    ("да", "не")
)

# Въпрос 2
q2 = st.number_input(
    "2️ Въведи число:",
    step=1
)

# Въпрос 3
q3 = st.number_input(
    "3️ Колко е 5 × 5?",
    step=1
)

st.divider()

# Бутон за изпращане
if st.button(" Изпрати"):
    
    st.subheader(" Резултати")

    # Проверка въпрос 1
    if q1 == "да":
        st.success("1️ Супер!")
    else:
        st.warning("1️ Ще го харесаш!")

    # Проверка въпрос 2
    if q2 > 10:
        st.success("2️ Голямо число")
    else:
        st.info("2️ Малко число")

    # Проверка въпрос 3
    if q3 == 25:
        st.success("3️ Вярно! Браво!")
    else:
        st.error("3️ Грешно. Правилният отговор е 25.")

    st.balloons()
