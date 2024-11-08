from django.urls import path

from . import views

# /api/products/
urlpatterns = [
    # equivalent in node js http://localhost:3000/products/1
    # path('<int:pk>', views.ProductDetailApiView.as_view())
    path('', views.product_create_view),
    path('<int:pk>/', views.product_detail_view)
]