#!/usr/bin/env python
# coding: utf-8

# # Daily Deviations

# ## ArtWork Updated Daily ##

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
import ipywidgets as widgets
from IPython.display import display


# In[2]:


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
        image = widgets.Image(value=response.raw.read(),format="png",width=400,height=400)
        
        text = widgets.Label(
            value = str(counter),
        )
        items = widgets.HBox([image,text])
        #plt.imshow(img)
        #plt.show()
        dalist += [items]
        counter += 1
widgets.GridBox(dalist, layout=widgets.Layout(grid_template_columns="repeat(2, 500px)"))


# In[3]:


radio = widgets.RadioButtons(
            options = [x for x in range(1,13)],
            description="Your AR Pick:",
            disabled = False
        )
radio

