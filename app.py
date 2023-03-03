import streamlit as st
from datetime import datetime
import requests
import pandas as pd
'''
# Taxi Fare Calculation
'''

#st.markdown('''
#Remember that there are several ways to output content into your web page...

#Either as with the title by just creating a string (or an f-string). Or as with this paragraph using the `st.` functions
#''')
#'''

#'''

date = str(st.date_input("Date"))
time = str(st.time_input('time'))
datetime = date + ' ' + time
pickup_longitude = st.number_input('Pickup longitude')
pickup_latitude = st.number_input('Pickup latitude')
dropoff_longitude = st.number_input('Dropoff longitude')
dropoff_latitude = st.number_input('Dropoff latitude')
passenger_count = st.selectbox('Passenger count', [1, 2, 3, 4, 5, 6, 7])

#Transformation des adresses en coordonnées
#url_geo =

url = 'https://taxifare.lewagon.ai/predict'

#2. Let's build a dictionary containing the parameters for our API...
parameters = {
    "pickup_datetime": datetime,
    "pickup_longitude": pickup_longitude,
    "pickup_latitude": pickup_latitude,
    "dropoff_longitude": dropoff_longitude,
    "dropoff_latitude": dropoff_latitude,
    "passenger_count": passenger_count
}

#st.write(parameters)
#3. Let's call our API using the `requests` package...

if st.button('Calculate fare'):
    # print is visible in the server output, not in the page
    r = requests.get(url, params=parameters).json()
    fare = r['fare']
    st.write(fare)

    #map
    coordinates = {
        "lat": [pickup_latitude, dropoff_latitude],
        "lon": [pickup_longitude, dropoff_longitude]
    }
    coordinates_df = pd.DataFrame(coordinates)
    st.map(coordinates_df)

#4. Let's retrieve the prediction from the **JSON** returned by the API...

## Finally, we can display the prediction to the user
