
from flask import Flask, render_template, request
import pandas as pd
import joblib

app = Flask(__name__)

model = joblib.load("bank_churn_model.pkl")

@app.route("/")
def home():
    return render_template("index.html", form_data={})

@app.route("/predict", methods=["POST"])
def predict():
    try:
        customer = pd.DataFrame([{
            "CreditScore": int(request.form["CreditScore"]),
            "Geography": request.form["Geography"],
            "Gender": request.form["Gender"],
            "Age": int(request.form["Age"]),
            "Tenure": int(request.form["Tenure"]),
            "Balance": float(request.form["Balance"]),
            "NumOfProducts": int(request.form["NumOfProducts"]),
            "HasCrCard": int(request.form["HasCrCard"]),
            "IsActiveMember": int(request.form["IsActiveMember"]),
            "EstimatedSalary": float(request.form["EstimatedSalary"])
        }])

        prediction = int(model.predict(customer)[0])
        probability = float(model.predict_proba(customer)[0][1])

        return render_template(
            "index.html",
            prediction=prediction,
            probability=probability,
            form_data=request.form,
            error=None
        )

    except Exception as e:
        return render_template(
            "index.html",
            prediction=None,
            probability=None,
            form_data=request.form,
            error=str(e)
        )

if __name__ == "__main__":
    app.run(debug=True)
