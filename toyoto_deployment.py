import streamlit as st
import pickle
import numpy as np
import pandas as pd

model = pickle.load(open( "model.p", "rb" ))

def inputs(Age,KM,HP,CC,Gears,Quarterly_Tax,Weight):
    Age = float(Age)
    KM = float(KM)
    HP = float(HP)
    CC = float(CC)
    Gears = int(Gears)
    Quarterly_Tax = float(Quarterly_Tax)
    Weight = float(Weight)
    new_data=pd.DataFrame({'Age_08_04':Age,"KM":KM,"HP":HP, "cc":CC, 
                           "Gears":Gears, "Quarterly_Tax":Quarterly_Tax, "Weight":Weight},index=[1])
    final_predict = model.predict(new_data).round(2)
    return(final_predict).values

def main():
    
    st.title('Predicting car prices')
    '''#### Multiple Linear Regression Model'''
    '''Dataset : Toyoto Corolla'''
    '''@ Shrikant Uppin'''
 
    Age = st.sidebar.slider('Age', 44, 70)
    KM = st.sidebar.slider('KM', 43000, 87000)
    HP = st.selectbox('HP',(90,110))
    CC = st.selectbox('CC', (1400, 1600))
    Gears = st.selectbox('Gears',(4,5))
    Quarterly_Tax = st.sidebar.slider('Quarterly_Tax',68,85)
    Weight = st.sidebar.slider('Weight',1040,1085)
    
    if st.button('Predict'):
        output = inputs(Age,KM,HP,CC,Gears,Quarterly_Tax,Weight)
        st.success('the predicted car price is {} INR'.format(output))
    
if __name__=='__main__':
        main()