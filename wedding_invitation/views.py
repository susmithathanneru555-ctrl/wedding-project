
from django.shortcuts import render
from django.http import HttpResponse
def home(request):
    return render(request, 'home.html')
def next_page_view(request):
    return render(request, 'next_page.html')
# views.py
def groom_view(request):
    context = {
        "message": "Groom Details",
        "groom_name": "Krishna",
        "father_name": "Ramesh",
        "mother_name": "Lakshmi",
        "wedding_date": "21-05",
    }
    return render(request, "groom.html", context)
def bride_view(request):
        context = {
            "message": "Bride Details",
            "bride_name": "Radha",
            "father_name": "Shyam",
            "mother_name": "Sita",
            "wedding_date": "21-05",
        }
        return render(request, "bride.html", context)

