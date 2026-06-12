import streamlit as st
import pandas as pd
import numpy as np
# title of the application
st.title("hello streamlit")
#display a simple text
st.write("this is a simple text")
## create  the dataframe
df =pd.DataFrame({
    'first col':[1,2,3,4,5],
    'second col':[10,20,30,40,50]
})
#display the dataframe
st.write("here is the dataframe")
st.write(df)
#create the liine chart
chart_data=pd.DataFrame(
    np.random.randn(20,3),columns=['a','b','c']
)
st.line_chart(chart_data)