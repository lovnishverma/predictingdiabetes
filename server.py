from flask import *
import numpy as np
import pandas as pd
from sklearn.linear_model import LogisticRegression


app=Flask(__name__)

@app.route('/')
def iris():
  return render_template("index.html")

@app.route('/irisf', methods=["POST"])
def page():
  swidth=eval(request.form.get("n1"))
  sheight=eval(request.form.get("n2"))
  pwidth=eval(request.form.get("n3"))
  pheight=eval(request.form.get("n4"))
  height=eval(request.form.get("n5"))
  hght=eval(request.form.get("n6"))
  
  url="te.csv"
  
  data=pd.read_csv(url, header=None)
  flower=data.values
  
  #Split
  x=flower[:,:6]
  y=flower[:,-1]
  
  model=LogisticRegression()
  model.fit(x,y)
  
  arr=model.predict([[swidth,sheight,pwidth,pheight,height,hght]])

  return render_template("index.html", data=str(0))


if __name__ == '__main__':
  app.run()