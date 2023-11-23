from .serializers import *
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.http import HttpResponse, JsonResponse
from .models import Customers, Suppliers, Categories, Products, Orders, Orderdetails, Employees


# --- COSTUMERS ------------------------------------------------------------------------------------
@api_view(["GET", "POST"])
def getAllCustomers(request):
    if request.method == "GET":
        customers = Customers.objects.all()         
        #customers = Customers.objects.filter(contactname__startswith = 'M')[:4]
        customersSerializers = CustomerSerializer(customers, many=True)
        return Response(customersSerializers.data, status=status.HTTP_200_OK)
    elif request.method == "POST":
        customerNuevo = CustomerSerializer(data = request.data)
        if customerNuevo.is_valid():
            customerNuevo.save()
            return Response(customerNuevo.data, status=status.HTTP_200_OK)
        return Response(customerNuevo.errors ,status=status.HTTP_400_BAD_REQUEST)
    
@api_view(["GET", "PUT", "DELETE"])
def getCustomerById(request, pk):
    try:
        customer = Customers.objects.get(customerid=pk)
    except Exception:
        return Response(status=status.HTTP_204_NO_CONTENT)
    if request.method == 'GET':
        serializer = CustomerSerializer(customer)
        return Response(serializer.data, status=status.HTTP_200_OK)
    if request.method == 'PUT':
        request.data['customerid'] = pk

        if 'companyname' not in request.data:
            request.data['companyname'] = customer.companyname
    
        serializer = CustomerSerializer(customer, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    if request.method == 'DELETE':
        Orders.objects.filter(customer=customer).delete()
        #customer.delete()
        return Response(status=status.HTTP_200_OK)

# --- SUPPLIERS ------------------------------------------------------------------------------------
@api_view(["GET", "POST"])
def getAllSuppliers(request):
    if request.method == "GET":         
        suppliers = Suppliers.objects.all()
        suppliersSerializers = SupplierSerializer(suppliers, many=True)
        return Response(suppliersSerializers.data, status=status.HTTP_200_OK)
    elif request.method == "POST":
        supplierNuevo = SupplierSerializer(data = request.data)
        if supplierNuevo.is_valid():
            supplierNuevo.save()
            return Response(supplierNuevo.data, status=status.HTTP_200_OK)
        return Response(supplierNuevo.errors ,status=status.HTTP_400_BAD_REQUEST)
    
@api_view(["GET", "PUT", "DELETE"])
def getSupplierById(request, pk):
    try:
        supplier = Suppliers.objects.get(supplierid=pk)
    except Exception:
        return Response(status=status.HTTP_204_NO_CONTENT)
    if request.method == 'GET':
        serializer = SupplierSerializer(supplier)
        return Response(serializer.data, status=status.HTTP_200_OK)
    if request.method == 'PUT':
        request.data['supplierid'] = pk
    
        serializer = SupplierSerializer(supplier, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    if request.method == 'DELETE':
        supplier.delete()
        return Response(status=status.HTTP_200_OK)

# --- CATEGORIES ------------------------------------------------------------------------------------
@api_view(["GET", "POST"])
def getAllCategories(request):
    if request.method == "GET":         
        categories = Categories.objects.all()
        categoriesSerializers = CategorieSerializer(categories, many=True)
        return Response(categoriesSerializers.data, status=status.HTTP_200_OK)
    elif request.method == "POST":
        categorieNuevo = CategorieSerializer(data = request.data)
        if categorieNuevo.is_valid():
            categorieNuevo.save()
            return Response(categorieNuevo.data, status=status.HTTP_200_OK)
        return Response(categorieNuevo.errors ,status=status.HTTP_400_BAD_REQUEST)
    
@api_view(["GET", "PUT", "DELETE"])
def getCategoryById(request, pk):
    try:
        categorie = Categories.objects.get(categoryid=pk)
    except Exception:
        return Response(status=status.HTTP_204_NO_CONTENT)
    if request.method == 'GET':
        serializer = CategorieSerializer(categorie)
        return Response(serializer.data, status=status.HTTP_200_OK)
    if request.method == 'PUT':
        request.data['categoryid'] = pk
    
        serializer = CategorieSerializer(categorie, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    if request.method == 'DELETE':
        categorie.delete()
        return Response(status=status.HTTP_200_OK)

# --- PRODUCTS ------------------------------------------------------------------------------------
@api_view(["GET", "POST"])
def getAllProducts(request):
    if request.method == "GET":         
        products = Products.objects.select_related('supplierid').all()
        serializer = ProductSerializer(products, many=False)
        return JsonResponse(serializer.data)
    elif request.method == "POST":
        productNuevo = ProductSerializer(data=request.data)
        if productNuevo.is_valid():
            productNuevo.save()
            return Response(productNuevo.data, status=status.HTTP_200_OK)
        return Response(productNuevo.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(["GET", "PUT", "DELETE"])
def getProductById(request, pk):
    try:
        product = Products.objects.get(productid=pk)
    except Exception:
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    if request.method == 'GET':
        serializer = ProductSerializer(product)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    if request.method == 'PUT':
        request.data['productid'] = pk
        serializer = ProductSerializer(product, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    if request.method == 'DELETE':
        product.delete()
        return Response(status=status.HTTP_200_OK)

# --- ORDERS ------------------------------------------------------------------------------------

@api_view(["GET", "POST"])
def getAllOrders(request):
    if request.method == "GET":         
        orders = Orders.objects.all()
        orderSerializers = OrderSerializer(orders, many=True)
        return Response(orderSerializers.data, status=status.HTTP_200_OK)
    elif request.method == "POST":
        orderNuevo = OrderSerializer(data=request.data)
        if orderNuevo.is_valid():
            orderNuevo.save()
            return Response(orderNuevo.data, status=status.HTTP_200_OK)
        return Response(orderNuevo.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(["GET", "PUT", "DELETE"])
def getOrderById(request, pk):
    try:
        order = Orders.objects.get(orderid=pk)
    except Exception:
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    if request.method == 'GET':
        serializer = OrderSerializer(order)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    if request.method == 'PUT':
        request.data['orderid'] = pk
        serializer = OrderSerializer(order, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    if request.method == 'DELETE':
        order.delete()
        return Response(status=status.HTTP_200_OK)

# --- ORDER_DETAILS ------------------------------------------------------------------------------------

@api_view(["GET", "POST"])
def getAllOrderDetails(request):
    if request.method == "GET":         
        order_details = Orderdetails.objects.all()
        orderDetailsSerializers = OrderdetailSerializer(order_details, many=True)
        return Response(orderDetailsSerializers.data, status=status.HTTP_200_OK)
    elif request.method == "POST":
        orderDetailNuevo = OrderdetailSerializer(data=request.data)
        if orderDetailNuevo.is_valid():
            orderDetailNuevo.save()
            return Response(orderDetailNuevo.data, status=status.HTTP_200_OK)
        return Response(orderDetailNuevo.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(["GET", "PUT", "DELETE"])
def getOrderDetailById(request, pk, pk2):
    try:
        order_detail = Orderdetails.objects.get(orderid=pk, productid=pk2)
    except Exception:
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    if request.method == 'GET':
        serializer = OrderdetailSerializer(order_detail)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    if request.method == 'PUT':
        request.data['orderid'] = pk
        serializer = OrderdetailSerializer(order_detail, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    if request.method == 'DELETE':
        order_detail.delete()
        return Response(status=status.HTTP_200_OK)

# --- EMPLOYEES ------------------------------------------------------------------------------------

@api_view(["GET", "POST"])
def getAllEmployees(request):
    if request.method == "GET":         
        employees = Employees.objects.all()
        employeeSerializers = EmployeeSerializer(employees, many=True)
        return Response(employeeSerializers.data, status=status.HTTP_200_OK)
    elif request.method == "POST":
        employeeNuevo = EmployeeSerializer(data=request.data)
        if employeeNuevo.is_valid():
            employeeNuevo.save()
            return Response(employeeNuevo.data, status=status.HTTP_200_OK)
        return Response(employeeNuevo.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(["GET", "PUT", "DELETE"])
def getEmployeeById(request, pk):
    try:
        employee = Employees.objects.get(employeeid=pk)
    except Exception:
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    if request.method == 'GET':
        serializer = EmployeeSerializer(employee)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    if request.method == 'PUT':
        request.data['employee_id'] = pk

        if 'firstname' not in request.data:
            request.data['firstname'] = employee.firstname

        if 'lastname' not in request.data:
            request.data['lastname'] = employee.lastname
        
        if 'notes' not in request.data:
            request.data['notes'] = employee.notes

        serializer = EmployeeSerializer(employee, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    if request.method == 'DELETE':
        employee.delete()
        return Response(status=status.HTTP_200_OK)

# ---------------------------------------- PRUEBAS -------------------------------------------

@api_view(["POST"])
def create_order_with_details(request):
    order_serializer = OrderSerializer(data=request.data)
    if order_serializer.is_valid():
        order = order_serializer.save()
        order_details_data = request.data.get('order_details', [])
        for order_detail_data in order_details_data:
            order_detail_data['order'] = order.id
            order_detail_serializer = OrderdetailSerializer(data=order_detail_data)
            if order_detail_serializer.is_valid():
                order_detail_serializer.save()
            else:
                order.delete()
                return Response(order_detail_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response(order_serializer.data, status=status.HTTP_201_CREATED)
    return Response(order_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(["GET"])
def get_orders_with_details(request):
    orders = Orders.objects.all()
    order_serializer = OrderSerializer(orders, many=True)
    return Response(order_serializer.data, status=status.HTTP_200_OK)

#-----------------y

def punto1(request):
    letra = request.query_params.get("letter")
    year = request.query_params.get("year")

    empleadosFiltrados = Employees.objects.filter(firstname__icontains = letra)
    resultados = []
    for e in empleadosFiltrados:
        resultado = {
            "id" : e.employeeid,
            "nombre" : e.firstname,
            "apellido" : e.lastname,
            "birthdate" : e.birthdate
        }
        if e.birthdate.year >= int(year):
            resultados.append(resultado)
    serializados = Punto1Serializer(resultados, many=True)
    return Response(serializados.data)

def pruebacountry(request):
    if request.method == 'GET':
        country = request.query_params.get("country")
        orders = Orders.objects.filter(shipcountry=country)
        resultados = []

        for order in orders:
            resultado = {
                "orderid" : order.orderid,
                "shippingcountry" : order.shipcountry
            }
            resultados.append(resultado)
        order_serializer = CountrySerializer(resultados, many=True)
        return Response(order_serializer.data)

import datetime
@api_view(['GET'])
def ejemplo1(request):
    if request.method == 'GET':
        fecha = request.query_params.get('mayorquefecha')
        try:
            fecha = datetime.datetime.strptime(fecha, '%Y-%m-%d').date()
        except ValueError:
            fecha = None
        letra = request.query_params.get('letra')
        employees = Employees.objects.filter(birthdate__lt=fecha).filter(lastname__contains = letra).filter(reportsto__lastname__contains = letra)
        resultados = []
        for employee in employees:
            employee.salary = request.data['salario']
            employee.save()
            resultado = { 
                        "id":employee.employeeid,
                        "nombre": employee.firstname,
                        "apellido":employee.lastname,
                        "reportsto":employee.reportsto,
                        "nacimiento":employee.birthdate,
                        "salario":employee.salary
                        }
            
            resultados.append(resultado)
        serializados = Punto1Serializer(resultados, many=True)
        return Response(serializados.data)

#employees = Employees.objects.filter(birthdate__lt = datetime.date(1950,1,3))
#clientes = Clientes.objects.all()[:4]
#clientes = Clientes.objects.all().order_by('nombre', 'altura')
#clientes = Clientes.objects.all()
#clientes = Clientes.objects.filter(apellido='ALONSO')
#clientes = Clientes.objects.filter(cod_cliente__gte=5)
#clientes = Clientes.objects.filter(apellido__startswith = 'A')
#clientes = Clientes.objects.filter(nombre__startswith = 'A', cod_condicion_iva__gte=2 )
#clientes = Clientes.objects.filter(Q(apellido__startswith = 'M') |Q(apellido__startswith = 'C') )
#serializados = ClientesSerializer(clientes,many = True)
#return Response(serializados.data)