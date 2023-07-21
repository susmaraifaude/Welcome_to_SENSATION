#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import requests

def get_location():
    try:
        response = requests.get('https://ipapi.co/json/')
        data = response.json()
        city = data['city']
        region = data['region']
        country = data['country_name']

        if 'location' in data and 'street' in data['location']:
            street = data['location']['street']
            return f"You are currently in {street}, {city}, {region}, {country}"
        else:
            return f"You are currently in {city}, {region}, {country}"
    except requests.exceptions.RequestException:
        return "Sorry, I couldn't retrieve the location."

