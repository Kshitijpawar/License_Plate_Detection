import requests
import random
import numpy as np 
import pandas as pd
from tqdm import tqdm
from PIL import Image
import urllib
import os
import json

#Initializing  empty lists for appending
img_width = []
img_height = []
x_min_list = []
y_min_list = []
x_max_list = []
y_max_list = []

#column name
col = ['x_min_list' ,'y_min_list' , 'x_max_list' , 'y_max_list' , 'img_height' , 'img_width']

data = pd.read_json('Indian_Number_plates.json', lines=True)
pd.set_option('display.max_colwidth', -1)

# Delete the empty column
del data['extras']

# Extracting the boundig boxes co-ordinates
data['points'] = data.apply(lambda row: row['annotation'][0]['points'], axis=1)

def downloadTrainingData(df):

    for index, row in df.iterrows():

        # Obtaining image from the URL
        resp = urllib.request.urlopen(row[0])
        p = np.array(Image.open(resp))
        
          

        #Converting to normalized co-ordinates by multiplying with image_width and image_height 
        x_point_top = row[1][0]['x']*im.shape[1]
        y_point_top = row[1][0]['y']*im.shape[0]
        x_point_bot = row[1][1]['x']*im.shape[1]
        y_point_bot = row[1][1]['y']*im.shape[0]
        x_min_list.append(x_point_top)
        y_min_list.append(y_point_top)
        x_max_list.append(x_point_bot)
        y_max_list.append(y_point_bot)
        img_width.append(row['annotation'][0]['imageWidth'])
        img_height.append(row['annotation'][0]['imageHeight'])
        
        print(x_point_top,y_point_top,x_point_bot,y_point_top)
	
	        

        # Cropping the license plate and storing for future references
        car_Image = Image.fromarray(p)	#numpy array to PIL Image 
        car_Image.save("C:\KSHITIJ\TE\HumAIn\images\cars\car"+str(index)+".jpg")
        plate_Image = car_Image.crop((x_point_top, y_point_top, x_point_bot, y_point_bot))
        plate_Image.save("C:\KSHITIJ\TE\HumAIn\images\plates\plate"+str(index)+".jpg")
        
	        	
downloadTrainingData(data)

#Creating bounding_box.csv for bounding box .xml file creation for each image of car in the dataset

tuple_co = list(zip(x_min_list , y_min_list , x_max_list , y_max_list , img_height , img_width))
df = pd.DataFrame(tuple_co , columns = col) #creating pandas dataframe
df.to_csv('bounding_box_final.csv' , index = None)