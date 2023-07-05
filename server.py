from falsk import*
import numpy as np
import pandas as pd
from sklearn.linear_model import LogisticRegression

app=Flask(__name__)

@app.route('/')
def diabetes():
  return render_template("index.html")