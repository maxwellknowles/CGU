## Imports
import urllib 
import pandas as pd
from datetime import datetime, timedelta, date
import streamlit as st

import pyspark
import matplotlib.pyplot as plt

import numpy as np
import os
from geopy.geocoders import Nominatim
geolocator = Nominatim(user_agent="sample app")
import geopy.distance
import pydeck as pdk

st.title('Title')

###setdate
##year, month, day = date.today().year, date.today().month, date.today().day
##end = datetime(year, month, day)
##start = datetime(year, month, day) - timedelta(days=2)

st.text("Hi there!")


state_requirements = pd.read_csv("https://raw.githubusercontent.com/2Maximus7/CGU/main/Homeschool%20Project%20MVP%20-%20State%20High%20School%20Grad%20Requirements.csv")
st.dataframe(state_requirements)
#latlong_data = pd.read_csv("https://raw.githubusercontent.com/maxwell4zero/zerogrocery/master/CA%20Farms%20-%20Mock%20Farm%20Lat%20Lon.csv")
##latlong = []
##for i in vendor_zips.iterrows():
##    vendor = i[1]['vendor']
##    zipcode = i[1]['zipcode']
##    address = geolocator.geocode(i[1]['zipcode'])
##    lat = address.point.latitude
##    lon = address.point.longitude
##    coords = (lat, lon)
##    tup = (vendor, address, zipcode, lat, lon, coords)
##    latlong.append(tup)
##    latlong_data = pd.DataFrame(latlong, columns = ['vendor', 'address', 'zipcode', 'lat', 'lon', 'coords'])
##    st.dataframe(latlong_data)
##    st.map(latlong_data, zoom=None, use_container_width=True)
