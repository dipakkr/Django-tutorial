from django.urls import path

from products.views import product_detail_view, product_create_view, product_list_view

app_name = "products"
urlpatterns = [
    
    path('all/', product_list_view, ),
    path('<int:id>/', product_detail_view, name="product-detail"),
    path('create/', product_create_view )
]
