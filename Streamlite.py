import streamlit
import pandas
streamlit.title("My Parents Healthier Dinner")
streamlit.header("Breakfast Menu")
streamlit.text("Mutton Pulav")
streamlit.text("Chicken Kabab")
streamlit.text("Chicken Tandori")
streamlit.header("Build Your Own Fruits Smoothie")

my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")

#lets put a picklist so that they can pick the fruit they want to include
streamlit.mulitselect("pick some fruits :", list(my_fruit_list.idex))

streamlit.dataframe(my_fruit_list)
