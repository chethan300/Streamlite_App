import streamlit
import pandas
import requests
streamlit.title("My Parents Healthier Dinner")
streamlit.header("Breakfast Menu")
streamlit.text("Mutton Pulav")
streamlit.text("Chicken Kabab")
streamlit.text("Chicken Tandori")
streamlit.header("Build Your Own Fruits Smoothie")

my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list= my_fruit_list.set_index('Fruit')
#lets put a picklist so that they can pick the fruit they want to include
fruits_selected=streamlit.multiselect("pick some fruits :", list(my_fruit_list.index), ['Avocado','Strawberries'])
fruits_to_show=my_fruit_list.loc[fruits_selected]
streamlit.dataframe(fruits_to_show)

## New section to add fruit vice

fruityvice_response = requests.get("https://fruityvice.com/api/fruit/watermelon")
##streamlit.text(fruityvice_response.json())

#Normailze the JSOn
fruityvice_normalized =pandas.json_normalize(fruityvice_response.json())

streamlit.dataframe(fruityvice_normalized)
