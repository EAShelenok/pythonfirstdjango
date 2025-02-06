from django.shortcuts import render
from django.views.generic import TemplateView

def func_view(request):
    return render(request, 'templ_func.html')

class Class_View(TemplateView):
    template_name = 'templ_class.html'