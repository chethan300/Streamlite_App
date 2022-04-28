import streamlit
import pandas
streamlit.title("My Parents Healthier Dinner")
streamlit.header("Breakfast Menu")
streamlit.text("Mutton Pulav")
streamlit.text("Chicken Kabab")
streamlit.text("Chicken Tandori")
streamlit.header("Build Your Own Fruits Smoothie")

my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")



streamlit.dataframe(my_fruit_list)
