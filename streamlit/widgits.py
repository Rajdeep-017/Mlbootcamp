import streamlit as st
import pandas as pd
st.title("streamlit text input")

name=st.text_input("enter your name")


age=st.slider("select your age",0,100,25)

st.write(f"your age{age}")

opt=["py",'java','cpp','rust']
choice=st.selectbox("choose your lang",opt)
st.write(f"your selected {choice}")


if name:
    st.write(f"{name} , hello")

data={
    "name":["jj","hh","yy"],
    "age":[23,44,55],
    "city":["nyc",'ls','del']
}
df=pd.DataFrame(data)
st.write(df)
uploaed_file=st.file_uploader("choose a csv",type='csv')

if uploaed_file is not None:
    df=pd.read_csv(uploaed_file)
    st.write(df)
