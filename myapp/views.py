from django.shortcuts import render
import pandas as pd
import os
import joblib
from forex_python.converter import CurrencyRates
from django.conf import settings

# Load pipeline
model_path = os.path.join(settings.BASE_DIR, "myapp", "loan_model.pkl")
pipeline = joblib.load(open(model_path, "rb"))

# Currency converter
c = CurrencyRates()

def loan_form(request):
    return render(request, "form.html")

def predict_form(request):
    if request.method == "POST":
        try:
            # ------------------ Collect inputs ------------------
            person_age = int(request.POST.get("person_age"))
            person_gender = request.POST.get("person_gender")
            person_education = request.POST.get("person_education")
            person_income = float(request.POST.get("person_income"))
            income_currency = request.POST.get("income_currency")
            loan_amnt = float(request.POST.get("loan_amnt"))
            loan_currency = request.POST.get("loan_currency")
            person_emp_exp = int(request.POST.get("person_emp_exp"))
            person_home_ownership = request.POST.get("person_home_ownership")
            loan_intent = request.POST.get("loan_intent")
            loan_percent_income = float(request.POST.get("loan_percent_income"))
            cb_person_cred_hist_length = int(request.POST.get("cb_person_cred_hist_length"))
            credit_score = int(request.POST.get("credit_score"))
            previous_loan_defaults_on_file = request.POST.get("previous_loan_defaults_on_file")

            # ------------------ Currency conversion to USD ------------------
            try:
                income_in_usd = c.convert(income_currency, "USD", person_income) if income_currency != "USD" else person_income
            except:
                income_in_usd = person_income  # fallback

            try:
                loan_in_usd = c.convert(loan_currency, "USD", loan_amnt) if loan_currency != "USD" else loan_amnt
            except:
                loan_in_usd = loan_amnt  # fallback

            # ------------------ Rule-based default check ------------------
            if previous_loan_defaults_on_file == "Yes":
                context = {
                    "myapproved": "No",
                    "predicted_interest_rate": 0,
                    "error": "Loan not approved due to previous loan default.",
                }
                context.update({
                    "person_age": person_age,
                    "person_gender": person_gender,
                    "person_education": person_education,
                    "person_income": round(person_income, 2),
                    "income_currency": income_currency,
                    "income_in_usd": round(income_in_usd, 2),
                    "person_emp_exp": person_emp_exp,
                    "person_home_ownership": person_home_ownership,
                    "loan_amnt": round(loan_amnt, 2),
                    "loan_currency": loan_currency,
                    "loan_in_usd": round(loan_in_usd, 2),
                    "loan_intent": loan_intent,
                    "loan_percent_income": loan_percent_income,
                    "cb_person_cred_hist_length": cb_person_cred_hist_length,
                    "credit_score": credit_score,
                    "previous_loan_defaults_on_file": previous_loan_defaults_on_file,
                })
                return render(request, "result.html", context)

            # ------------------ Prepare input DataFrame ------------------
            input_df = pd.DataFrame([{
                "person_age": person_age,
                "person_gender": person_gender,
                "person_education": person_education,
                "person_income": income_in_usd,
                "person_emp_exp": person_emp_exp,
                "person_home_ownership": person_home_ownership,
                "loan_amnt": loan_in_usd,
                "loan_intent": loan_intent,
                "loan_percent_income": loan_percent_income,
                "cb_person_cred_hist_length": cb_person_cred_hist_length,
                "credit_score": credit_score,
                "previous_loan_defaults_on_file": previous_loan_defaults_on_file
            }])

            # ------------------ Model prediction ------------------
            prediction = pipeline.predict(input_df)[0]
            myapproved = "Yes" if prediction == 1 else "No"

            # ------------------ Interest rate assignment ------------------
            intent_rates = {
                "Personal": 12.5,
                "Education": 8.0,
                "Home": 6.5,
                "Business": 10.0,
                "Medical": 9.0,
                "Venture": 11.0
            }
            predicted_interest_rate = intent_rates.get(loan_intent, 12.0) if myapproved == "Yes" else 0.0

            # ------------------ Prepare context ------------------
            context = {
                "myapproved": myapproved,
                "predicted_interest_rate": predicted_interest_rate,
                "person_age": person_age,
                "person_gender": person_gender,
                "person_education": person_education,
                "person_income": round(person_income, 2),
                "income_currency": income_currency,
                "income_in_usd": round(income_in_usd, 2),
                "person_emp_exp": person_emp_exp,
                "person_home_ownership": person_home_ownership,
                "loan_amnt": round(loan_amnt, 2),
                "loan_currency": loan_currency,
                "loan_in_usd": round(loan_in_usd, 2),
                "loan_intent": loan_intent,
                "loan_percent_income": loan_percent_income,
                "cb_person_cred_hist_length": cb_person_cred_hist_length,
                "credit_score": credit_score,
                "previous_loan_defaults_on_file": previous_loan_defaults_on_file,
            }

            return render(request, "result.html", context)

        except Exception as e:
            return render(request, "result.html", {
                "myapproved": "Error",
                "predicted_interest_rate": 0,
                "error": str(e)
            })

    # GET request
    return render(request, "form.html")
