from django.shortcuts import render
import os
from dotenv import load_dotenv

load_dotenv()
# Create your views here.


def homepage(request):

    print(os.getenv("IURL"))
    
    return render(request,"home.html")