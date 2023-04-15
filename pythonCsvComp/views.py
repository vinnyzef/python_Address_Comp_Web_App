from django.http import HttpResponse
from django.shortcuts import render
from . import formSet
from . import fileCompare


def submit(request):
    if request.method == 'POST':
        form = formSet.UploadCSVForm(request.POST, request.FILES)
        if form.is_valid():
            csv_file1 = form.cleaned_data['csv_file1']
            csv_file2 = form.cleaned_data['csv_file2']

            # Process the CSV files here
            compare = fileCompare.CompareForms(csv_file1, csv_file2)
            result = compare.compare()  # Call the compare method and store the result
            return HttpResponse("RESULT: <br><pre>" + result + "</pre>")

    else:
        form = formSet.UploadCSVForm()

    return render(request, 'upload.html', {'form': form})
