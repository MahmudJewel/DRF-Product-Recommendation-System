# API for Product Recommendation System
# Requirements ==> 
The project will have following features-
* You need to create three types of users: admins, vendors, and customers.
* Weather conditions can be categorized into normal, hot, and cold.
* You need to make multiple APIs for these users.
* All users should be able to log in to the system using email & password through API. Use JWT token for authentication.
* Ensure you use the proper HTTP methods and codes while writing these APIs.
* You can use any free Weather API for this project. OpenWeather is a free weather API that you can use or you can use other free weather APIs too. Ensure you provide the required API keys and instructions on the project's Readme.md file.

## Requirements for vendors:
* Vendors should be able to CRUD(Create, Read, Update, Delete) products with the quantity of the product.

## Requirements for admins:
* Admin should be able to CRUD product types. For example normal, hot, cold.
* Admin should be able to CRUD weather types. For example normal, hot, cold.
* Admin should be able to set the temperature range(high, low) for each weather type.

## Requirements for customers:
* Customers should be able to see all the products.
* Customers should be able to see product recommendations depending on the current weather condition grabbed from the weather API. For example, If the temperature is in the normal range, the user will be recommended the normal weather clothes.
* Customers should be able to search for products using the product's name or weather type.

** Write REST APIs to expose the information.
** Write test cases to test your code.


# Developed API
### Login & verify user
| SRL | METHOD | ROUTE | FUNCTIONALITY |ACCESS|
| ------- | ------- | ----- | ------------- | ------------- |
| *1* | *POST* | ```/api/token/``` | _Login user_| _All users_|
| *2* | *POST* | ```/api/token/refresh/``` | _Refresh the access token_|_All users_|
| *3* | *POST* | ```/api/token/verify/``` | _Verify the validity of a token_|_All users_|

### Customer Related API 
| SRL | METHOD | ROUTE | FUNCTIONALITY |ACCESS|
| ------- | ------- | ----- | ------------- | ------------- |
| *4* | *POST* | ```/api/auth/customer/``` | _Register new customer_|_Allow any_|
| *5* | *GET* | ```/api/auth/customer/``` | _List all customer_|_Adminuser_|
| *6* | *PUT* | ```/api/auth/customer/uid/``` | _Update customer_|_Adminuser_|
| *7* | *DELETE* | ```/api/auth/customer/uid/``` | _Delete customer_|_Adminuser_|

### Vendor Related API 
| SRL | METHOD | ROUTE | FUNCTIONALITY |ACCESS|
| ------- | ------- | ----- | ------------- | ------------- |
| *8* | *POST* | ```/api/auth/vendor/``` | _Register new vendor_|_Allow any_|
| *9* | *GET* | ```/api/auth/vendor/``` | _List all vendor_|_Adminuser_|
| *10* | *PUT* | ```/api/auth/vendor/uid/``` | _Update vendor_|_Adminuser_|
| *11* | *DELETE* | ```/api/auth/vendor/uid/``` | _Delete vendor_|_Adminuser_|

### Weather Related API 
| SRL | METHOD | ROUTE | FUNCTIONALITY |ACCESS|
| ------- | ------- | ----- | ------------- | ------------- |
| *12* | *POST* | ```/api/weather/``` | _Add new weather type_|_Adminuser_|
| *13* | *GET* | ```/api/weather/``` | _List all weather type_|_Adminuser_|
| *14* | *PUT* | ```/api/weather/id/``` | _Edit weather type_|_Adminuser_|
| *15* | *DELETE* | ```/api/weather/id/``` | _Delete weather type_|_Adminuser_|
| *16* | *PATCH* | ```/api/weather/id/``` | _Update high and low temperature_|_Adminuser_|

### Product Related API 
| SRL | METHOD | ROUTE | FUNCTIONALITY |ACCESS|
| ------- | ------- | ----- | ------------- | ------------- |
| *17* | *GET* | ```/api/product/``` | _All product list_|_Any user_|
| *18* | *POST* | ```/api/product/``` | _Add new product_|_vendor_|
| *19* | *PUT* | ```/api/product/pid/``` | _Edit product_|_vendor_|
| *20* | *DELETE* | ```/api/product/pid/``` | _Delete  product_|_vendor_|
| *21* | *GET* | ```/api/search/?search=text``` | _Search product according to product title or weather type_|_Any user_|
| *22* | *PATCH* | ```/api/product/id/``` | _Update product type_|_Adminuser_|
| *23* | *GET* | ```/api/recommendation/?location=city_name``` | _Product recommendation_|_Any one_|


# Tools
### Back-end
#### Language:
	Python (3.9.0)

#### Frameworks:
	Django(4.1.1)
	django rest framework (3.13.1 )
	
#### Other libraries / tools:
	asgiref                       3.5.2
	autopep8                      1.7.0
	certifi                       2022.6.15
	cffi                          1.15.1
	charset-normalizer            2.1.1
	coreapi                       2.3.3
	coreschema                    0.0.4
	cryptography                  38.0.1
	defusedxml                    0.7.1
	django-templated-mail         1.1.1
	djangorestframework-simplejwt 5.2.0
	djoser                        2.1.0
	idna                          3.3
	itypes                        1.2.0
	Jinja2                        3.1.2
	MarkupSafe                    2.1.1
	mysqlclient                   2.1.1
	oauthlib                      3.2.0
	Pillow                        9.2.0
	pip                           20.2.3
	pycodestyle                   2.9.1
	pycparser                     2.21
	PyJWT                         2.4.0
	python-dotenv                 0.21.0
	python3-openid                3.2.0
	pytz                          2022.2.1
	requests                      2.28.1
	requests-oauthlib             1.3.1
	setuptools                    49.2.1
	six                           1.16.0
	social-auth-app-django        4.0.0
	social-auth-core              4.3.0
	sqlparse                      0.4.2
	toml                          0.10.2
	uritemplate                   4.1.1
	urllib3                       1.26.12

	
### Database:
	MySQL

# Setup
The first thing to do is to clone the repository:
```sh
$ https://github.com/MahmudJewel/API-ecommerce_for_mktech
```
### Back-end
Create a virtual environment to install dependencies in and activate it:
```sh
$ cd API-ecommerce_for_mktech
$ python -m venv venv
$ source venv/bin/activate
```
Then install the dependencies:
```sh
(venv)$ pip install -r requirements.txt
```
Note the `(venv)` in front of the prompt. This indicates that this terminal
session operates in a virtual environment set up by `virtualenv2`.

Once `pip` has finished downloading the dependencies:
```sh
(venv)$ python manage.py migrate
(venv)$ python manage.py runserver 8000
```

# Happy Coding
## From ==> Juwel Mahmud

