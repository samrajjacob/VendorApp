# VendorApp
Developed a Vendor Management System using Django and Django REST Framework. This system will handle vendor profiles, track purchase orders, and calculate vendor performance metrics
## Getting Started
### Prerequisites

- Python 3.10.7
- Git (for cloning the repository)

  
### **Libraries Used**

- **Djangorestframework-simplejwt**: This library is an extension of Django REST framework (DRF) that provides JSON Web Token (JWT) authentication. JWTs are a secure way to transmit information between parties, and they are commonly used for authentication in web applications. `djangorestframework-simplejwt` simplifies the integration of JWT authentication into Django REST framework.

- **Django**: Django is a high-level Python web framework that encourages rapid development and clean, pragmatic design. It follows the Model-View-Controller (MVC) architectural pattern and includes an Object-Relational Mapping (ORM) system for database interactions. In your project, Django serves as the foundation for building web applications.

- **Djangorestframework**: Django REST framework (DRF) is a powerful and flexible toolkit for building Web APIs in Django applications. It is an extension of Django that makes it easy to build, test, and deploy RESTful APIs. DRF includes serializers for data handling, class-based views for defining API endpoints, and authentication mechanisms. It simplifies the process of building robust and scalable APIs.

  
### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/samrajjacob/VendorApp.git
   
2. Create the environment:

   ```bash
   py -m venv venv
   
3. Activate the environnment:
   
      ```bash
     .\venv\Scripts\activate
  
3. Install the requirements:

   ```bash
   pip install -r requirements.txt
   
4. Run Migrations:

   ```bash
   python manage.py makemigrations
   
   python manage.py migrate
   
6. Run the code:

   ```bash
   python manage.py runserver
   
