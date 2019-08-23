import pandas as pd 
import os
directory = r'C:\KSHITIJ\TE\HumAIn\test\xml construction'
bd_box = pd.read_csv(r"C:\KSHITIJ\TE\HumAIn\test\xml construction\bounding_box.csv")
#print(type(bd_box.at[0 , 'image_width']))

for filenamew in os.listdir(directory):
    if filenamew.endswith("jpg"):
        print(filenamew)
        number = os.path.splitext(os.path.basename(filenamew))[0]
        print(bd_box.at[int(number) , 'image_width'] , bd_box.at[int(number) , 'image_height'])
        #print(type(number))
        