#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 15 18:15:43 2020

@author: veax-void
"""
# libs
from matplotlib.image import imread, imsave
from matplotlib.gridspec import GridSpec
import matplotlib.pyplot as plt
import numpy as np

# Functions
def sort_img(img):
    print("Compute sort keys...")
    sorted_img = {} 
    
    for i in range(img.shape[0]):
        for j in range(img.shape[1]):
            sorted_img[str(i)+'.'+str(j)] = [sum(img[i,j])]
            
    sorted_keys = sorted(sorted_img, key=sorted_img.get)
    
    print("Coping sorted img...")
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

def plot_info(img, sorted_img):
    print('Plotting extra info...')
    fig = plt.figure(constrained_layout=True)

    gs = GridSpec(2,2, fig)
    
    ax = []
    ax += [fig.add_subplot(gs[0,0])]
    ax += [fig.add_subplot(gs[0,1])]
    ax += [fig.add_subplot(gs[1,:])]
    
    ax[0].imshow(img)
    ax[0].axis('off')
    ax[0].set_xlabel('Original')
    
    ax[1].imshow(sorted_img)
    ax[1].axis('off')
    ax[1].set_xlabel('Sorted')
    
    ax[2].hist(img[:,:,0].ravel(), bins=256, range=(0.0, 1.0), alpha=0.4)
    ax[2].hist(img[:,:,1].ravel(), bins=256, range=(0.0, 1.0), alpha=0.4)
    ax[2].hist(img[:,:,2].ravel(), bins=256, range=(0.0, 1.0), alpha=0.4)
    ax[2].set_yscale('log')
    ax[2].set_xlabel('Tonal variations')
    ax[2].set_ylabel('Log of frequency')
    ax[2].set_xlim([-0, 1])
    
    fig.suptitle("Image sort")
    fig.show()

def main():
    img_path = 'img.png'
    
    img = imread(img_path)
    
    sorted_img = sort_img(img)
    
    # Some extra info about img
    plot_info(img, sorted_img) 
    
    imsave('output.png', sorted_img)
    

main()


