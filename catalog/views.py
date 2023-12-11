from django.shortcuts import render
from django.views.generic import ListView, DetailView

from catalog.models import Product


class ProductListView(ListView):
    model = Product
    template_name = 'catalog/index.html'

# def index(request):
#     product_list = Product.objects.all()
#     context = {
#         'object_list': product_list,
#     }
#     return render(request, 'catalog/index.html', context)


def contacts(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        print(f'{name}, {phone}: {message}')
    return render(request, 'catalog/contacts.html')


class ProductDetailView(DetailView):
    model = Product
    template_name = 'catalog/product_detail.html'


# def product(request, pk):
#     context = {
#         'object': Product.objects.get(pk=pk),
#     }
#     return render(request, 'catalog/product_detail.html', context)

