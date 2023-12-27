from django.shortcuts import redirect, render
from .models import Product, Commande
from django.db import models


# Create your views here.
def index(request):
    product_object = Product.objects.all()
    item_name = request.GET.get('item-name')
    if item_name !='' and item_name is not None:
        product_object = Product.objects.filter(title__icontains=item_name)
    if request.method == 'POST':
        nouveau_produit = Product(
            title=request.POST['title'],
            price=request.POST['price'],
            description=request.POST['description'],
            category_id=request.POST['category'],  # Utilisation de l'ID de la catégorie
            image=request.POST['image']
        )
        nouveau_produit.save()
   
    return render(request, 'shop/index.html', {'product_object': product_object})

def detail(request, myid):
    product_object = Product.objects.get(id=myid)
    return render(request, 'shop/detail.html', {'product': product_object}) 

def checkout(request):
    if request.method == "POST":
        items = request.POST.get('items')
        total = request.POST.get('total')
        nom = request.POST.get('nom')
        phone_number = request.POST.get('phone_number')
        address = request.POST.get('address')
        ville = request.POST.get('ville')
        pays = request.POST.get('pays')
        com = Commande(items=items,total=total, nom=nom, phone_number=phone_number, address=address, ville=ville, pays=pays, )
        com.save()
        return redirect('confirmation')


    return render(request, 'shop/checkout.html') 

def confimation(request):
    info = Commande.objects.all()[:1]
    for item in info:
        nom = item.nom
    return render(request, 'shop/confirmation.html', {'name': nom})          

from .models import Product  # Assurez-vous d'importer votre modèle Product






   
      