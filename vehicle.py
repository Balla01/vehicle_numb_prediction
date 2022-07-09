# -*- coding: utf-8 -*-
"""
Created on Sat Jul  9 22:25:27 2022

@author: rakesh
"""
import streamlit as st #web app and camera
import numpy as np # for image processing 
from PIL import Image #Image processing 
import cv2 #computer vision 


# pip install requests
import requests
import matplotlib.pyplot as plt
from pprint import pprint
import json
def extract(paths):
    regions = ['in'] # Change to your country
    with open(paths, 'rb') as fp:
        response = requests.post(
        'https://api.platerecognizer.com/v1/plate-reader/',
        data=dict(regions=regions),  # Optional
        files=dict(upload=fp),
        headers={'Authorization': 'Token 29766c1f8d7ae8e9eb60fdd6aee2d549e8588d8e'})
    res=response.json()    
#pprint(response.json())


# Calling with a custom engine configuration

    with open(paths, 'rb') as fp:
        response = requests.post(
        'https://api.platerecognizer.com/v1/plate-reader/',
        data=dict(regions=['in'], config=json.dumps(dict(region="strict"))),  # Optional
        files=dict(upload=fp),
        headers={'Authorization': 'Token 29766c1f8d7ae8e9eb60fdd6aee2d549e8588d8e'})
    lis=[]
    for results in res:
        lis.append(res[results])   
    return lis[1][0]["plate"]

st.title("VECHILE DETAILS DETECTOR")

# collect the user input 

#file_image = st.sidebar.file_uploader("Upload your Photos", type=['jpeg','jpg','png'])
#st.write(file_image)

# collecting the input image from user camera 

vin=st.text_input("enter the img path")

if vin:
    st.write(extract(vin))
    img = plt.imread(vin)
    input_img = Image.open(vin)
    #abc=extract(file_image)
    one, two = st.columns(2)
    with one:
        st.write("**Input vehicle Photo**")
        st.image(input_img, use_column_width=True)
    with two:
        
        st.write("**vehicle details**")
        st.write(extract(vin))
        #st.image(final_sketch, use_column_width=True)

else:
     st.write("You haven't uploaded any image file")
   

#st.write("Courtesy: 1littlecoder Youtube Channel - [Sketch Code](https://github.com/amrrs/youtube-r-snippets/blob/master/Create_a_Pencil_Sketch_Portrait_with_Python_OpenCV.ipynb)")

st.markdown("![](https://mms.businesswire.com/media/20200616005364/en/798639/23/Streamlit_Logo_%281%29.jpg=200x200)")