from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import stores,products
from .forms import newstoreform,newproductform,contactform
from email.message import EmailMessage
import smtplib


# Create your views here.
def home(request):
    return render(request,'home.html')


def info(request):
    visitante = 'Visitante'
    return render(request,"info.html",{'visitante':visitante})

def stores_v(request):
    s = stores.objects.all()
    return render(request, 'stores.html',{'stores':s})

def products_v(request):
    p = products.objects.all()
    return render(request, 'products.html',{'products':p})

def create_store(request):
    if request.method == 'GET':
        return render(request, 'create_store.html',{'forms': newstoreform()})
    else:
        stores.objects.create(name = request.POST['name'],description = request.POST['description'])
        return redirect('stores')
    
def create_products(request):
    if request.method == 'GET':
        return render(request, 'create_products.html',{'forms': newproductform()})
    else:
        a = stores.objects.get(name = request.POST['store'])
        products.objects.create(title = request.POST['title'],price = request.POST['price'],store_id = a.id)
        return redirect('products')
    
def details(request, id):
    s = stores.objects.get(id = id)
    p = products.objects.filter(store_id = id)
    return render(request,'details.html',{'store': s,'products': p})
    
def contact(request):
    if request.method == 'GET':
        return render(request,"contact.html",{'forms':contactform()})
    else:
        remitente = "bastianimaximiliano@gmail.com"
        destinatario = request.POST['email']
        mensaje = """Hola, Grupo Informatorio Nro. 1"""
        for i in products.objects.all():
            mensaje = mensaje + str(i)+ ' - ' + str(i.price) + '\n'
        email = EmailMessage()
        email["From"] = remitente
        email["To"] = destinatario
        email["Subject"] = "Contacto tienda Django"
        email.set_content(mensaje)
        smtp = smtplib.SMTP("smtp.gmail.com",port=587) # si es hotmail/outlook usar "smtp-mail.outlook.com"
        smtp.starttls()
        smtp.login(remitente,"password")
        smtp.sendmail(remitente,destinatario,email.as_string())
        smtp.quit()
        return redirect('home')