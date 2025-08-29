# 🏦 Smart Loan Predictor  

![Python](https://img.shields.io/badge/Python-3.11-blue)
![Django](https://img.shields.io/badge/Django-5.0-green)
![Machine Learning](https://img.shields.io/badge/ML-ScikitLearn-orange)
![Status](https://img.shields.io/badge/Status-Active-brightgreen)

## 📌 Overview  

Smart Loan Predictor is a **Machine Learning + Django web application** that predicts whether a loan application will be approved based on applicant details such as income, loan amount, credit history, and more.  

This project demonstrates how ML can be applied in finance for **risk assessment** and provides a clean, user-friendly web interface for predictions.  

---

## 🚀 Features  
- ✅ Loan approval prediction using ML model  
- ✅ Django-based web interface with Bootstrap styling  
- ✅ Automatic **INR → USD currency conversion** for calculations  
- ✅ User-friendly form & result display  
- ✅ Ready for deployment on platforms like Heroku / Render / AWS  

---

## 🛠️ Tech Stack  
- **Frontend**: HTML, CSS, Bootstrap  
- **Backend**: Django (Python)  
- **Machine Learning**: Scikit-learn, Pandas, NumPy  
- **Model Persistence**: Joblib  
- **Version Control**: Git & GitHub  

---


## 🖼️ Screenshots  

### Loan Application Form  
![Loan Form]("C:\Users\Lenovo\OneDrive\Pictures\Screenshots\Screenshot 2025-08-30 002623.png")

### Prediction Result  
![Result Page]("C:\Users\Lenovo\OneDrive\Pictures\Screenshots\Screenshot 2025-08-30 002728.png")

---

## ⚙️ Installation  

Clone this repository:  
```bash
git clone https://github.com/Arjunsharma20/Smart-Loan-Predictor.git
cd Smart-Loan-Predictor


## 📂 Project Structure  
Smart-Loan-Predictor/
│── myproject/ # Django project folder
│ ├── myapp/ # Main app with views & templates
│ │ ├── templates/ # form.html, result.html
│ │ ├── views.py # Prediction logic
│ │ ├── urls.py # App routes
│ │ ├── loan_model.pkl # Trained ML model
│ │ └── encoder.pkl # Preprocessing encoder
│ ├── settings.py # Django settings
│ └── urls.py # Project-level routes
│
│── requirements.txt # Python dependencies
│── README.md # Project documentation
