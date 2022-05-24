import streamlit
import pandas
import requests
import snowflake.connector
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
streamlit.header("FruityVice Fruit Advisory")
fruit_choice =streamlit.text_input("What fruit would you like information about ?",'kiwi')
streamlit.write("the user entered ",fruit_choice )
fruityvice_response = requests.get("https://fruityvice.com/api/fruit/"+fruit_choice)
##streamlit.text(fruityvice_response.json())

#Normailze the JSOn
fruityvice_normalized =pandas.json_normalize(fruityvice_response.json())

streamlit.dataframe(fruityvice_normalized)


my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_cur = my_cnx.cursor()
my_cur.execute("SELECT CURRENT_USER(), CURRENT_ACCOUNT(), CURRENT_REGION()")
my_data_row = my_cur.fetchone()
streamlit.text("Hello from Snowflake:")
streamlit.text(my_data_row)
