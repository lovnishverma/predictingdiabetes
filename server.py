from falsk import*
import numpy as np
import pandas as pd
from sklearn.linear_model import LogisticRegression

app=Flask(__name__)

@app.route('/',methods=["POST"])
def diabetesprediction():
  Age=eval(request.form.get("Age"))
  HyperTension=eval(request.form.get("HyperTension"))
  Heart-Disease=eval(request.form.get(" Heart-Diseas"))
  Bmi=eval(request.form.get("Bmi"))
  HbA1c_level=eval(request.form.get("  HbA1c_level"))
  Blood_Glucose_Level=eval(request.form.get("Blood_Glucose_Level"))
  
  url="dia.csv"
  data=pd.read_csv(url,header=None)
  flower=data.values
  
  # split the values into input and output
  x=flower[:,7]
  y=flower[:,7]
  
  model=LogisticRegression()
  model.fit(x,y)
  
  arr=model.predict([[Age,HyperTension, Heart-Disease,Bmi,HbA1c_level,  Blood_Glucose_Level]])
  result=arr[0]
  return "diabetes prediction: "+str(result)


  
  
  return render_template("index.html", result=str(arr[0]))

if __name__ == '__main__':
  app.run()