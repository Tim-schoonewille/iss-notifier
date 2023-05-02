import requests
import datetime as dt
from email_sender import EmailSender
import os



MY_LOCATION = {
    "CITY": "Brunssum",
    "LATITUDE": 50.950489,
    "LONGITUDE":  5.970680,
    
}

emails = ['tim.schoonewille@gmail.com', 'tiema.jwz@gmail.com']


# Request the sunrise/sunset times for my location
SUNRISE_SUNSET_URL = 'https://api.sunrise-sunset.org/json'
params = {
    "lat": MY_LOCATION["LATITUDE"],
    "lng": MY_LOCATION["LONGITUDE"]
}
sun_position_response = requests.get(url=SUNRISE_SUNSET_URL,
                                     params=params)
sun_position_response.raise_for_status()
sun_data = sun_position_response.json()['results']


# get sunrise/sunset/current time in DateTime format
date_format = '%I:%M:%S %p'
sunrise = dt.datetime.strptime(sun_data['sunrise'], date_format).time()
sunset = dt.datetime.strptime(sun_data['sunset'], date_format).time()
current_time = dt.datetime.utcnow().time()


def is_dark(sunrise: dt.time, sunset: dt.time, current_time: dt.time):
    if sunset < current_time < sunrise:
        return True
    else:
        return False 

is_the_sun_down = is_dark(sunrise=sunrise, sunset=sunset, current_time=current_time)


# Get ISS location

iss_response = requests.get(url="http://api.open-notify.org/iss-now.json")
iss_response.raise_for_status()
data = iss_response.json()

iss_latitude = float(data["iss_position"]["latitude"])
iss_longitude = float(data["iss_position"]["longitude"])




# my_latitude = MY_LOCATION["LATITUDE"]
# my_longitude = MY_LOCATION["LONGITUDE"]

my_latitude = -20
my_longitude = -13

iss_lat_minimum = iss_latitude - 5
iss_lat_maximum = iss_latitude + 5

iss_long_minimum = iss_longitude - 5
iss_long_maximum = iss_longitude + 5

if is_the_sun_down:
    if iss_lat_minimum < my_latitude < iss_lat_maximum and iss_long_minimum < my_longitude < iss_long_maximum:
        for email in emails:
            
            email = EmailSender(os.environ['SMTP_PASSWORD'], send_to=email, subject='ISS Space Station is in sight!', body='Look up now! The space station is in sight! :)')
            email.send()




