# Nutricare-Ai
NutriCare AI is a web application that provides nutrition-related services, connecting dietitians and patients to help achieve their fitness and health goals. This document will give an overview of the app's features, target audience, and functionality.

## Contributors

- **Team Members:** Abdullah Hassan

## Tools used:
      1) Programming Language and Libraries: Django (Python web framework), Bootstrap, JavaScript, Ajax, Django REST framework.
      2) Database: SQLite
      3) APIs used: MailTrap, SSLCommerz Payment Gateway, , Django PDF library, Django channels for chat, ngrok HTTP, PyPI packages.

## Features

### 1. Dietitian Registration and Online Consultation

- **Registration:** Dietitians can register on the platform by providing detailed information such as academic records and verification documents (HEC and ACEND).
- **Consultation:** Once approved by the admin, dietitians can offer online consultations through chat and video conferencing.
- **Prescriptions and Tests:** Dietitians can provide prescriptions and perform necessary tests.

### 2. Patient Registration and Interaction

- **Registration:** Patients can register and log in to the platform.
- **Booking:** Patients can view the list of available dietitians and book consultations based on their preferred time slots.
- **Chat and Video Conferencing:** Patients can communicate with dietitians through chat and video calls.

### 3. AI Dietitian "Dr. Ally"

- **Virtual Assistance:** Dr. Ally is a virtual dietitian that provides free assistance to patients, helping them achieve their fitness goals and answering their queries.
- **User Experience:** Dr. Ally is designed to be sweet and kind, enhancing user interaction.

### 4. Diet Plans

- **Premium Plans:** The platform offers premium diet plans designed by experienced dietitians.
- **Personalization:** These plans cater to various dietary needs and health goals.

### 5. Supplement Store

- **Health Supplements:** Patients can buy health supplements and vitamins at affordable prices.
- **Convenience:** The store aims to provide easy access to essential supplements.

### 6. Nutrient Check

- **Food Analysis:** Users can check the nutrient content in food based on a 100-gram quantity.
- **Health Tracking:** This feature helps users keep track of their nutrient intake.

### 7. Health Records Management

- **Patient Records:** Patients can manage their health records and history on the platform.
- **Data Security:** The platform ensures the security and privacy of patient data.

### 8. Payment System

- **Card Payment:** The platform offers a card payment system, currently in test mode.
- **Future Availability:** Payments cannot be made at the moment, but this feature will be available soon.

## How It Works

### Dashboards

### 1. Patient Dashboard

- **User Interface:** Patients can easily navigate through the platform, view available dietitians, book consultations, and manage their health records.

### 2. Doctor Dashboard

- **Registration:** Dietitians register on the platform by providing detailed information.
- **Approval Process:** The admin reviews the information and approves the registration.
- **Consultation Management:** Dietitians can accept or reject patient consultation requests and define their consultation fees (currently fixed at 1000 rupees).
- **Additional Features:** Various other features are available to enhance the dietitian's experience on the platform.

### 3. Admin Dashboard

- **Full Access:** The admin has complete access to the platform.
- **Management:** The admin can manage doctor and patient profiles, approve or disapprove doctor requests, and oversee the overall functionality of the platform.

## Conclusion

NutriCare AI aims to provide a comprehensive solution for dietitians and patients, facilitating easy and effective nutrition-related services. By leveraging technology, the platform ensures a seamless connection between dietitians and patients, helping them achieve their health and fitness goals efficiently.
## APIs and PyPI packages used:

#### [Django Rest Framework](https://www.django-rest-framework.org/#installation) - toolkit for building web APIs
#### [Django Widget Tweaks](https://pypi.org/project/django-widget-tweaks/) - tweak form field rendering in templates
#### [Pillow](https://pillow.readthedocs.io/en/stable/index.html) - Python imaging library
#### [Mailtrap API](https://mailtrap.io/blog/django-send-email/) - smtp fake testing server
#### [Django Environ](https://django-environ.readthedocs.io/en/latest/) - protecting credentials online (.env file)
#### [SSLCommerz API](https://github.com/sslcommerz/SSLCommerz-Python) - a payment gateway that provides various payment options in Bangladesh (debit card, credit card, mobile banking, etc.)
#### [Django Debug Toolbar](https://django-debug-toolbar.readthedocs.io/en/latest/installation.html) - configurable set of panels that display various debug information about the current request/response and when clicked
#### [xhtml2pdf](https://xhtml2pdf.readthedocs.io/en/latest/usage.html) - to generate and download pdf documents.

## Installation Details
      1) Create an environment to run django project  
      2) Migrate to create dbsqlite database 
      3) Look for .env.example and settings.py files to see what credentials to set up, and then create .env files
      
      The credentials that you need to set up are: Mailtrap credentials, SSLCommerz Credentials. 

## Steps to start the app
      1) Start python virtual env
            python -m venv venv
      2) Activate the virtual environment venv
            source venv/bin/activate
      3) Install python pip paclages
            pip install -r requirements
      4) Create .env from  .env.example and add secret key
            cp .env.example .env
      5) Upgrade django framework
            pip install --upgrade djangorestframework-simplejwt
      6) Migrate DB 
            python manage.py migrate
      7) Start the application
            python manage.py runserver
            
