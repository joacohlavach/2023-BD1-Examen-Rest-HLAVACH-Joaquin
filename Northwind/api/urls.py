from django.urls import path, include
from .views import *

urlpatterns = [
    path("customer/", getAllCustomers, name="getAllCustomers"),
    path("customer/<str:pk>", getCustomerById , name="getCustomerById"),

    path("supplier/", getAllSuppliers, name="getAllSuppliers"),
    path("supplier/<str:pk>", getSupplierById , name="getSupplierById"),

    path("category/", getAllCategories, name="getAllCategories"),
    path("category/<str:pk>", getCategoryById , name="getCategoryById"), 

    path("product/", getAllProducts, name="getAllProducts"),
    path("product/<str:pk>", getProductById , name="getProductById"), 

    path("order/", getAllOrders, name="getAllOrders"),
    path("order/<str:pk>/", getOrderById, name="getOrderById"),

    path("orderdetail/", getAllOrderDetails, name="getAllOrderDetails"),
    path("orderdetail/<int:pk>/<int:pk2>", getOrderDetailById, name="getOrderDetailById"),

    path("employee/", getAllEmployees, name="getAllEmployees"),
    path("employee/<int:pk>/", getEmployeeById, name="getEmployeeById"),

    #pruebas
    path("punto1/", punto1),
    path("test/", create_order_with_details, name="test"),
    #path("pruebacountry/", pruebacountry, name="test"),
    ]