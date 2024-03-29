from django.shortcuts import render, get_object_or_404
from .models import Category ,Subcategory


def Categories(request):
    catigories = Category.objects.all()
    return render(request, "index.html", {'categories': catigories})

#ну я привык что в drf огромные views.как то не привычно

def Subcategorydetail(request, pk):
    subcategory = get_object_or_404(Subcategory, pk=pk)
    return render(request, "subindex.html", {'subcategory': subcategory})


