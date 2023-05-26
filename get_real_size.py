# import requiered libraries
import cv2 
import numpy as np


def pixel_to_size(model,results):  # calculate and convert pixel to cm 
    real_width = 2.615   # reference object real width (we select 1 TL)
    for object in results.pred[0]: # get detected objects
        if (model.names[int(object[5].item())]=="reference"): # get reference object
            x1 = np.array(results.pred[0][0][:4])[0] # reference object x1 coordinate
            x2 = np.array(results.pred[0][0][:4])[2] # reference object x2 coordinate
            y1 = np.array(results.pred[0][0][:4])[1] # reference object y1 coordinate
            y2 = np.array(results.pred[0][0][:4])[3] # reference object y2 coordinate
            width_pixel = x2-x1 # calculate width in pixel format
            height_pixel = y2-y1 # calculate height in pixel format
            real_metric_width = (width_pixel / real_width) # calculate how many pixels the actual width is equal to
            real_metric_height = (height_pixel / real_width) # calculate how many pixels the actual height is equal to
            real_metric_length = (real_metric_width+real_metric_height / 2) # calculate how many pixels the actual length is equal to
    return real_metric_width,real_metric_height,real_metric_length
            
        
        
def get_real_size(model,results): # get real size for cargo objects
    real_metric_width,real_metric_height,real_metric_length = pixel_to_size(model,results)    # get how many pixels the actual width,height and length
    for object in results.pred[0]:
        if (model.names[int(object[5].item())]=="cargo"):    # get cargo object  
            x1 = np.array(results.pred[0][0][:4])[0] # cargo object x1 coordinate
            x2 = np.array(results.pred[0][0][:4])[2] # cargo object x2 coordinate
            y1 = np.array(results.pred[0][0][:4])[1] # cargo object y1 coordinate
            y2 = np.array(results.pred[0][0][:4])[3] # cargo object y2 coordinate
            width = ((x2-x1)/real_metric_width)*2.165 # get real_width for cargo object 
            height = ((y2-x1)/real_metric_width)*2.165 # get real_height for cargo object 
            length = (width+height)/2 # get real_length for cargo object 
            
            
            sizes = [str(width),str(height),str(length)]  # append width,height,length as like a string format in sizes list       
    return sizes



