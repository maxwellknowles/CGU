## Imports
#import dns
import urllib 
import pandas as pd
##from datetime import datetime, timedelta, date
import streamlit as st

#import pyspark
#import matplotlib.pyplot as plt

##import numpy as np
##import os
##from geopy.geocoders import Nominatim
##geolocator = Nominatim(user_agent="sample app")
##import geopy.distance
##import pydeck as pdk

primaryColor="#F63366"
backgroundColor="#F0F2F6"
secondaryBackgroundColor="#FFFFFF"
textColor="#262730"
font="sans serif"

st.title('Catalyst')
st.header('Early Prototype')
st.sidebar.header('Filter on what matters most to you and your family...')

state_requirements = pd.read_csv("https://raw.githubusercontent.com/2Maximus7/CGU/main/Homeschool%20Project%20MVP%20-%20State%20High%20School%20Grad%20Requirements.csv")

###setdate
##year, month, day = date.today().year, date.today().month, date.today().day
##end = datetime(year, month, day)
##start = datetime(year, month, day) - timedelta(days=2)


st.text("Hi there!")

##with st.form("my_form"):
##    st.write("Inside the form")
##    state = st.selectbox('Filter by state',
##('All States','Alabama', 'District of Columbia', 'New Mexico', 'Louisiana', 'West Virginia', 'Alaska', 'Arkansas',
## 'Mississippi', 'Nevada', 'Hawaii', 'California', 'Oklahoma', 'Rhode Island', 'South Carolina', 'Delaware',
## 'Kentucky', 'Florida', 'Georgia', 'Arizona', 'Maryland', 'Michigan', 'New York', 'Oregon', 'Tennessee',
## 'Texas', 'Missouri', 'Iowa', 'Kansas', 'Maine', 'Illinois', 'Montana', 'North Carolina', 'Colorado',
## 'Nebraska', 'Pennsylvania', 'Utah','Connecticut', 'Idaho', 'Indiana', 'North Dakota', 'Ohio', 'Washington',
## 'Wyoming', 'New Hampshire', 'South Dakota', 'Vermont', 'Virginia', 'Wisconsin', 'Minnesota', 'New Jersey', 'Massachusetts'))
##    checkbox_val = st.checkbox("Form checkbox")
##
##    # Every form must have a submit button.
##    submitted = st.form_submit_button("Submit")
##    if submitted:
##        st.write("selectbox", state, "checkbox", checkbox_val)
##
##st.write("Outside the form")

st.subheader('High School Credit Requirements by State')
st.sidebar.subheader('State Requirements')
state = st.sidebar.selectbox('Filter by state',
('All States','Alabama', 'District of Columbia', 'New Mexico', 'Louisiana', 'West Virginia', 'Alaska', 'Arkansas',
 'Mississippi', 'Nevada', 'Hawaii', 'California', 'Oklahoma', 'Rhode Island', 'South Carolina', 'Delaware',
 'Kentucky', 'Florida', 'Georgia', 'Arizona', 'Maryland', 'Michigan', 'New York', 'Oregon', 'Tennessee',
 'Texas', 'Missouri', 'Iowa', 'Kansas', 'Maine', 'Illinois', 'Montana', 'North Carolina', 'Colorado',
 'Nebraska', 'Pennsylvania', 'Utah','Connecticut', 'Idaho', 'Indiana', 'North Dakota', 'Ohio', 'Washington',
 'Wyoming', 'New Hampshire', 'South Dakota', 'Vermont', 'Virginia', 'Wisconsin', 'Minnesota', 'New Jersey', 'Massachusetts'))

st.write('You are looking at credit requirements for:', state)

if state == 'All States':
    st.dataframe(state_requirements)
else:
    state_requirements_state = state_requirements.loc[(state_requirements['State']==state)]
    st.dataframe(state_requirements_state)

st.subheader('Homeschool Requirements by State')
homeschool_requirements = pd.read_csv("https://raw.githubusercontent.com/2Maximus7/CGU/main/Homeschool%20Project%20MVP%20-%20Homeschool%20Requirements.csv")
if state == 'All States':
    st.dataframe(homeschool_requirements)
else:
    homeschool_requirements.loc[(homeschool_requirements['State']==state)]

st.write('You are looking at the specific homeschool requirements for:', state)

st.sidebar.subheader('Curricular Choices')
st.subheader('Curricular Options')
mock_curricula = pd.read_csv("https://raw.githubusercontent.com/2Maximus7/CGU/main/Homeschool%20Project%20MVP%20-%20Mock%20Curricula%20Data%20(1).csv")
subject = st.sidebar.selectbox('Filter by subject',('All',
 'Math',
 'English',
 'History & Social Studies',
 'Science',
 'Foreign Language',
 'Religion',
 'Computer Science',
 'Math',
 'English',
 'History & Social Studies'))
grade = st.sidebar.selectbox('Filter by grade',('All','9', '10', '11', '12'))
#advanced = st.selectbox('Filter by subject',('All',list(mock_curricula['Advanced'])))
free = st.sidebar.checkbox('Free Resources Only')
online = st.sidebar.checkbox('Online Resources Only')

#subject
if subject == 'All':
    mock_curricula2 = mock_curricula
else:
    mock_curricula2 = mock_curricula.loc[(mock_curricula['Subject']==subject)]

#grade
if grade == 'All':
    mock_curricula3 = mock_curricula2
else:
    mock_curricula3 = mock_curricula2.loc[(mock_curricula2['Grade Levels']==grade)]

#free
if not free:
    mock_curricula4 = mock_curricula3
else:
    mock_curricula4 = mock_curricula3.loc[(mock_curricula3['Cost']=='FREE')]

#online
if not online:
    st.dataframe(mock_curricula4)
else:
    mock_curricula4.loc[(mock_curricula4['Format']=='Digital')]

st.subheader('Find Homeschooling Groups')

st.text('https://www.thehomeschoolmom.com/local-support/')
st.text('https://my.hslda.org/groups/s/')
st.text('https://www.homeschool.com/supportgroups/')

st.subheader('Sources')
st.text('https://www.homeschool.com/articles/state-homeschooling-laws/')
st.text('https://nces.ed.gov/programs/statereform/tab2_13.asp')
