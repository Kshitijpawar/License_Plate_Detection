#.xml file creation to use with TensorFlow Object Detection API for transfer learning on custom dataset

import os
import xml.etree.cElementTree as ET
import pandas as pd

bd_box = pd.read_csv(r"C:\KSHITIJ\TE\HumAIn\test\xml construction\bounding_box.csv")
directory = r'C:\KSHITIJ\TE\HumAIn\test\xml construction'
for filenamew in os.listdir(directory):
    if filenamew.endswith("jpg"):
        number = os.path.splitext(os.path.basename(filenamew))[0]	#extracts filename without extension
        annotation = ET.Element("annotation")

        #sub field "folder"
        folder = ET.SubElement(annotation, "folder")
        folder.text = "images"

        #sub field "filename"
        filename = ET.SubElement(annotation , "filename")
        filename.text = filenamew
        
        #sub field "path"
        path = ET.SubElement(annotation, "path")
        #path_text = "C:\\KSHITIJ\\TE\\HumAIn\\"+filenamew
        path.text = "C:\\KSHITIJ\\TE\\HumAIn\\"+filenamew          #self note:do remember to add path of the image

        #subfield "source" with "database"
        source = ET.SubElement(annotation , "source")
        database = ET.SubElement(source , "database")
        database.text = "Unknown"

        #sub field "size" with parameters width height and depth
        size = ET.SubElement(annotation , "size")
        width = ET.SubElement(size , "width")
        height = ET.SubElement(size , "height")
        depth = ET.SubElement(size , "depth")

        width.text = str(int(bd_box.at[int(number) , 'image_width']))		#typecasting to string 
        height.text = str(int(bd_box.at[int(number) , 'image_height']))		#typecasting to string 
        depth.text = "3"

        segmented = ET.SubElement(annotation , "segmented")
        segmented.text = "0"

        #subfield object
        object = ET.SubElement(annotation , "object")
        name = ET.SubElement(object , "name")
        pose = ET.SubElement(object , "pose")
        truncated = ET.SubElement(object , "truncated")
        difficult = ET.SubElement(object , "diffcult")
        bndbox = ET.SubElement(object , "bndbox")
        xmin = ET.SubElement(bndbox , "xmin")
        ymin = ET.SubElement(bndbox , "ymin")
        xmax = ET.SubElement(bndbox , "xmax")
        ymax = ET.SubElement(bndbox , "ymax")
        name.text = "plate"
        pose.text = "Unspecified"
        truncated.text = "0"
        difficult.text = "0"
        xmin.text = str(int(bd_box.at[int(number) , 'x_min_list']))	#typecasting from float to int is necessary for bounding box co-ordinates
        ymin.text = str(int(bd_box.at[int(number) , 'y_min_list']))
        xmax.text = str(int(bd_box.at[int(number) , 'x_max_list']))
        ymax.text = str(int(bd_box.at[int(number) , 'y_max_list']))

        tree = ET.ElementTree(annotation)
       
        tree.write(number+".xml")
       
        
        