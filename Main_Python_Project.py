import streamlit as st
import pandas

st.set_page_config(layout="wide")


st.title('Adam Idrissi')
content = """
Hello I am Adam Idrissi. I just started learning how to code in Python and I am currently 13 years old.
I will be learning other languages than python so the side bar will keep on updating and 
there will be new projects each week.
"""
st.info(content)

content2 = """
Below you can find some of the apps I have built in Python that will continue to update. 
Feel free to contact me!
"""

st.write(content2)

col1, empty_column, col2 = st.columns([1.5,0.5,1.5])

df = pandas.read_csv(r"C:\Users\adami\PycharmProjects\PythonProject2\data.csv", sep=";")

with col1:
    for index, row in df[:10].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("images/" + row["image"])
        st.write(f'[Source Code]({row["url"]})')


with col2:
    for index, row in df[10:].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("images/" + row["image"])
        st.write(f'[Source Code]({row["url"]})')
