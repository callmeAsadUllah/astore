from django.urls import path


from store.views import (
    product_list,
    product_detail
)

app_name = 'store'

urlpatterns = [
    path('', product_list, name='product-list'),
    path('<slug:category_slug>/', product_list, name='product-list-by-category'),
    path('<int:id>/<slug:slug>/', product_detail, name='product-detail')
]
