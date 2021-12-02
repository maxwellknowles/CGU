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

st.header('High School Credit Requirements by State')
st.sidebar.subheader('State Requirements & Resources')
state = st.sidebar.selectbox('Filter by state',
('All States','Alabama', 'District of Columbia', 'New Mexico', 'Louisiana', 'West Virginia', 'Alaska', 'Arkansas',
 'Mississippi', 'Nevada', 'Hawaii', 'California', 'Oklahoma', 'Rhode Island', 'South Carolina', 'Delaware',
 'Kentucky', 'Florida', 'Georgia', 'Arizona', 'Maryland', 'Michigan', 'New York', 'Oregon', 'Tennessee',
 'Texas', 'Missouri', 'Iowa', 'Kansas', 'Maine', 'Illinois', 'Montana', 'North Carolina', 'Colorado',
 'Nebraska', 'Pennsylvania', 'Utah','Connecticut', 'Idaho', 'Indiana', 'North Dakota', 'Ohio', 'Washington',
 'Wyoming', 'New Hampshire', 'South Dakota', 'Vermont', 'Virginia', 'Wisconsin', 'Minnesota', 'New Jersey', 'Massachusetts'))

st.write('You are looking at credit requirements for:', state)

if state == 'All States':
    state_requirements_state = state_requirements
    st.dataframe(state_requirements_state)
else:
    state_requirements_state = state_requirements.loc[(state_requirements['State']==state)]
    st.dataframe(state_requirements_state)

@st.cache
def convert_df(df):
    # IMPORTANT: Cache the conversion to prevent computation on every rerun
    return df.to_csv().encode('utf-8')

csv = convert_df(state_requirements_state)

st.download_button(
    label="Download your state's credit requirements as a CSV",
    data=csv,
    file_name='high_school_credit_requirements.csv',
    mime='text/csv',)



st.header('Homeschool Requirements by State')
st.write('You are looking at the specific homeschool requirements for:', state)
homeschool_requirements = pd.read_csv("https://raw.githubusercontent.com/2Maximus7/CGU/main/Homeschool%20Project%20MVP%20-%20Homeschool%20Requirements.csv")
if state == 'All States':
    homeschool_requirements2 = homeschool_requirements
    st.dataframe(homeschool_requirements2)
else:
    homeschool_requirements2 = homeschool_requirements.loc[(homeschool_requirements['State']==state)]
    st.dataframe(homeschool_requirements2)

st.caption('† Not applicable.')
st.caption('1 Colorado state law requires satisfactory completion of a Civics/Government course that encompasses information on both the United States and State of Colorado.')
st.caption('2 LD = Graduation course requirements are locally determined. Thus, the units required by subject and total number of units are not comparable to other states.')
st.caption('3 Idaho, Indiana, Nebraska, and New Jersey define units of credit differently than most states. For the purposes of comparison, the number of units required by subject and the total number of units has been adjusted to align better with how the majority of states define units of credit (i.e., Carnegie units where one unit equates to a year of instruction).')
st.caption('NOTE: The data included in this table reflect the requirements of the default degree option for each state and the District of Columbia. States define diplomas and graduation requirements differently and may offer one diploma, multiple diplomas, multiple courses of study leading to one diploma, or endorsements students may earn in addition to a standard diploma. Total includes required course work in other disciplines not separately shown.')
st.caption('SOURCE: Achieve, Graduating Ready Data Explorer, retrieved December 31, 2018 from https://highschool.achieve.org/data-explorer. Data Source.')

@st.cache
def convert_df(df):
    # IMPORTANT: Cache the conversion to prevent computation on every rerun
    return df.to_csv().encode('utf-8')

csv = convert_df(homeschool_requirements2)

st.download_button(
    label="Download your state's homeschool guidelines as a CSV",
    data=csv,
    file_name='state_homeschool_guidelines.csv',
    mime='text/csv',)


