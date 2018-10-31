#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 19 01:39:01 2017

@author: erdembocugoz
"""

from PIL import Image
im = Image.open('photo.jpg')
im.save('photo.png')