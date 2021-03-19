# -*- coding: utf-8 -*-
"""
Created on Fri Mar 19 14:07:06 2021

@author: deepak
"""

import streamlit as st 
from PIL import Image
import pickle
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
st.set_option('deprecation.showfileUploaderEncoding', False)
# Load the pickled model
model = pickle.load(open('kmeansclusterassignment.pkl','rb'))   
dataset= pd.read_csv('Wholesale customers data.csv')
X = dataset.iloc[:,2:8].values
from sklearn.preprocessing import StandardScaler
sc = StandardScaler()
X = sc.fit_transform(X)
def predict_note_authentication(chanel,region,fresh,milk,grocery,frozen,detergents,delicassen):
  predict= model.predict(sc.transform([[fresh,milk,grocery,frozen,detergents,delicassen]]))
  print("cluster number", predict)
  if predict==[0]:
    result="Customer is careless"

  elif predict==[1]:
    result="Customer is standard"
  elif predict==[2]:
    result="Customer is Target"
  elif predict==[3]:
    result="Customer is careful"

  else:
    result="Custmor is sensible"
  
  return result
def main():

    
    html_temp = """
   <div class="" style="background-color:blue;" >
   <div class="clearfix">           
   <div class="col-md-12">
   <center><p style="font-size:40px;color:white;margin-top:10px;">Poornima Institute of Engineering & Technology</p></center> 
   <center><p style="font-size:30px;color:white;margin-top:10px;">Department of Computer Engineering</p></center> 
   <center><p style="font-size:25px;color:white;margin-top:10px;"Machine Learning Lab Experiment</p></center> 
   </div>
   </div>
   </div>
   """
    st.markdown(html_temp,unsafe_allow_html=True)
    st.header("Customer Segmenation on wholesale data ")
    
    chanel = st.selectbox(
    "Chanel",
    ("1", "2")
    )
    region = st.selectbox(
    "Region",
    ("1", "2","3")
    )
    fresh = st.number_input('Insert a amount spent on Fresh items',3,100000)
    milk = st.number_input("Insert  amount spent on milk products",55,100000)
    grocery = st.number_input("Insert  amount spent on grocery",3,100000)
    frozen = st.number_input("Insert  amount spent on frozen items",25,100000)
    detergents = st.number_input("Insert  amount on  detergents",3,100000)
    delicassen = st.number_input("Insert  amount spent on deliseen",3,100000)
    resul=""
    if st.button("Predict"):
      result=predict_note_authentication(chanel,region,fresh,milk,grocery,frozen,detergents,delicassen)
      st.success('Model has predicted {}'.format(result))
      
    if st.button("About"):
      st.subheader("Developed by Deepak Moud")
      st.subheader("Head , Department of Computer Engineering")
    html_temp = """
   <div class="" style="background-color:orange;" >
   <div class="clearfix">           
   <div class="col-md-12">
   <center><p style="font-size:20px;color:white;margin-top:10px;">Machine learning Experiment No. 8</p></center> 
   </div>
   </div>
   </div>
   """
    st.markdown(html_temp,unsafe_allow_html=True)
if __name__=='__main__':
  main()