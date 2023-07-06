from flask import *
import numpy as np
import pandas as pd
from sklearn.linear_model import LogisticRegression

app=Flask(__name__)

@app.route('/',methods=["POST"])
def diabetesprediction():
  Age=eval(request.form.get("n1"))
  HyperTension=eval(request.form.get("n2"))
  HeartDisease=eval(request.form.get("n3"))
  Bmi=eval(request.form.get("n4"))
  HbA1clevel=eval(request.form.get("n5"))
  BloodGlucoseLevel=eval(request.form.get("n6"))
  
  url="dia.csv"
  data=pd.read_csv(url,header=None)
  flower=data.values
  
  # split the values into input and output
  x=flower[:,7]
  y=flower[:,7]
  
  model=LogisticRegression()
  model.fit(x,y)
  
  arr=model.predict([[Age,HyperTension, HeartDisease,Bmi,HbA1clevel,BloodGlucoseLevel]])
  result=arr[0]
  return "diabetes prediction: "+str(result)


  
  
  return render_template("index.html", result=str(arr[0]))

if __name__ == '__main__':
  app.run()