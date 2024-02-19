#%%writefile app.py
# Streamlit is an open-source app framework for Machine Learning and Data Science projects.
import streamlit as st

# Pandas is a fast, powerful, flexible, and easy-to-use open-source data analysis and data manipulation Python library.
import pandas as pd

# NumPy is a library for the Python programming language, adding support for large, multi-dimensional arrays and matrices, along with a large collection of high-level mathematical functions.
import numpy as np

# Matplotlib is a plotting library for the Python programming language and its numerical mathematics extension NumPy.
import matplotlib.pyplot as plt

# Seaborn is a Python data visualization library based on Matplotlib. It provides a high-level interface for drawing attractive and informative statistical graphics.
import seaborn as sns

# Plotly Express is a terse, consistent, high-level API for creating figures with Plotly.py.
import plotly.express as px

# (Note: Streamlit is imported twice in the provided code, which is redundant.)
import streamlit as st

# Python's built-in library for generating random numbers.
import random

# PIL (Python Imaging Library) is a free library for the Python programming language that adds support for opening, manipulating, and saving many different image file formats.
from PIL import Image


# Load the Chocolate image >>>>>>>>>>>>
choco_img = Image.open('chocolate_img.jpeg')
# Display the NYU logo on the Streamlit app
st.image(choco_img, width=100)

# Set the title for the Streamlit app >>>>>>>>>>>>
st.title("Chocolate Data Visualization")

# Create a sidebar header and a separator
st.sidebar.header("Dashboard")
st.sidebar.markdown("---")

df = pd.read_csv("chocolate.csv")
#df = pd.read_csv("df_spotify_final.csv")


## Description of Dataset

num = st.number_input('No of Rows',5,10)
st.dataframe(df.head(num))

### Description of the dataset

st.dataframe(df.describe())

#if st.button("Show Describe Code"):
      #  code = '''df.describe()'''
       # st.code(code, language='python')


list_variables = df.columns

# Display a header for the Visualization section
st.markdown("## Visualization")
symbols = st.multiselect("Select two variables", list_variables, ["review_date", "cocoa_percent"])

#df["cocoa_percent"] = df["cocoa_percent"].astype(str).str.replace("%", "")
review_date_min, review_date_max = st.sidebar.slider('Select Date Range', min_value=int(df['review_date'].min()), max_value=int(df['review_date'].max()), value=(int(df['review_date'].min()), int(df['review_date'].max())))
rating_min, rating_max = st.sidebar.slider('Select Coco Percent Range', min_value=float(df['rating'].min()), max_value=float(df['rating'].max()), value=(float(df['rating'].min()), float(df['rating'].max())))

# Filtering the dataframe based on the slider values
filtered_df = df[(df['review_date'] >= review_date_min) & (df['review_date'] <= review_date_max) & (df['rating'] >= rating_min) & (df['rating'] <= rating_max)]


tab1, tab2 = st.tabs(["Line Chart", "Bar Chart"])

tab1.subheader("Line Chart")
# Display a line chart for the selected variables
tab1.line_chart(data=filtered_df, x=symbols[0], y=symbols[1], width=0, height=0, use_container_width=True)

tab2.subheader("Bar Chart")
# Display a bar chart for the selected variables
tab2.bar_chart(data=filtered_df, x=symbols[0], y=symbols[1], use_container_width=True)


if st.button("Generate Report"):
  import streamlit as st
  import streamlit.components.v1 as components

  # Title for your app
  st.title('Sweetviz Report in Streamlit')

  # Display the Sweetviz report
  report_path = 'report.html'
  HtmlFile = open(report_path, 'r', encoding='utf-8')
  source_code = HtmlFile.read()
  components.html(source_code, height=1000,width=1000)



