from django.shortcuts import render
from django.contrib.auth.decorators import permission_required


# Create your views here.

@permission_required('smartphone.view_smartphone', raise_exception=True)
def home(request):
    return render(request, 'smartphone/home.html')