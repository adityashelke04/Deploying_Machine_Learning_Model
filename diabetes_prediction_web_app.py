"""
Created on Mon Oct 27

@author: adiboss
"""

import numpy as np
import pickle
import streamlit as st


#loading the saved model
loaded_model = pickle.load(open('D:/ML Projects/Deploying a ML Model/trained_model.sav', 'rb')) #rb - reading the binary file

#creating a function for prediction

def diabetes_prediction(input_data):
    
    #changing the input data into numpy array
    input_data_as_numpy_array = np.asarray(input_data)

    #reshape the array as we are predicting for one instance - #IF WE DONT RESHAPE IT EXPECTS 768 array(total)
    input_data_reshaped = input_data_as_numpy_array.reshape(1,-1) #reshaping - telling that we are giving 1 array


    prediction = loaded_model.predict(input_data_reshaped)
    print(prediction) #output should be 0 - non diabetic, ie: predict the outcome as 0

    if (prediction[0] == 0): #prediction is a list so index is required (has only 1 value in the list anyways)
         return 'The person is non-diabetic'
    else:
         return 'The person is diabetic'
     
        
def main():
    
    #giving a title
    st.title("Diabetes Prediction Web Application")
    
    #getting the input data from the user
    
    Pregnancies = st.text_input('Number of Pregnancies')
    Glucose = st.text_input('Glucose Level')
    BloodPressure = st.text_input('Blood Pressure Value')
    SkinThickness = st.text_input('Skin Thickness Value')
    Insulin = st.text_input('Insulin Level')
    BMI = st.text_input('BMI Value')
    DiabetesPedigreeFunction = st.text_input('Diabetes Pedigree Function Value')
    Age = st.text_input('Age of the Person')
    
    #code for prediction
    diagnonsis = ''
    
    #creating a button for prediction
    
    if st.button("Diabetes Test Result"):
        diagnonsis = diabetes_prediction([Pregnancies,Glucose,BloodPressure,SkinThickness,Insulin,BMI,DiabetesPedigreeFunction,Age])
        
    st.success(diagnonsis)
    
if __name__ == '__main__':
    main()
    
    
    
    
    
    
    