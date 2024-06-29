from django.shortcuts import render,redirect
from .models import Product,Cart,Pay,ContactUs, UserMessage
from .forms import NewUserForm
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from.forms import PayForm, AddressForm, UserMessageForm
from django.contrib.auth.decorators import login_required


#---------------------------------------------------------------------------------------------------------------------------------------
# Create your views here.
# def index(request):

#     if request.method == 'POST':
#             who = request.POST.get('who')
#             current_user = User.objects.get(username=who)
#             product_name = request.POST.get('product_name')
#             product_price = request.POST.get('product_price')
#             Product.objects.create(who=current_user, name=product_name, price=product_price)
#             return redirect('index')
    
#     user_products = User.objects.all()
#     product = Product.objects.all()
#     cart = Cart.objects.all()
    
#     return render(request, 'main/index.html', context = {
#         'product':product,
#         'cart':cart,
#         'user_products':user_products


#     } )

# def cart(request):
#     quantity = 0
#     summ = 0
#     cart = Cart.objects.all()
#     for i in cart:
#         summ = i.product.price * i.quantity
#         if quantity > 0:
#             quantity += 1

#     return render(request, 'main/cart.html', context = {
#         'cart':cart,
#         'summ':summ,
#         'quantity':quantity

#     } )

# def add_to_cart(request):
#     if request.method == 'POST':
#         prod_id = request.POST.get('prod_id')
#         prod = Product.objects.get(id = prod_id)
#         cart_items, smth = Cart.objects.get_or_create(product=prod)
#         if not smth:
#             cart_items.quantity += 1
#             cart_items.save()
#         return redirect('index')

# def delete_from_cart(request):
#     if request.method == 'POST':
#         prod_id = request.POST.get('prod_id')
#         cart_items = Cart.objects.get(id=prod_id)
#         if cart_items.quantity > 1:
#             cart_items.quantity -= 1
#             cart_items.save()
#         else:
#             cart_items.delete()
#         return redirect('cart')
    

# def register_request(request):
# 	if request.method == "POST":
# 		form = NewUserForm(request.POST)
# 		if form.is_valid():
# 			user = form.save()
# 			login(request, user)
# 			messages.success(request, "Registration successful." )
# 			return redirect("index")
# 		messages.error(request, "Unsuccessful registration. Invalid information.")
# 	form = NewUserForm()
# 	return render(request=request, template_name="main/register.html", context={"register_form":form})

# def login_request(request):
# 	if request.method == "POST":
# 		form = AuthenticationForm(request, data=request.POST)
# 		if form.is_valid():
# 			username = form.cleaned_data.get('username')
# 			password = form.cleaned_data.get('password')
# 			user = authenticate(username=username, password=password)
# 			if user is not None:
# 				login(request, user)
# 				messages.info(request, f"You are now logged in as {username}.")
# 				return redirect("index")
# 			else:
# 				messages.error(request,"Invalid username or password.")
# 		else:
# 			messages.error(request,"Invalid username or password.")
# 	form = AuthenticationForm()
# 	return render(request=request, template_name="main/login.html", context={"login_form":form})

# def logout_request(request):
# 	logout(request)
# 	messages.info(request, "You have successfully logged out.") 
# 	return redirect("index")
#---------------------------------------------------------------------------------------------------------------------------------------




def index(request):
    if request.method == 'POST':
        who = request.POST.get('who')
        current_user = User.objects.get(username=who)
        product_name = request.POST.get('product_name')
        product_price = request.POST.get('product_price')
        Product.objects.create(who=current_user, name=product_name, price=product_price)
        return redirect('index')
    
    user_products = User.objects.all()
    product = Product.objects.all()
    pay = Pay.objects.first()
    if request.user.is_authenticated:
        cart_items = Cart.objects.filter(user=request.user)
    else:
        cart_items = []

    return render(request, 'main/index.html', context={
        'product': product,
        'cart': cart_items,
        'user_products': user_products,
        'pay':pay
    })

def cart(request):
    quantity = 0
    summ = 0
    if request.user.is_authenticated:
        cart_items = Cart.objects.filter(user=request.user)
        for i in cart_items:
            quantity += i.quantity
            summ += i.product.price * i.quantity
    else:
        cart_items = []
        messages.info(request, f"Login/Register first .")


    return render(request, 'main/cart.html', context={
        'cart': cart_items,
        'summ': summ,
        'quantity': quantity
    })

def add_to_cart(request):
    if request.method == 'POST':
        prod_id = request.POST.get('prod_id')
        prod = Product.objects.get(id=prod_id)
        if request.user.is_authenticated:
            cart_item, created = Cart.objects.get_or_create(user=request.user, product=prod)
            if not created:
                cart_item.quantity += 1
                cart_item.save()
        return redirect('index')

