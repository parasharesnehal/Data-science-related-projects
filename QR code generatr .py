#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Import QRCode from pyqrcode 
import pyqrcode 
import png 
from pyqrcode import QRCode 


# String which represents the QR code 
s = "www.geeksforgeeks.org"

# Generate QR code 
url = pyqrcode.create(s) 

# Create and save the svg file naming "myqr.svg" 
url.svg("myqr.svg", scale = 8) 

# Create and save the png file naming "myqr.png" 
url.png('myqr.png', scale = 6) 


# In[2]:


pip install pyqrcode


# In[3]:


pip install pypng


# In[2]:





# In[ ]:




