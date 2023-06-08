from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
import xmlrpc.client

import requests

def index(request):
    #mjnw-2cfb-q9tx
    url = 'https://universidad-modelo.odoo.com' 
    db = 'universidad-modelo'
    username = 'paco991121@hotmail.com'
    password = '55b65e6ead259e2ea9919d0b8c72d56987a009e1'

    common = xmlrpc.client.ServerProxy('{}/xmlrpc/2/common'.format(url))
    
    uid = common.authenticate(db, username, password, {})

    models = xmlrpc.client.ServerProxy('{}/xmlrpc/2/object'.format(url))
    pelis = models.execute_kw(db, uid, password, 'product.product', 'search_read', [], {'fields': []})

    return render(request, 'index.html', {'peliculas': pelis})

def abrirGuardar(request):
    return render(request, 'abrir.html')

def guardar(request):
    if request.method == 'POST':
        id = request.POST['id']
        nombre = request.POST['nombre']
        descripcion = request.POST['descripcion']
        precio = request.POST['precio']
        cantidad = request.POST['stock']
        imagen = request.POST['imagen']

        url = 'https://universidad-modelo.odoo.com'
        db = 'universidad-modelo'
        username = 'paco991121@hotmail.com'
        password = '55b65e6ead259e2ea9919d0b8c72d56987a009e1'

        common = xmlrpc.client.ServerProxy('{}/xmlrpc/2/common'.format(url))
        uid = common.authenticate(db, username, password, {})
        models = xmlrpc.client.ServerProxy('{}/xmlrpc/2/object'.format(url))

        if(id == ""):
            models.execute_kw(db, uid, password, 'product.product', 'create', [{
                'name': nombre,
                'description': descripcion,
                'list_price': float(precio),
                'qty_available': float(cantidad),
            }])

            url = "http://host.docker.internal:8081/admin445uuqlher1u5dsmvdj/create-product.php?secure_key=1DVTYYAHX796EWT315CS9FCLJWS29WYW"

            datos = {
                'ean13': id,
                'referencia': nombre,
                'nombre': nombre,
                'cantidad': cantidad,
                'descripcion': descripcion,
                'precio': precio,
                'imagen': imagen,
                'default_category': 4,
                'categories': [5, 6]
            }

            requests.post(url, data=datos)

        else:
            models.execute_kw(db, uid, password,'product.product', 'write',[[int(id)], {
                'name': nombre, 
                'description': descripcion, 
                'list_price': float(precio)
            }])

        return redirect('index')
    

def borrar(request, id):
    
    url = 'https://universidad-modelo.odoo.com'
    db = 'universidad-modelo'
    username = 'paco991121@hotmail.com'
    password = '55b65e6ead259e2ea9919d0b8c72d56987a009e1'

    common = xmlrpc.client.ServerProxy('{}/xmlrpc/2/common'.format(url))
    uid = common.authenticate(db, username, password, {})
    models = xmlrpc.client.ServerProxy('{}/xmlrpc/2/object'.format(url))
    
    models.execute_kw(db, uid, password, 'product.product', 'unlink', [[id]])

    return redirect('index')


def editar(request, id):
    url = 'https://universidad-modelo.odoo.com'
    db = 'universidad-modelo'
    username = 'paco991121@hotmail.com'
    password = '55b65e6ead259e2ea9919d0b8c72d56987a009e1'

    common = xmlrpc.client.ServerProxy('{}/xmlrpc/2/common'.format(url))
    uid = common.authenticate(db, username, password, {})
    models = xmlrpc.client.ServerProxy('{}/xmlrpc/2/object'.format(url))
    
    peliculas = models.execute_kw(db, uid, password, 'product.product', 'search_read', [[['id', '=', int(id)]]], {'fields': ['id','display_name', 'description', 'list_price', 'qty_available']})
    
    return render(request, 'editar.html', {'objeto': peliculas[0]})

def pelicula(request, id):

    url = 'https://universidad-modelo.odoo.com'
    db = 'universidad-modelo'
    username = 'paco991121@hotmail.com'
    password = '55b65e6ead259e2ea9919d0b8c72d56987a009e1'

    common = xmlrpc.client.ServerProxy('{}/xmlrpc/2/common'.format(url))
    uid = common.authenticate(db, username, password, {})
    models = xmlrpc.client.ServerProxy('{}/xmlrpc/2/object'.format(url))

    peliculas = models.execute_kw(db, uid, password, 'product.product', 'search_read', [[['id', '=', int(id)]]], {'fields': ['id','display_name', 'description', 'list_price', 'qty_available']})

    return render(request, 'pelicula.html', {'objeto': peliculas[0]})