from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView

from catalog.forms import ProductForm
from catalog.models import Product, Version


class ProductListView(ListView):
    model = Product
    template_name = 'catalog/index.html'

    # def index(request):
    #     product_list = Product.objects.all()
    #     context = {
    #         'object_list': product_list,
    #     }
    #     return render(request, 'catalog/index.html', context)def get_context_data(self, **kwargs):
    #

    def get_context_data(self, *args, **kwargs):
        data = super().get_context_data(*args, **kwargs)
        data['version'] = self.object.version_set.filter(is_active=True).first(),

        return data


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

class ProductCreateView(CreateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('catalog:index')


class ProductUpdateView(UpdateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('catalog:index')
