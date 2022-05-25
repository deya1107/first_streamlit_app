import streamlit
import pandas as pd

my_fruit_list = pd.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")

streamlit.title("My Parents new healthy diner")
streamlit.header("Breakfast Menu")
streamlit.text("🥣 Omega 3 & Blueberry Oatmeal")
streamlit.text("🥗 Kale, Spinach & Rocket Smoothie")
streamlit.text("🐔 Hard Boiled Free-Range Egg")
streamlit.text("🥑🍞 Avocado Toast")

streamlit.header("🍌🥭 Build your own smoothie 🥝🍇")
my_fruit_list = my_fruit_list.set_index("Fruit")

#Pick up fruits from the list 
fruit_selected = streamlit.multiselect("Pick up some fruits:", list(my_fruit_list.index), ["Avocado","Strawberries"])
fruit_show = my_fruit_list.loc[fruit_selected]

#Display the fruit list on the page
streamlit.dataframe(fruit_show)

