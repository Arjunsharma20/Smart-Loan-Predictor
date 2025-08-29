from django.contrib import admin
from django.urls import path
from myapp import views

urlpatterns = [
    path('admin/', admin.site.urls),

    # Show form at home page
    path('', views.loan_form, name='loan_form'),

    # Handle prediction (POST request)
    path('predict_form/', views.predict_form, name='predict_form'),
]
