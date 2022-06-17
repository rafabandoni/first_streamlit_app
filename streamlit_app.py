import streamlit

streamlit.title('My Parents New Healthy Dinner')

streamlit.header('Breakfast Favourites')
streamlit.text('🍜 Omega 3 & Blueberry Oatmeal')
streamlit.text('🥗 Kale, Spinach & Rocket Smoothie')
streamlit.text('🐔 Hard-Boiled Free-Range Egg')
streamlit.text('🥑🍞 Avocado Toast')

streamlit.header('🍌🍓 Build Your Own Fruit Smoothie 🥝🍇')

import pandas as pd

my_fruit_list = pd.read_csv('https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt')
my_fruit_list = my_fruit_list.set_index('Fruit')

# Adding a pick list
streamlit.multiselect('Pick some fruits:', list(my_fruit_list.index))

# Display table
streamlit.dataframe(my_fruit_list)