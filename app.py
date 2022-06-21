import tensorflow as tf
import os
import numpy as np #used for numerical analysis
from flask import Flask,request,render_template #Flask-It is our frame work which are going to run
#run or serve our application
#request-for accessing file which was uploaded by user on our application
#render_template-used for rendering the html pages
from tensorflow.keras.models import load_model #to load our trained data
from tensorflow.keras.preprocessing import image
app=Flask(__name__) #our flask app
model=load_model('food.h5') #loading the model
@app.route("/") #default route
def upload_file():
    return render_template("RR.html") #rendering html page
@app.route("/about") #route to about page
def upload_file1():
    return render_template("RR.html") #rendering html page
@app.route("/upload")
def upload_file2():
    return render_template("RRP.html")
@app.route("/predict",methods=["GET","POST"]) #route for our prediction
def upload():
    if request.method=='POST':
        f=request.files['file'] #requesting the file
        basepath=os.path.dirname('__file__')# storing the file directory
        filepath=os.path.join(basepath,"uploads",f.filename)
        f.save(filepath)#saving the file
        img=image.load_img(filepath,target_size=(64,64)) #load and reshaping the image
        x=image.img_to_array(img) #converting image to array
        x=np.expand_dims(x,axis=0) #changing the dimensions of the image
        pred=model.predict_classes(x) #predicting classes
        print(pred)
        index=['French Fries','Pizza','Samosa']
        result=str(index[pred[0]])
        if(result=='French Fries'):
            return render_template("0.html",showcase=str(result))
        elif(result=='Pizza'):
            return render_template("1.html",showcase=str(result))
        else:
            return render_template("2.html",showcase=str(result))
        #returning the result
    else:
        return None
if __name__=="__main__":
    app.run(debug=False) #running the app
        
    
    
            