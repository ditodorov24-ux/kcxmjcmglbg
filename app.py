import streamlit as st

st.title("Анкета")

name = st.text_input("Въведете име")
age = st.number_input("Въведете възраст", min_value=0, max_value=30, step=1)

grade = st.number_input(
    "Въведете оценка (2–6)",
    min_value=2,
    max_value=6,
    step=1
)

student_class = st.selectbox(
    "Изберете клас",
    ["-- изберете клас --", "1 клас", "2 клас", "3 клас", "4 клас",
     "5 клас", "6 клас", "7 клас", "8 клас", "9 клас",
     "10 клас", "11 клас", "12 клас"]
)

if st.button("Провери"):
    errors = []

    if age < 7 or age > 18 :
        errors.append("Възрастта трябва да бъде от 7 до 18 години.")

    if grade < 2 or grade > 6:
        errors.append("Оценката трябва да бъде между 2 и 6.")

    if student_class == "-- изберете клас --":
        errors.append("Моля, изберете клас.")

    if errors:
        st.error("❌ Има грешки при въвеждането:")
        for e in errors:
            st.write(f"- {e}")
    else:
        st.success("✅ Данните са валидни!")
        st.write(f"Име: {name}")
        st.write(f"Възраст: {age}")
        st.write(f"Клас: {student_class}")
        st.write(f"Оценка: {grade}")

        if grade >= 3:
            st.info("📘 Ученикът е издържал.")
        else:
            st.warning("📕 Ученикът не е издържал.") 
           
          subject = st.selectbox(
    "Изберете предмет",
    [
        "-- изберете предмет --",
        "Математика",
        "Български език",
        "Английски език",
    ]
)
if subject == "-- изберете предмет --":
    st.error("Моля, изберете предмет.")
else:
    st.success(f"Избран предмет: {subject}")
    
st.write(f"Предмет: {subject}")

            
