from django.shortcuts import render,redirect, get_object_or_404
from django.contrib import messages
from .models import Feedback, Product, Category, Review

# Create your views here.
def index(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    products = Product.objects.filter(available=True)[:4]
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)

    context={
        'category': category,
        'categories': categories,
        'products': products,
    }
    return render(request, 'index.html', context)

def about_us(request):
    return render(request, 'about-us.html')

def contact(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        feedback = request.POST['feedback']

        if len(feedback) < 15:
            messages.warning(request, "Feedback length should be greator than 15 charactors")
            return redirect('contact')
        
        feed = Feedback.objects.create(
            name = name,
            email = email,
            feedback = feedback
        )
        feed.save()

        #print(f"\n\n {name} \n\n {email} \n\n {feedback} \n\n")
        messages.success(request,"Feedback sent successfully")
        return redirect('/')

    return render(request,"contact-page.html")

def product(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    products = Product.objects.filter(available=True)
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)

    context={
        'category': category,
        'categories': categories,
        'products': products,
    }
    return render(request, 'product/list.html',context)

def product_detail(request, id, slug):
    product = get_object_or_404(Product,id=id,slug=slug,available=True)
    return render(request,'product/detail.html',{'product': product})


def accounts(request):
    return render(request, 'accounts.html')