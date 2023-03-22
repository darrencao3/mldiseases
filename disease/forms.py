from django import forms
import pandas as pd

temp = pd.read_csv(r'C:\Users\kyuusarii\PycharmProjects\P3\disease\data.csv')
lst = temp['symptoms'].tolist()
lst.insert(0, "None")


class ModelForm(forms.Form):
    symptom1 = forms.ChoiceField(choices=[(x, x) for x in lst])
    symptom2 = forms.ChoiceField(choices=[(x, x) for x in lst])
    symptom3 = forms.ChoiceField(choices=[(x, x) for x in lst])
    symptom4 = forms.ChoiceField(choices=[(x, x) for x in lst])
    symptom5 = forms.ChoiceField(choices=[(x, x) for x in lst])
    symptom6 = forms.ChoiceField(choices=[(x, x) for x in lst])