def delete_from_cart(request):
    if request.method == 'POST':
        prod_id = request.POST.get('prod_id')
        if request.user.is_authenticated:
            cart_item = Cart.objects.get(id=prod_id, user=request.user)
            if cart_item.quantity > 1:
                cart_item.quantity -= 1
                cart_item.save()
            else:
                cart_item.delete()
        return redirect('cart')

def register_request(request):
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Registration successful." )
            return redirect("index")
    else:
        form = NewUserForm()
    return render(request=request, template_name="main/register.html", context={"register_form": form})

def login_request(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"You are now logged in as {username}.")
                return redirect("index")
        messages.error(request, "Invalid username or password.")
    else:
        form = AuthenticationForm()
    return render(request=request, template_name="main/login.html", context={"login_form": form})

def logout_request(request):
    logout(request)
    messages.info(request, "You have successfully logged out.") 
    return redirect("index")



@login_required
def pay(request):
    if request.user.is_authenticated:
        quantity = 0
        summ = 0
        cart_items = Cart.objects.filter(user=request.user)
        for item in cart_items:
            quantity += item.quantity
            summ += item.product.price * item.quantity
    else:
        cart_items = []
        summ = 0
        quantity = 0

    if request.method == 'POST':
        form = PayForm(request.POST)
        if form.is_valid():
            pay = form.save(commit=False)
            pay.user = request.user
            pay.cart = Cart.objects.get(id=request.session['cart_id'])  

            pay.save()
            messages.info(request, "You have successfully paid.") 
        elif messages.error(request, "Please LogIn First."):

            return redirect('index') 
    else:
        form = PayForm()
    

    return render(request, 'main/payment.html', context = {
        'form': form,
        'summ': summ,
        'quantity': quantity
    })
#--------------------------------------------------------------------------------------------------------------------------------------

# @login_required
# def pay(request):
#     quantity = 0
#     summ = 0
#     cart_items = Cart.objects.filter(user=request.user)
#     for item in cart_items:
#         quantity += item.quantity
#         summ += item.product.price * item.quantity

#     if request.method == 'POST':
#         form = PayForm(request.POST)
#         if form.is_valid():
#             pay = form.save(commit=False)
#             pay.user = request.user
#             pay.save()
#             request.session['pay_data'] = {
#                 'name_on_card': pay.name_on_card,
#                 'card_number': pay.card_number,
#                 'expiry_date': pay.expiry_date,
#                 'cvv_code': pay.cvv_code
#             }
#             return redirect('user_details')  
#     else:
#         form = PayForm()
    
#     return render(request, 'main/payment.html', context={
#         'form': form,
#         'summ': summ,
#         'quantity': quantity
#     })


#------------------------------------------------------------------------------------------------------------------------------------



def delivery(request):
    quantity = 0
    summ = 0

    if request.user.is_authenticated:
        cart_items = Cart.objects.filter(user=request.user)
        for item in cart_items:
            quantity += item.quantity
            summ += item.product.price * item.quantity
    else:
        cart_items = []

    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        address = request.POST.get('address')
        message = request.POST.get('message')
        ContactUs.objects.create(name=name, email=email,address=address, message=message)

        return redirect('index')

    return render(request, 'main/delivery.html', context={
        'cart': cart_items,
        'summ': summ,
        'quantity': quantity
    })

#------------------------------------------------------------------------------------------------------------------------------------

# @login_required
# def enter_address(request):
#     if request.method == 'POST':
#         form = AddressForm(request.POST)
#         if form.is_valid():
#             address = request.POST.get('address')
#             phone_number = request.POST.get('number')
            
#             # Retrieve the payment data from the session
#             pay_data = request.session.get('pay_data', {})
#             if pay_data:
#                 pay = Pay.objects.create(
#                     user=request.user,
#                     cart=Cart.objects.filter(user=request.user).first(),
#                     name=pay_data['name'],
#                     card_number=pay_data['card_number'],
#                     hetevi_tver=pay_data['hetevi_tver'],
#                     phone_number=phone_number,
#                     email=pay_data['email'],
#                     address=address
#                 )
#                 # Clear the session data after saving
#                 del request.session['pay_data']
#                 messages.success(request, "Payment successful!")
#                 return redirect('index')
#     else:
#         form = AddressForm()

#     return render(request, 'main/address_after_payment.html', context={'form': form})


# def enter_address(request):
#     if request.method == "POST":
#         name = request.POST.get('name')
#         email = request.POST.get('email')
#         message = request.POST.get('message')
#         UserMessage.objects.create(name=name, email=email, message=message)
#         messages.success(request, "Details submitted successfully.")
#         return redirect('index')

#     return render(request, 'main/enter_address.html')

#--------------------------------------------------------------------------------------


def user_details(request):
    if request.method == "POST":
        form = UserMessageForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Details submitted successfully.")
            return redirect('index')
    else:
        form = UserMessageForm()
    
    return render(request, 'main/address_after_payment.html', context={'form': form})