import streamlit
import pandas
streamlit.title("My Parents Healthier Dinner")
streamlit.header("Breakfast Menu")
streamlit.text("Mutton Pulav")
streamlit.text("Chicken Kabab")
streamlit.text("Chicken Tandori")
streamlit.header("Build Your Own Fruits Smoothie")

my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list= my_fruit_list.set_index('Fruit')
#lets put a picklist so that they can pick the fruit they want to include
streamlit.multiselect("pick some fruits :", list(my_fruit_list.index), ['Avocado','Strawberries'])

streamlit.dataframe(my_fruit_list)
