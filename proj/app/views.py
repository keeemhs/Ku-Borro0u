from django.shortcuts import render
# from .models import Building, Employee, Visitor
from django.views.generic.base import TemplateView

# Create your views here.

class MainpageView(TemplateView):
    template_name = 'app/main.html'

#def home_view(request):
#    return render(request, 'home.html')

# def db_view(request):
#     employees = Employee.objects.all()
#     buildings = Building.objects.all()
#     visitors = Visitor.objects.all()
#     return render(request, 'app/all.html', {"employees":employees, "buildings":buildings, "visitors":visitors})

# def emp_view(request):
#     employees = Employee.objects.all()
#     return render(request, 'app/emp.html', {"employees":employees})

# def bui_view(request):
#     buildings = Building.objects.all()
#     return render(request, 'app/bui.html', {"buildings":buildings})

# def vis_view(request):
#     visitors = Visitor.objects.all()
#     return render(request, 'app/vis.html', {"visitors":visitors})

#def building_view(request):
#    buildings = Building.objects.all()
#    return render(request, 'index.html', {"employees":employees})