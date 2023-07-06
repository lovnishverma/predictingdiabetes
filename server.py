from flask import Flask, render_template, request
import numpy as np
import pandas as pd
from sklearn.linear_model import LogisticRegression

app = Flask(__name__)

def validate_input(input_data):
    required_fields = ["age", "hypertension", "heart_disease", "bmi", "HbA1c_level", "blood_glucose_level"]
    for field in required_fields:
        if field not in input_data or input_data[field] == "":
            return False
    return True

@app.route('/', methods=["POST", "GET"])
def page():
    if request.method == "POST":
        input_data = {
            "age": request.form.get("age"),
            "hypertension": request.form.get("hypertension"),
            "heart_disease": request.form.get("heart_disease"),
            "bmi": request.form.get("bmi"),
            "HbA1c_level": request.form.get("HbA1c_level"),
            "blood_glucose_level": request.form.get("blood_glucose_level")
        }

        if validate_input(input_data):
            url = "te.csv"
            data = pd.read_csv(url)
            x = data.iloc[:, :-1]
            y = data.iloc[:, -1]

            model = LogisticRegression()
            model.fit(x, y)

            try:
                input_values = [float(input_data[field]) for field in input_data]
                arr = model.predict([input_values])
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
