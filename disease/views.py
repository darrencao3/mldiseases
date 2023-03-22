from django.shortcuts import render
from .forms import ModelForm
import pickle
import pandas as pd


def predict_model(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = ModelForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            symptom1 = form.cleaned_data['symptom1']
            symptom2 = form.cleaned_data['symptom2']
            symptom3 = form.cleaned_data['symptom3']
            symptom4 = form.cleaned_data['symptom4']
            symptom5 = form.cleaned_data['symptom5']
            symptom6 = form.cleaned_data['symptom6']

            lst = list()
            lst.append(symptom1)
            lst.append(symptom2)
            lst.append(symptom3)
            lst.append(symptom4)
            lst.append(symptom5)
            lst.append(symptom6)
            temp = set(lst)
            if "None" in temp:
                temp.remove("None")
            if len(temp) < 2:
                return render(request, 'home.html', {'form': form, 'prediction': "Please enter at least 2 unique symptoms"})
            lst = list(temp)

            temp2 = pd.read_csv(r'C:\Users\kyuusarii\PycharmProjects\P3\disease\data.csv')
            lst2 = temp2['symptoms'].tolist()

            model_features = []

            for i in range(len(lst2)):
                if lst2[i] in lst:
                    model_features.append(1)
                else:
                    model_features.append(0)

            model_features = [model_features]

            loaded_model1 = pickle.load(open("code_folder/logisticRegression.pkl", 'rb'))
            loaded_model2 = pickle.load(open("code_folder/bernoulliBayes.pkl", 'rb'))
            loaded_model3 = pickle.load(open("code_folder/kNN.pkl", 'rb'))
            prediction1 = loaded_model1.predict(model_features)[0]
            prediction2 = loaded_model2.predict(model_features)[0]
            prediction3 = loaded_model3.predict(model_features)[0]

            prediction = "MyPrediction"

            prediction = prediction1

            if prediction1 == prediction2 and prediction1 == prediction3:
                prediction += " . 3/3"
            elif prediction1 == prediction2:
                prediction += " . 2/3"
            elif prediction2 == prediction3:
                prediction = prediction2
                prediction += " . 2/3"
            elif prediction1 == prediction3:
                prediction += " . 2/3"
            else:
                prediction += " . 1/3"

            return render(request, 'home.html', {'form': form, 'prediction': prediction})

    # if a GET (or any other method) we'll create a blank form
    else:
        form = ModelForm()

    return render(request, 'home.html', {'form': form})