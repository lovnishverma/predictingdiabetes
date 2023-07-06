from flask import *
import numpy as np
import pandas as pd
from sklearn.linear_model import LogisticRegression

app=Flask(__name__)

@app.route('/',methods=["POST"])
def diabetesprediction():
  if request.method== 'POST' :
  Age=eval(request.form["n1"])
  HyperTension=eval(request.form["n2"])
  HeartDisease=eval(request.form["n3"])
  Bmi=eval(request.form["n4"])
  HbA1clevel=eval(request.form["n5"])
  BloodGlucoseLevel=eval(request.form["n6"])
  
  url = "dia.csv"
  data = pd.read_csv(url,header=None)
  flower=data.values
  
  # split the values into input and output
  x=flower[:,7]
  y=flower[:,7]
  
  model = LogisticRegression()
  model.fit(x,y)
  
  arr = model.predict([[Age,HyperTension, HeartDisease,Bmi,HbA1clevel,BloodGlucoseLevel]])
  
  return render_template("index.html", result=str(arr[0]))

if __name__ == '__main__':
  app.run(debug=True)