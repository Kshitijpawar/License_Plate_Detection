import libraries as lb   #custom libraries
import cv2
import numpy as np
import utils as u
import os
from PIL import Image
from xml.dom import minidom
import xml.etree.ElementTree as ET
directory = r'C:\KSHITIJ\TE\HumAIn\image augmentation\source'

for filename in os.listdir(directory):
    if filename.endswith(".jpg"):
        pure = os.path.splitext(os.path.basename(filename))[0]
        
        f_path = os.path.join(directory, filename)
        conct_pth = os.path.splitext(f_path)[0]
        img_pth = conct_pth + ".jpg"
        xml_pth = conct_pth + ".xml"
        original_boundingbox = lb.get_bounding_box(img_pth)
        original_image = u.read_image( img_pth )
        #rotated_images = lb.apply_transformation( original_image, original_boundingbox, "rotation", 4 )
        w_shifted_images = lb.apply_transformation( original_image, original_boundingbox, "width_shift", 4 )
        #h_shifted_images = lb.apply_transformation( original_image, original_boundingbox, "height_shift", 4 )

        for i in range(4):
            '''
            #ROTATION AUGMENTATION
            im = Image.fromarray(rotated_images[i][0])
            width_im, height_im = im.size
            bdboc = rotated_images[i][1]
            x1 = int(bdboc[0])      #xmin
            y1 = int(bdboc[1])      #ymin
            x2 = int(bdboc[2])      #xmax
            y2 = int(bdboc[3])      #ymax
            path = "C:/KSHITIJ/TE/HumAIn/image augmentation/junk/"+"rotated_"+pure+"_"+str(i)+".jpg"
            im.save(path)
            
            #XML CREATION
            annotation = ET.Element("annotation")

            #sub field "folder"
            folder = ET.SubElement(annotation, "folder")
            folder.text = "images"

            #sub field "filename"
            filename = ET.SubElement(annotation , "filename")
            filename.text = "rotated_"+pure+"_"+str(i)+".jpg"
            
            #sub field "path"
            path = ET.SubElement(annotation, "path")
            #path_text = "C:\\KSHITIJ\\TE\\HumAIn\\"+filenamew
            path.text = "C:\\KSHITIJ\\TE\\HumAIn\\image augmentation\\junk\\"+"rotated_"+pure+"_"+str(i)+".jpg"          #self note:do remember to add path of the image

            #subfield "source" with "database"
            source = ET.SubElement(annotation , "source")
            database = ET.SubElement(source , "database")
            database.text = "Unknown"

            #sub field "size" with parameters width height and depth
            size = ET.SubElement(annotation , "size")
            width = ET.SubElement(size , "width")
            height = ET.SubElement(size , "height")
            depth = ET.SubElement(size , "depth")

            width.text = str(width_im)     #typecasting to string 
            height.text = str(height_im) 	#typecasting to string 
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
            xmin.text = str(x1)	#typecasting from float to int is necessary for bounding box co-ordinates
            ymin.text = str(y1)
            xmax.text = str(x2)
            ymax.text = str(y2)

            tree = ET.ElementTree(annotation)
        
            tree.write("C:\\KSHITIJ\\TE\\HumAIn\\image augmentation\\junk\\"+"rotated_"+pure+"_"+str(i)+".xml")
            #XML CREATION
            #ROTATION AUGMENTATION
            '''
            #WIDTH SHIFT AUGMENTATION
            im = Image.fromarray(w_shifted_images[i][0])
            width_im, height_im = im.size
            bdboc = w_shifted_images[i][1]
            x1 = int(bdboc[0])      #xmin
            y1 = int(bdboc[1])      #ymin
            x2 = int(bdboc[2])      #xmax
            y2 = int(bdboc[3])      #ymax
            path = "C:/KSHITIJ/TE/HumAIn/image augmentation/junk/"+"width_"+pure+"_"+str(i)+".jpg"
            im.save(path)
            
            #XML CREATION
            annotation = ET.Element("annotation")

            #sub field "folder"
            folder = ET.SubElement(annotation, "folder")
            folder.text = "images"

            #sub field "filename"
            filename = ET.SubElement(annotation , "filename")
            filename.text = "width_"+pure+"_"+str(i)+".jpg"
            
            #sub field "path"
            path = ET.SubElement(annotation, "path")
            #path_text = "C:\\KSHITIJ\\TE\\HumAIn\\"+filenamew
            path.text = "C:\\KSHITIJ\\TE\\HumAIn\\image augmentation\\junk\\"+"width_"+pure+"_"+str(i)+".jpg"          #self note:do remember to add path of the image

            #subfield "source" with "database"
            source = ET.SubElement(annotation , "source")
            database = ET.SubElement(source , "database")
            database.text = "Unknown"

            #sub field "size" with parameters width height and depth
            size = ET.SubElement(annotation , "size")
            width = ET.SubElement(size , "width")
            height = ET.SubElement(size , "height")
            depth = ET.SubElement(size , "depth")

            width.text = str(width_im)     #typecasting to string 
            height.text = str(height_im) 	#typecasting to string 
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
            xmin.text = str(x1)	#typecasting from float to int is necessary for bounding box co-ordinates
            ymin.text = str(y1)
            xmax.text = str(x2)
            ymax.text = str(y2)

            tree = ET.ElementTree(annotation)
        
            tree.write("C:\\KSHITIJ\\TE\\HumAIn\\image augmentation\\junk\\"+"width_"+pure+"_"+str(i)+".xml")
            #XML CREATION
            #SHIFT AUGMENTATION
