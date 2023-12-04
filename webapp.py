import numpy as np
import pickle
import pandas as pd
import streamlit as st

#loading the model
pickle_in = open('xgb_model1.pkl','rb')
classifier = pickle.load(pickle_in)


def welcome():
    return "Welcome to the Tour Package purchase prediction page"

def predict_purchase(input_data):
    
    prediction = classifier.predict(input_data)
    print(prediction)
    
    if (prediction == 0):
        return "Customer will not purchase the travel package"
    else:
        return "Customer will purchase the travel package"
    



def main():
    st.title('Tour Package Purchase Prediction')
    Age = st.number_input('Age',min_value=17,max_value=80)
    
    
    col1, col2 = st.columns(2)
    
    with col1:
        DurationOfPitch = st.number_input('Duration of Pitch')
        
    with col2:
        NumberOfPersonVisiting = st.number_input('Number of Person Visiting',min_value=int(1))
        
    st.write("Enter '1' if yes else '0' for the questions in the next row")
    
    col3, col4, col5 = st.columns(3)
    
    with col3:
        MaritalStatus_Married = st.number_input('Married?',min_value=int(0),max_value=int(1))
    
    with col4:
        MaritalStatus_Single = st.number_input("Single?",min_value=int(0),max_value=int(1))
        
    with col5:
        MaritalStatus_Unmarried = st.number_input("In a Relation but Unmarried?",min_value=int(0),max_value=int(1))
    
    col6, col7 = st.columns(2)
    
    with col6:
        PreferredPropertyStar = st.number_input('Peferred Propert Star', min_value=float(3),max_value=float(5))
        
    with col7:
        NumberOfChildrenVisiting = st.number_input('Number of Children Visiting',min_value=float())
        
    
    st.write("Enter '1' if yes else '0' for the questions in the next row")
    
    col8, col9, col10 = st.columns(3)
    
    with col8:
        Occupation_Large_Business = st.number_input("Owner of a large business firm?",min_value=int(0),max_value=int(1))
    
    with col9:
        Occupation_Salaried = st.number_input("Salaried employee?",min_value=int(0),max_value=int(1))
    
    with col10:
        Occupation_Small_Business = st.number_input("Owns a small business?",min_value=int(0),max_value=int(1))
    
    NumberOfFollowups = st.number_input('Number Of Followups',min_value=0)
    
    MonthlyIncome = st.number_input('Monthly Income')
    
    
    
    #code for prediction
    result = ''
       
    # Creating button for prediction
    if st.button('Prediction'):
        result = predict_purchase([[Age,DurationOfPitch,NumberOfChildrenVisiting,
                                   NumberOfPersonVisiting, NumberOfFollowups,MonthlyIncome, 
                                   PreferredPropertyStar, MaritalStatus_Married,MaritalStatus_Single, 
                                   MaritalStatus_Unmarried, Occupation_Large_Business,Occupation_Salaried,
                                   Occupation_Small_Business]])
        
    st.success(result)
    
    
if __name__ == '__main__':
    main()
    
        
