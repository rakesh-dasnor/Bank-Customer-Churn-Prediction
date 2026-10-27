# Bank Customer Churn Prediction

## About the Project

This project focuses on predicting whether a bank customer is likely to leave the bank. I used Machine Learning to study customer data and build a model that predicts customer churn.

The project also includes a Flask web application where users can enter customer details and view the prediction.

## Project Objectives

- Understand bank customer data.
- Explore the factors that may influence customer churn.
- Prepare the data for Machine Learning.
- Train a model to predict customer churn.
- Build a simple web application to use the trained model.

## Features

- Enter customer details through a web form.
- Predict whether a customer may leave the bank.
- View the churn probability.
- Explore the dataset through a Jupyter Notebook.
- Use the model through a Flask web interface.

## Technologies Used

- Python
- Pandas and NumPy
- Matplotlib and Seaborn
- Scikit-learn
- Flask
- HTML and CSS
- Jupyter Notebook

## Project Structure

```text
Bank-Customer-Churn-Prediction/
├── app.py
├── bank_churn_model.pkl
├── churn_analysis_project.ipynb
├── Churn_Modelling.csv
├── requirements.txt
└── templates/
    └── index.html
```

## Dataset

The project uses a bank customer dataset with details such as:

- Credit Score
- Geography
- Gender
- Age
- Tenure
- Account Balance
- Number of Products
- Credit Card Status
- Active Membership
- Estimated Salary

These details are used to understand customer behaviour and predict whether a customer is likely to leave the bank.

## Data Preprocessing

Before training the model, the dataset needs to be checked and prepared. The preprocessing work may include:

1. Loading the dataset using Pandas.
2. Checking the data types, columns, and statistical information.
3. Checking for missing values and handling them if needed.
4. Checking for duplicate records.
5. Removing unnecessary columns, where applicable.
6. Converting categorical values such as Geography and Gender into numerical values.
7. Selecting the features needed for prediction.
8. Scaling numerical features if required by the model.
9. Splitting the dataset into training and testing data.
10. Preparing the processed data for model training.

## Machine Learning Model

I trained a Machine Learning model using the prepared customer data. The trained model is saved as `bank_churn_model.pkl` and loaded into the Flask application.

When a user enters customer details, the application uses the model to predict whether the customer is likely to leave the bank. It can also display the predicted churn probability.

## Web Application

The web application is developed using Flask, HTML, and CSS. It provides a simple interface for entering customer information and viewing the prediction without running the model manually from a notebook.

## Author

**Rakesh Dasnor**

GitHub: [rakesh-dasnor](https://github.com/rakesh-dasnor)