'''
            #HEIGHT AUGMENTATION
            im = Image.fromarray(h_shifted_images[i][0])
            width_im, height_im = im.size
            bdboc = h_shifted_images[i][1]
            x1 = int(bdboc[0])      #xmin
            y1 = int(bdboc[1])      #ymin
            x2 = int(bdboc[2])      #xmax
            y2 = int(bdboc[3])      #ymax
            path = "C:/KSHITIJ/TE/HumAIn/image augmentation/junk/"+"height_"+pure+"_"+str(i)+".jpg"
            im.save(path)
            
            #XML CREATION
            annotation = ET.Element("annotation")

            #sub field "folder"
            folder = ET.SubElement(annotation, "folder")
            folder.text = "images"

            #sub field "filename"
            filename = ET.SubElement(annotation , "filename")
            filename.text = "height_"+pure+"_"+str(i)+".jpg"
            
            #sub field "path"
            path = ET.SubElement(annotation, "path")
            #path_text = "C:\\KSHITIJ\\TE\\HumAIn\\"+filenamew
            path.text = "C:\\KSHITIJ\\TE\\HumAIn\\image augmentation\\junk\\"+"height_"+pure+"_"+str(i)+".jpg"          #self note:do remember to add path of the image

            #subfield "source" with "database"
            source = ET.SubElement(annotation , "source")
            database = ET.SubElement(source , "database")
            database.text = "Unknown"

            #sub field "size" with parameters width height and depth
            size = ET.SubElement(annotation , "size")
            width = ET.SubElement(size , "width")
            height = ET.SubElement(size , "height")
            depth = ET.SubElement(size , "depth")

            width.text = str(width_im)     #typecasting to string 
            height.text = str(height_im) 	#typecasting to string 
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
            xmin.text = str(x1)	#typecasting from float to int is necessary for bounding box co-ordinates
            ymin.text = str(y1)
            xmax.text = str(x2)
            ymax.text = str(y2)

            tree = ET.ElementTree(annotation)
        
            tree.write("C:\\KSHITIJ\\TE\\HumAIn\\image augmentation\\junk\\"+"height_"+pure+"_"+str(i)+".xml   ")
            #XML CREATION
            #HEIGHT AUGMENTATION
'''
        