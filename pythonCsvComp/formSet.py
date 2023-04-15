from django import forms

class UploadCSVForm(forms.Form):
    csv_file1 = forms.FileField(label="CSV File 1", required=True, widget=forms.ClearableFileInput(attrs={'accept': '.csv'}))
    csv_file2 = forms.FileField(label="CSV File 2", required=True, widget=forms.ClearableFileInput(attrs={'accept': '.csv'}))
