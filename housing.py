import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st
plt.style.use('seaborn')


st.title('California Housing Data (1990) by Wentian Lv')
housing = pd.read_csv('housing.csv')

h_slider = st.slider('Median House Price', 0.0, 500000.0, 200000.0)
housing = housing[housing.median_house_value >= h_slider]
st.subheader('See more filters in the sidebar')

h_filter = st.sidebar.multiselect(
    'Choose the location type:',
    housing.ocean_proximity.unique(),
    housing.ocean_proximity.unique()
)
housing = housing[housing.ocean_proximity.isin(h_filter)]

choose = st.sidebar.radio(
    'Choose income level:',
    ('low', 'median', 'high'),
)
if choose == 'low':
    housing = housing[housing.median_income <= 2.5]
elif choose == 'median':
    housing = housing[(housing.median_income > 2.5) & (housing.median_income < 4.5)]
elif choose == 'high':
    housing = housing[housing.median_income >= 4.5]

st.map(housing)

st.subheader('Histogram of the Median House Value')
fig, ax = plt.subplots()
ax.set_title('Median house value')
housing.median_house_value.plot.hist(bins=30)
st.pyplot(fig)

st.write(housing)