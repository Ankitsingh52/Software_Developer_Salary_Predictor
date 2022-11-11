import streamlit as st
import pickle
import numpy as np

def load_model():
    with open('saved_steps.pkl', 'rb') as file:
        data = pickle.load(file)
    return data

data = load_model()

regressor = data["model"]
le_country = data["le_country"]
le_education = data["le_education"]
c_salary = 20431.56
def show_predict_page():
    st.title("Software Developer Salary Prediction")

    st.write("""### We need some information to predict the salary""")

    countries = (
        "India",
        "United States",
        "United Kingdom",
        "Germany",
        "Canada",
        "Brazil",
        "France",
        "Spain",
        "Australia",
        "Netherlands",
        "Poland",
        "Italy",
        "Russian Federation",
        "Sweden",
    )

    education = (
        "Less than a Bachelors",
        "Bachelor’s degree",
        "Master’s degree",
        
    )

    country = st.selectbox("Country", countries)
    education = st.selectbox("Education Level", education)

    experience = st.slider("Years of Experience", 0, 50, 3)

    ok = st.button("Calculate Salary")
    if ok:
        X = np.array([[country, education, experience ]])
        X[:, 0] = le_country.transform(X[:,0])
        X[:, 1] = le_education.transform(X[:,1])
        X = X.astype(float)

        salary = regressor.predict(X)
        if country == 'India' and experience < 3 and education != "Master’s degree":
            salary = c_salary
            st.subheader(f"The estimated salary is ${salary:.2f}")
        else:
            st.subheader(f"The estimated salary is ${salary[0]:.2f}")
        #st.subheader(f"The estimated salary is ${salary[0]:.2f}")
        if country == 'India':
            salary = salary * 81.98;
            if experience < 3 and education != "Master’s degree":
                st.subheader(f"The estimated salary in INR is ₹{salary:.2f}")
            else:
                st.subheader(f"The estimated salary in INR is ₹{salary[0]:.2f}")
        elif country == 'United Kingdom':
            salary = salary * 0.88;
            st.subheader(f"The estimated salary in GBP is £{salary[0]:.2f}")
        elif country == 'Germany' or country == 'France' or country == 'Spain' or country == 'Italy' or country == 'Netherlands':
            salary = salary * 1.00;
            st.subheader(f"The estimated salary in EUR is €{salary[0]:.2f}")
        elif country == 'Canada':
            salary = salary * 1.35;
            st.subheader(f"The estimated salary in CAD is ${salary[0]:.2f}")
        elif country == 'Brazil':
            salary = salary * 5.04;
            st.subheader(f"The estimated salary in BRL is R${salary[0]:.2f}")
        elif country == 'Sweden':
            salary = salary * 11.01;
            st.subheader(f"The estimated salary in SEK is {salary[0]:.2f} kr")
        elif country == 'Australia':
            salary = salary * 1.55;
            st.subheader(f"The estimated salary in AUD is ${salary[0]:.2f}")
        elif country == 'Poland':
            salary = salary * 4.71;
            st.subheader(f"The estimated salary in PLN is zł{salary[0]:.2f}")
        elif country == 'Russian Federation':
            salary = salary * 62.00;
            st.subheader(f"The estimated salary in RUB is ₽{salary[0]:.2f}")
