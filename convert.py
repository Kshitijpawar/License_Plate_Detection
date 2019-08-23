#simple script to convert all .png files to .jpg
from glob import glob                                                           
import cv2 
pngs = glob('./*.png')

for j in pngs:
    img = cv2.imread(j)
    cv2.imwrite(j[:-3] + 'jpg', img)