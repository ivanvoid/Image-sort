#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 15 18:15:43 2020

@author: veax
"""

import matplotlib.pyplot as plt
import matplotlib.image as mpimg

def sort_img(img):
    print("Compute sort keys")
    sorted_img = {} 
    
    for i in range(img.shape[0]):
        for j in range(img.shape[1]):
            sorted_img[str(i)+'.'+str(j)] = [sum(img[i,j])]
            
    sorted_keys = sorted(sorted_img, key=sorted_img.get)
    
    print("Coping sorted img")
    sorted_img = np.zeros(img.shape)
    i = 0
    j = 0
    
    for coords in sorted_keys:
        x, y = coords.split('.')
        x = int(x)
        y = int(y)
        
        sorted_img[i, j] = img[x, y]
        
        j += 1
        if j >= img.shape[1]:
            j = 0
            i += 1
    
    return sorted_img

img_path = 'img.png'
img = mpimg.imread(img_path)

# imgplot = plt.imshow(img[:100, :100, 0], clim=(0.8,0.1))
# plt.colorbar()

plt.imshow(img)
# plt.colorbar()


a = sort_img(img)

a_img = a[:,:,0]
plt.figure()
plt.imshow(a)
# plt.colorbar()

plt.figure()
plt.hist(a_img.ravel(), bins=256, range=(0.0, 1.0), fc='k', ec='k')










