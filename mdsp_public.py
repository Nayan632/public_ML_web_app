import pickle
import sklearn 
import streamlit as st
from streamlit_option_menu import option_menu

diabetes_model = pickle.load(open('diabetes_model.sav','rb'))
heart_disease_model = pickle.load(open('heart_disease_model.sav','rb'))
#parkinsons_model = pickle.load(open('C:\\Users\\nayan\\OneDrive\\Desktop\\MDP\\parkinsons_model.sav','rb'))

with st.sidebar:
    selected = option_menu('Multiple Disease Prediction System',
                           ['Diabetes Prediction',
                            'Heart Disease Prediction'],
                           icons=['activity','heart'],
                           default_index=0)
    
if (selected == 'Diabetes Prediction'):
    
    st.title('Diabetes Prediction using ML')
    
    col1,col2,col3 = st.columns(3)
    
    with col1:
        Pregnancies = st.text_input('Number of Pregnancies')
    with col2:
        Glucose = st.text_input('Glucose Level')
    with col3:
        BloodPressure = st.text_input('Blood Pressure value')
    with col1:
        SkinThickness = st.text_input('Skin Thickness value')
    with col2:
        Insulin = st.text_input('Insulin Level')
    with col3:
        BMI = st.text_input('BMI value')
    with col1:
        DiabetesPedigreeFunction = st.text_input('Diabetes Pedigree Function value')
    with col2:
        Age = st.text_input('Age of the Person')
    
    diab_diagnosis = ''
    
    if st.button('Diabetes Test Result'):
        diab_prediction = diabetes_model.predict([[Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age]])
        if (diab_prediction[0]==1):
            diab_diagnosis = 'The person is Diabetic'
        else:
            diab_diagnosis = 'The person is Not Diabetic'
    st.success(diab_diagnosis)

    
if (selected == 'Heart Disease Prediction'):
    st.title('Heart Disease Prediction using ML')
    col1, col2, col3 = st.columns (3)

    with col1:
    
        age=st.number_input('Age')
    
    with col2:
    
        sex = st.number_input('Sex')
    
    with col3:
    
        cp=st.number_input('Chest Pain types')
    
    with col1:
    
        trestbps = st.number_input('Resting Blood Pressure')
    
    with col2:
    
        chol = st.number_input('Serum Cholestoral in mg/dL')
    
    with col3:
    
        fbs = st.number_input('Fasting Blood Sugar > 120 mg/dl')
    
    with col1:
    
        restecg = st.number_input('Resting Electrocardiographic results')
        
    with col2:

        thalach = st.number_input('Maximum Heart Rate achieved')
    
    with col3:
        
        exang = st.number_input('Exercise Induced Angina')
    
    with col1:
    
        oldpeak = st.number_input('ST depression induced by exercise')
    
    with col2:
    
        slope = st.number_input('Slope of the peak exercise ST segment')
    
    with col3:
    
        ca = st.number_input('Major vessels colored by flourosopy')
    
    with col1:
    
        thal = st.number_input('thal: normal; 1 = fixed defect; 2 reversable defect')
            
        
    heart_diagnosis = ''
    
    if st.button('Heart Disease Test Result'):
        heart_prediction = heart_disease_model.predict([[age,sex,cp,trestbps,chol,fbs,restecg,thalach,exang,oldpeak,slope,ca,thal]])
        if (heart_prediction[0] == 1):
            heart_diagnosis = 'The person is having heart disease'
        else:
            heart_diagnosis = 'The person is not having heart disease'
    st.success(heart_diagnosis)       
    