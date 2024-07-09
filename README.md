# TechShelter Online Store Django Fullstack Website
[![Python Version](https://img.shields.io/badge/python-3.8.6-brightgreen.svg)](https://python.org)
[![Django Version](https://img.shields.io/badge/django-3.1.7-brightgreen.svg)](https://djangoproject.com)

This is a website project I worked on as the sole worker for my final year/capstone project for my BSc (Hons) degree. I used the Django (v3.1.7) framework of the programming language Python (v3.8.8) and used Django's default built-in database SQLite (v3.34.0).
The project is to build a full stack website which I named “Techshelter Online Techstore” where users can visit to see tech items and gadgets, and register as either customers or sellers to buy or sell tech items and gadgets. Only A seller-type user has the privilege to see the functionalities which facilitate selling products and only a customer-type user can see and use the options which facilitate buying products. There can also be added managers and admins who have further privileges to maintain the website and the business, which can be chosen only by an admin and can only be added from among the registered users. Admins and managers have the privilege to see many options that other users do not have.
The website has a unique design with a dark-themed ambient lighting look, which I designed from scratch using only vanilla JavaScript and CSS.



## Running the Project Locally

First, clone the repository to your local machine:

```bash
git clone https://github.com/Ihtheram/Django-Online-Store-Fullstack-Website.git
```

Activate the virtual environment:

```bash
techshelter-env/Scripts/activate
```

Install the requirements:

Install Python v3.8.6

```bash
pip install -r requirements.txt
```
```or
pip install requests
```

Apply the migrations:

```bash
python manage.py migrate
```

Finally, run the development server:

```bash
python manage.py runserver
```

The project will be available at **127.0.0.1:8000**.


## License

The source code is released under the [GNU License](https://github.com/Ihtheram/IRMTech/blob/main/LICENSE).

