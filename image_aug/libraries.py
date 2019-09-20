import os 
import xml.etree.ElementTree as ET
import cv2
import numpy as np

def get_bounding_box(image_path):
    image_pth = os.path.splitext(image_path)[0]
    xml_path = image_pth + ".xml" 
    
    tree = ET.parse(xml_path)
    root = tree.getroot()
    list_bdbox = [int(root[6][4][0].text) , int(root[6][4][1].text) , int(root[6][4][2].text) , int(root[6][4][3].text)]
    
    return list_bdbox

def rotate_image( image, angle, bounding_box ):
    
    # get image dimension
    img_height, img_width = image.shape[:2]
    
    # get rotation matrix
    rotation_matrix = cv2.getRotationMatrix2D( center = (img_width // 2, img_height // 2), angle = angle, scale = 1.0 )
   
    # apply transformation (rotate image) 
    rotated_image = cv2.warpAffine( image, rotation_matrix, (img_width, img_height) )
    
    
    # Apply same transformation to the four bounding box corners
    rotated_point_A = np.matmul( rotation_matrix, np.array( [bounding_box[0], bounding_box[1], 1] ).T )   
    rotated_point_B = np.matmul( rotation_matrix, np.array( [bounding_box[2], bounding_box[1], 1] ).T )   
    rotated_point_C = np.matmul( rotation_matrix, np.array( [bounding_box[2], bounding_box[3], 1] ).T )   
    rotated_point_D = np.matmul( rotation_matrix, np.array( [bounding_box[0], bounding_box[3], 1] ).T )   
    # Compute new bounding box, that is, the bounding box for rotated object
    x = np.array( [ rotated_point_A[0], rotated_point_B[0], rotated_point_C[0], rotated_point_D[0] ] )
    y = np.array( [ rotated_point_A[1], rotated_point_B[1], rotated_point_C[1], rotated_point_D[1] ] )
    new_boundingbox = [np.min( x ).astype(int), np.min( y ).astype(int), np.max( x ).astype(int), np.max( y ).astype(int)]
    
    return rotated_image, new_boundingbox
def width_shift_image( image, width_shift_range, boundingbox ):
    
    img_height, img_width = image.shape[:2]
    factor = img_width * width_shift_range
    
    M = np.float32([[1,0,factor],[0,1,0]]) 
    shifted_image = cv2.warpAffine( image, M, (img_width, img_height) )
    
    # compute new bounding box    
    shifted_point_A = np.matmul( M, np.array( [boundingbox[0], boundingbox[1], 1] ).T )   
    shifted_point_C = np.matmul( M, np.array( [boundingbox[2], boundingbox[3], 1] ).T )   
    
    new_boundingbox = [ shifted_point_A[0].astype(int), shifted_point_A[1].astype(int), 
                        shifted_point_C[0].astype(int), shifted_point_C[1].astype(int) ]
    
    return shifted_image, new_boundingbox
def height_shift_image( image, height_shift_range, boundingbox ):
    
    img_height, img_width = image.shape[:2]
    factor = height_shift_range * img_height
    
    M = np.float32([[1,0,0],[0,1,factor]]) 
    shifted_image = cv2.warpAffine( image, M, (img_width, img_height) )
    
    # compute new bounding box    
    shifted_point_A = np.matmul( M, np.array( [boundingbox[0], boundingbox[1], 1] ).T )   
    shifted_point_C = np.matmul( M, np.array( [boundingbox[2], boundingbox[3], 1] ).T )   
    
    new_boundingbox = [ shifted_point_A[0].astype(int), shifted_point_A[1].astype(int), 
                        shifted_point_C[0].astype(int), shifted_point_C[1].astype(int) ]
    
    return shifted_image, new_boundingbox


t_dic = { "rotation":rotate_image, "width_shift":width_shift_image, "height_shift":height_shift_image}
f_dic = { "rotation":(0, 90), "width_shift":(0, 0.5), "height_shift":(0, 0.5)}
def apply_transformation( image, bounding_box, transformation, n ):
    
    import random
    
    t_images_list = []
    
    for i in range(0, n):
        interval = f_dic[transformation]
        factor = random.uniform(interval[0], interval[1])
        img, bb = t_dic[transformation]( image, factor, bounding_box )
        t_images_list.append( (img, bb, factor) )

    return t_images_list

