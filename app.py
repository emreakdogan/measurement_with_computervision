from flask import Flask, request ,jsonify, redirect # import necessary libraries to use Flask, send requests
from PIL import Image # This library is used to read image data
import base64 # import base64 library to encode and decode jpeg or png files
import io  # import io library to perform file operations
import torch # import pytorch library to load the model we trained in training.ipynb
import numpy  as np # import numpy library to convert the loaded image to array and RGB format
import json # import json library to convert the information related to the detected object to json format
import os # import os for system operations
import get_real_size #  that calculates real width,height and length


model = torch.hub.load('ultralytics/yolov5', 'custom', path='yolov5/runs/train/exp31/weights/last.pt', force_reload=True) # We load the model we prepared 

app = Flask(__name__) # create an instance of the Flask web application framework

@app.route('/') # define the home page ('/') and redirect to it
def index_view(): 
    return "index.html"


@app.route('/detectObjectType',methods=['GET','POST']) 
def detect_object():   
      if request.method=="POST": # only want the process to be executed when we receive a request with the POST method   
            image_data = request.json['imageBase64']  # read the request sent by the user and read the variable named 'imageBase64'
            img_base64_to_pıl = Image.open(io.BytesIO(base64.b64decode(image_data))) #use the b64decode function to convert the data in base64 format to binary data, read binary data with bytesIO, and then read the image with the open function
            img_array = np.array(img_base64_to_pıl)  # convert our image to a numpy array to use it in the yolov5s model
            img_array_rgb = img_array[:,:,::-1].copy() # convert the image to RGB format
            
            results = model(img_array_rgb,size=320)  # perform object detection using the trained model 


            # create empty lists to store the detected objects, confidence values, and bounding box coordinates
            detect_object = []   
            confidence = []     
            #bounding_box = []     
            sizes = []
            
            for box in results.pred[0]:  # create a loop to access each detected object in results
                  detect_object.append(model.names[int(box[5].item())])  # add the names of the detected objects to our list
                  confidence.append(box[4].item())    # add the confidence values of the detected objects to our list
                  #bounding_box.append(box[:4].tolist()) # add the bounding box coordinates of the detected objects to our list
                                   
            sizes.append(get_real_size.get_real_size(model,results))      # add the sizes of the detected objects to our sizes list                  
            data_json = json.dumps({"objectTypes":detect_object,"confidences":confidence,"sizes":sizes}) # convert our dictionary to json format
      return data_json
      

      
if __name__ =="__main__": # run app
      app.run(host='0.0.0.0', port=8080, debug=True)