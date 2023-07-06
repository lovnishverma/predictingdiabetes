from falsk import*
import numpy as np
import pandas as pd
from sklearn.linear_model import LogisticRegression

app=Flask(__name__)

@app.route('/')
def diabetes():
  return render_template("index.html")

@app.route('/diabetes',methods=["post"])
def page():
  Age=eval(request.form.get("n1"))
  HyperTension=eval(request.form.get("n2"))
  Heart-Disease=eval(request.form.get("n3"))
  Bmi=eval(request.form.get("n4"))
  HbA1c_level=eval(request.form.get("n5"))
  Blood_Glucose_Level=eval(request.form.get("n6"))
  
  url=""
  data=pd.read_csv(url,header=None)
  flower=data.values
  
  # split the values into input and output
  x=flower[:,7]
  y=flower[:,7]
  
  model=LogisticRegression()
  model.fit(x,y)
  
  arr=model.predict([[Age,HyperTension, Heart-Disease,Bmi,HbA1c_level,  Blood_Glucose_Level]])
  
  
  return render_template("index.html", data=str(arr[0]))

if __name__ == '__main__':
  app.run()