st.sidebar.subheader('Curricular Choices')
st.header('Curricular Options')
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
grade = st.sidebar.selectbox('Filter by grade',('All',9, 10, 11, 12))
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

@st.cache
def convert_df(df):
    # IMPORTANT: Cache the conversion to prevent computation on every rerun
    return df.to_csv().encode('utf-8')

csv = convert_df(mock_curricula4)

st.download_button(
    label="Download your curricular options as CSV",
    data=csv,
    file_name='curated_curricular_options.csv',
    mime='text/csv',)

st.sidebar.subheader('Are you an educator? Join our network')
teacher_name = st.sidebar.text_input('Name')
teacher_email = st.sidebar.text_input('Email')
teacher_zipcode = st.sidebar.text_input('Zipcode')
teacher_format = st.sidebar.checkbox('Willing to work digitally?')
uploaded_file = st.sidebar.file_uploader("Upload your CV or resume below please")


st.header('Catalyst Co-Ops, Teachers, and Mentors')
Co_Ops_Educators = pd.read_csv("https://raw.githubusercontent.com/2Maximus7/CGU/main/Homeschool%20Project%20MVP%20-%20Co-Ops%20%26%20Educators.csv")
if state == 'All States':
    Co_Ops_Educators2 = Co_Ops_Educators
    st.dataframe(Co_Ops_Educators)
else:
    Co_Ops_Educators2 = Co_Ops_Educators.loc[(Co_Ops_Educators['State']==state)]
    st.dataframe(Co_Ops_Educators2)
@st.cache
def convert_df(df):
    # IMPORTANT: Cache the conversion to prevent computation on every rerun
    return df.to_csv().encode('utf-8')

csv = convert_df(Co_Ops_Educators2)

st.download_button(
    label="Download these local resources as CSV",
    data=csv,
    file_name='local_resources.csv',
    mime='text/csv',)


st.header('Example Schedules')
st.subheader('Example Four Year Schedule')
four_year = pd.read_csv("https://raw.githubusercontent.com/2Maximus7/CGU/main/Homeschool%20Project%20MVP%20-%204-Year%20Schedule.csv")
four_year
    
@st.cache
def convert_df(df):
    # IMPORTANT: Cache the conversion to prevent computation on every rerun
    return df.to_csv().encode('utf-8')

csv = convert_df(four_year)

st.download_button(
    label="Download as a template CSV",
    data=csv,
    file_name='4year_schedule.csv',
    mime='text/csv',)


st.subheader('Example Semester')
semester = pd.read_csv("https://raw.githubusercontent.com/2Maximus7/CGU/main/Homeschool%20Project%20MVP%20-%20Semester%20Schedule.csv")
semester
   
@st.cache
def convert_df(df):
    # IMPORTANT: Cache the conversion to prevent computation on every rerun
    return df.to_csv().encode('utf-8')

csv = convert_df(semester)

st.download_button(
    label="Download as a template CSV",
    data=csv,
    file_name='semester_schedule.csv',
    mime='text/csv',)


st.subheader('Example Week')
week = pd.read_csv("https://raw.githubusercontent.com/2Maximus7/CGU/main/Homeschool%20Project%20MVP%20-%20Week%20Schedule.csv")
week
   
@st.cache
def convert_df(df):
    # IMPORTANT: Cache the conversion to prevent computation on every rerun
    return df.to_csv().encode('utf-8')

csv = convert_df(week)

st.download_button(
    label="Download as a template CSV",
    data=csv,
    file_name='weekly_schedule.csv',
    mime='text/csv',)


st.subheader('Resources on Finding Groups')
st.text('https://www.thehomeschoolmom.com/local-support/')
st.text('https://my.hslda.org/groups/s/')
st.text('https://www.homeschool.com/supportgroups/')

st.subheader('Sources')
st.text('https://www.homeschool.com/articles/state-homeschooling-laws/')
st.text('https://nces.ed.gov/programs/statereform/tab2_13.asp')

