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
  heartdisease=eval(request.form.get("heartdisease"))
  bmi=eval(request.form.get("bmi"))
  hbaic_level=eval(request.form.get("hbaic_level"))
  blood_glucose-level=eval(request.form.get("blood_glucose_level"))
  