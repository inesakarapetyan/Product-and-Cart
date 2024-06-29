# Product-and-Cart
Django





https://github.com/inesakarapetyan/Product-and-Cart/assets/165501683/a74143f3-c33c-4d97-bbe0-d3d65fc2e180





--------------------------------------------------------------------------------------------------------------------------------------------------------
|                                                            DESCRIPTION                                                                                |
--------------------------------------------------------------------------------------------------------------------------------------------------------


This project is an advanced online store that includes product management, user authentication, a shopping cart system, and support for multiple payment options. Users must be logged in to manage their cart and place orders. The store also supports multilingual functionality, allowing users to switch between Armenian, English, and Russian.

Key Features

1.Product Management: Admins can add, update, delete, and view products with attributes such as name, description, price, and stock quantity.

2.User Authentication: Users can register, log in, and log out. Authentication is required to manage the shopping cart and place orders.

3.Shopping Cart: Users can add products to their cart in any quantity, view their cart, update quantities, and remove items.

4.Order Management: Users can place orders and choose to pay now or upon delivery. Admins can view and manage orders.

5.Multilingual Support: The store interface is available in Armenian, English, and Russian.

Detailed Components

Authentication

-User Registration: Users can create a new account by providing a username, email, and password.

-User Login: Users can log in with their username and password.

-User Logout: Logged-in users can log out of their accounts.

Product Management

-Product List: Display a list of all available products with details such as name, description, price, and stock.

-Product Detail: View detailed information about a specific product.

-Admin Controls: Admins can add new products, update existing products, and delete products.

Shopping Cart

-Add to Cart: Users can add products to their cart in any desired quantity.

-View Cart: Users can view the contents of their cart, including product details and quantities.

-Update Cart: Users can update the quantity of products in their cart.

-Remove from Cart: Users can remove products from their cart.

Order Management
-Place Order: Users can place an order for the products in their cart.

-Payment Options: Users can choose to pay for their order immediately or upon delivery.

-Order History: Users can view their past orders, including order details and status.

-Admin Controls: Admins can view and manage all orders.

-Multilingual Support


Language Selection: Users can select their preferred language (Armenian, English, or Russian) from the website interface.
Translation: The entire website content, including product details, user instructions, and messages, is available in the selected language.



------------------------------------------------------------------------------------------------------------------------------------------------------
|                                                            RUN CODE                                                                                |
------------------------------------------------------------------------------------------------------------------------------------------------------


For Windows Users

1.Open Visual Studio Code

2.Open Terminal:

Open the integrated terminal in VS Code by navigating to 'View > Terminal' or using the shortcut 'Ctrl + ~' (backtick).

3.py -m venv venv         # Create a virtual environment

4.\venv\Scripts\activate      # Activate the virtual environment

5.py -m pip install --upgrade pip    # Upgrade pip

6.pip install django    # Install Django

7.django-admin startproject myproject      # Create a Django project

8.cd myproject              # Navigate into the project directory

9.python manage.py startapp main   #Create a project

10.python manage.py runserver         # Start the Django development server

For Mac or Linux Users

1.Open Visual Studio Code

2.Open Terminal:

Open the integrated terminal in VS Code by navigating to 'View > Terminal' or using the shortcut 'Ctrl + ~' (backtick).

3.python3 -m venv venv             # Create a virtual environment

4.source ./venv/bin/activate            # Activate the virtual environment

5.python3 -m pip install --upgrade pip    # Upgrade pip

6.pip install django         # Install Django

7.django-admin startproject myproject     # Create a Django project

8.cd myproject              # Navigate into the project directory

9.python3 manage.py startapp main   #Create a project

10.python3 manage.py runserver         # Start the Django development server
