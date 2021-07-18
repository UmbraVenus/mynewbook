#!/usr/bin/env python
# coding: utf-8

# # Daily Deviations

# ## ArtWork Updated Daily ##

# In[1]:


pip install ipywidgets


# In[2]:


pip install requests


# In[3]:


pip install pillow


# In[4]:


pip install deviantart


# In[5]:


pip install opencv-contrib-python


# In[6]:


pip install imutils


# In[7]:


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
import ipywidgets as widgets
from IPython.display import display
from ipywidgets import interact, interact_manual


# In[8]:


da = deviantart.Api("16260","66397f4afec59514bdf212884f4e0d74")
dailydeviations = da.browse_dailydeviations()

dalist = []
counter = 1
for deviation in dailydeviations:
    #print(da.get_deviation_metadata(deviation.deviationid)[0]["description"])
    #print(deviation.content)
    
    jr = deviation.content
    #for key, value in jr.items():
      #  print(key, ":", value)
    if jr:
        #print(jr["src"])

        response = requests.get(jr["src"],stream=True)
        #img = Image.open(response.raw)
        image = widgets.Image(value=response.raw.read(),format="png",width=300,height=300)
        
        text = widgets.Label(
            value = str(counter),
        )
        items = widgets.HBox([image,text])
        #plt.imshow(img)
        #plt.show()
        dalist += [items]
        counter += 1
widgets.GridBox(dalist, layout=widgets.Layout(grid_template_columns="repeat(2, 320px)"))


# ## More Recommendations ##

# In[9]:


radio = widgets.RadioButtons(
            options = [x for x in range(1,13)],
            description="Your AR Pick:",
            disabled = False
        )
radio


# In[10]:


morefav = da.browse_morelikethis_preview(dailydeviations[radio.value])['more_from_artist']
recommendation = []
for x in morefav:
    r = x.content
    #for key, value in jr.items():
      #  print(key, ":", value)
    if r:
        #print(jr["src"])

        response = requests.get(r["src"],stream=True)
        #img = Image.open(response.raw)
        image = widgets.Image(value=response.raw.read(),format="png",width=300,height= 300)
        #plt.imshow(img)
        #plt.show()
        recommendation += [image]
widgets.GridBox(recommendation, layout=widgets.Layout(grid_template_columns="repeat(2, 300px)"))

