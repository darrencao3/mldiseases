from django.contrib import admin
from django.urls import path
from disease import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.predict_model, name='predict_model'),
]