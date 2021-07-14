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
from ipywidgets import interact, interact_manual


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

# ### 1st artist ###

# In[3]:


morefav = da.browse_morelikethis_preview(dailydeviations[0])['more_from_artist']
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


# ### 2nd artist ###

# In[4]:


morefav = da.browse_morelikethis_preview(dailydeviations[1])['more_from_artist']
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


# ### 3rd artist ###

# In[5]:


morefav = da.browse_morelikethis_preview(dailydeviations[2])['more_from_artist']
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


# ### 4th artist ###

# In[6]:


morefav = da.browse_morelikethis_preview(dailydeviations[3])['more_from_artist']
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


# ### 5th artist ###

# In[7]:


morefav = da.browse_morelikethis_preview(dailydeviations[4])['more_from_artist']
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


# ### 6th artist ###

# In[8]:


morefav = da.browse_morelikethis_preview(dailydeviations[5])['more_from_artist']
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


# ### 7th artist ###

# In[9]:


morefav = da.browse_morelikethis_preview(dailydeviations[6])['more_from_artist']
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


# ### 8th artist ###

# In[10]:


morefav = da.browse_morelikethis_preview(dailydeviations[7])['more_from_artist']
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


# ### 9th artist ###

# In[11]:


morefav = da.browse_morelikethis_preview(dailydeviations[8])['more_from_artist']
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


# ### 10th artist ###

# In[12]:


morefav = da.browse_morelikethis_preview(dailydeviations[9])['more_from_artist']
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


# ### 11th artist ###

# In[ ]:


morefav = da.browse_morelikethis_preview(dailydeviations[10])['more_from_artist']
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


# ### 12th artist ###

# In[ ]:


morefav = da.browse_morelikethis_preview(dailydeviations[11])['more_from_artist']
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

