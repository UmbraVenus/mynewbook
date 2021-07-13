#!/usr/bin/env python
# coding: utf-8

# In[1]:


import requests
import json
from PIL import Image
from io import BytesIO
import matplotlib.pyplot as plt
import deviantart
import numpy as np
import argparse
import imutils
import sys
import cv2


# In[2]:



da = deviantart.Api("16260","66397f4afec59514bdf212884f4e0d74")
dailydeviations = da.browse_dailydeviations()
for deviation in dailydeviations:
#print(da.get_deviation_metadata(deviation.deviationid)[0]["description"])
#print(deviation.content)
    
    jr = deviation.content
#for key, value in jr.items():
    #  print(key, ":", value)
    if jr:
        print(jr["src"])

        response = requests.get(jr["src"],stream=True)
        img = Image.open(response.raw)

        plt.imshow(img)
        plt.show()


# In[3]:


resp = requests.get("https://backend.deviantart.com/oembed?url=http%3A%2F%2Ffav.me%2Fd2enxz7")
if resp.status_code != 200:
    raise ApiErrpr('Get /tasks/ {}'.format(resp.status_code))
jr = resp.json()
for key, value in jr.items():
    print(key, ":", value)
print(jr["url"])

response = requests.get(jr["url"],stream=True)
img = Image.open(response.raw)

plt.imshow(img)
plt.show()

