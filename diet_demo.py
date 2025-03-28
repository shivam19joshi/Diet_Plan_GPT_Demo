import streamlit as st

def calculate_bmi(weight, height):
    return round(weight / ((height / 100) ** 2), 2)

def get_diet_plan(bmi):
    if bmi < 18.5:
        return "Your BMI indicates that you are underweight. Increase your calorie intake with healthy fats, proteins, and carbs. Consider foods like nuts, dairy, lean meats, and whole grains."
    elif 18.5 <= bmi < 24.9:
        return "Your BMI is normal. Maintain a balanced diet with a mix of proteins, fats, and carbohydrates. Include plenty of fruits and vegetables."
    elif 25 <= bmi < 29.9:
        return "Your BMI suggests you are overweight. Focus on portion control, high-fiber foods, and lean proteins. Cut down on processed foods and sugary drinks."
    else:
        return "Your BMI indicates obesity. Prioritize weight loss with a high-protein, low-carb diet, and regular exercise. Consult a nutritionist for a personalized plan."

def main():
    st.title("Diet Plan Generator")
    
    name = st.text_input("Enter your name:")
    age = st.number_input("Enter your age:", min_value=1, max_value=120, step=1)
    height = st.number_input("Enter your height (cm):", min_value=50.0, max_value=250.0, step=0.1)
    weight = st.number_input("Enter your weight (kg):", min_value=10.0, max_value=300.0, step=0.1)
    
    if weight and height:
        bmi = calculate_bmi(weight, height)
        st.write(f"Hello {name}, your BMI is: {bmi}")
        st.write(get_diet_plan(bmi))

if __name__ == "__main__":
    main()
