Note: This project was done on PyCharm

0. Run the .py files in code_folder to produce .pkl files
1. Install Django for python using "python -m pip install django" on the terminal
		(From personal experience) If this doesn't work, do "python -m pip install --user django"
2. Do the same for scikit-learn and pandas
3. Navigate to venv, and edit pyvenv.cfg so that it home corresponds to your own version of Python
4. Navigate to disease, then to forms.py
5. On line 4, where it says temp = pd.read_csv..., change the absolute path
6. Do the same on line 36 in views.py, where it says temp2 = pd.read_csv...
7. On the terminal, navigate to the P3 directory
8. Enter in "py manage.py runserver"
9. Click the http address the terminal returns, and it should open up a browser.
10. In the browser, there should be 6 dropdown boxes. Select 2-6 symptoms that you wish to report.
		If less than 2 unique symptoms are selected, the website will simply inform you that the requirements have not been met. This is because one symptom is simply not enough to predict off of even remotely accurately.
11. After inputting the required information, the website will state that the model predicted a disease, as well as whether you should take it "with a grain of salt" or "with a larger grain of salt".
		The former means that the 2 algorithms used predicted the same thing. (Random forest was emitted because the pickle file was an astounding 20+ GBs)
		The latter means that the 2 algorithms disagreed, but went with linear regression, as it is the algorithm that showed the highest accuracy.
