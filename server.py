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
  age=eval(request.form.get("age"))
  hypertension=eval(request.form.get("hypertension"))
  heartdisease=eval(request.form.get("heart"))
  pheight=eval(request.form.get("pheight"))
  