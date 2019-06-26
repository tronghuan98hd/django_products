from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('save_product', views.saveProduct, name='save_product'),
    path('delete_product/<int:id>', views.deleteProduct, name='delete_product'),
    path('edit_product/<int:id>', views.editProduct, name='edit_product'),
]