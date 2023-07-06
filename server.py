from flask import Flask, render_template, request
import numpy as np
import pandas as pd
from sklearn.linear_model import LogisticRegression

app = Flask(__name__)

def validate_input(input_data):
    # Check if all input fields are provided
    required_fields = ["age", "hypertension", "heart_disease", "bmi", "HbA1c_level", "blood_glucose_level"]
    for field in required_fields:
        if field not in input_data or not input_data[field]:
            return False
    return True

@app.route('/', methods=["POST", "GET"])
def page():
    if request.method == "POST":
        input_data = {
            "age": float(request.form.get("age")),
            "hypertension": int(request.form.get("hypertension")),
            "heart_disease": int(request.form.get("heart_disease")),
            "bmi": float(request.form.get("bmi")),
            "HbA1c_level": float(request.form.get("HbA1c_level")),
            "blood_glucose_level": float(request.form.get("blood_glucose_level"))
        }

        if validate_input(input_data):
            url = "te.csv"
            data = pd.read_csv(url, header=None)
            diabete = data.values

            # Split
            x = diabete[:, :6]
            y = diabete[:, 6]

            model = LogisticRegression()
            model.fit(x, y)

            try:
                arr = model.predict([[input_data["age"], input_data["hypertension"], input_data["heart_disease"],
                                      input_data["bmi"], input_data["HbA1c_level"], input_data["blood_glucose_level"]]])
                result = str(arr[0])
            except:
                result = "Error occurred during prediction"

            return render_template("index.html", data=result)
        else:
            error_message = "Please provide values for all input fields."
            return render_template("index.html", error_message=error_message)

    return render_template("index.html", error_message="")

if __name__ == '__main__':
    app.run()
