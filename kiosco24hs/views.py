from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import stores, products, Comment
from .forms import newstoreform, newproductform, contactform, CommentForm
from email.message import EmailMessage
import smtplib


# Create your views here.
def home(request):
    return render(request, 'kiosco24hs/home.html')


def info(request):
    visitante = 'Visitante'
    return render(request, 'kiosco24hs/info.html', {'visitante': visitante})


def stores_v(request):
    s = stores.objects.all()
    return render(request, 'kiosco24hs/stores.html', {'stores': s})


def products_v(request):
    p = products.objects.all()
    return render(request, 'kiosco24hs/products.html', {'products': p})


def create_store(request):
    if request.method == 'GET':
        return render(
            request,
            'kiosco24hs/create_store.html',
            {'forms': newstoreform()}
        )
    else:
        stores.objects.create(
            name=request.POST['name'],
            description=request.POST['description']
        )
        return redirect('stores')


def create_products(request):
    if request.method == 'GET':
        return render(
            request,
            'kiosco24hs/create_products.html',
            {'forms': newproductform()}
        )
    else:
        a = stores.objects.get(name=request.POST['store'])
        products.objects.create(
            title=request.POST['title'],
            price=request.POST['price'],
            store_id=a.id
        )
        return redirect('products')


def details(request, id):
    s = stores.objects.get(id=id)
    p = products.objects.filter(store_id=id)
    return render(
        request,
        'kiosco24hs/details.html',
        {'store': s, 'products': p}
    )


def contact(request):
    if request.method == 'GET':
        return render(
            request,
            'kiosco24hs/contact.html',
            {'forms': contactform()}
        )
    else:
        remitente = "bastianimaximiliano@gmail.com"
        destinatario = request.POST['email']
        mensaje = "Hola, Grupo Informatorio Nro. 1\n\n"

        for i in products.objects.all():
            mensaje += f"{i} - {i.price}\n"

        email = EmailMessage()
        email["From"] = remitente
        email["To"] = destinatario
        email["Subject"] = "Contacto tienda Django"
        email.set_content(mensaje)

        smtp = smtplib.SMTP("smtp.gmail.com", port=587)
        smtp.starttls()
        smtp.login(remitente, "password")
        smtp.sendmail(remitente, destinatario, email.as_string())
        smtp.quit()

        return redirect('home')


# ✅ PRODUCT DETAIL CON COMENTARIOS
def product_detail(request, id):
    product = get_object_or_404(products, id=id)
    comments = product.comments.all()

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.product = product
            comment.save()
            return redirect('product_detail', id=product.id)
    else:
        form = CommentForm()

    context = {
        'product': product,
        'comments': comments,
        'form': form,
    }

    return render(request, 'kiosco24hs/product_detail.html', context)

def delete_comment(request, comment_id):
    comment = get_object_or_404(Comment, id=comment_id)
    product_id = comment.product.id
    comment.delete()
    return redirect('product_detail', id=product_id)
