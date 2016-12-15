==========================
dsfb
==========================

Django Superb File Browser is a simple Django app to browse the server file system. 

Javascript is required.


Quick start
-----------

1. Add "dsfb" to your INSTALLED_APPS setting like this::

    INSTALLED_APPS = [
        ...
        'dsfb',
    ]

2. Include the polls URLconf in your project urls.py like this::

    url(r'^dsfb/', include('dsfb.urls')),

3. dsfb has no models, so there is no strict need to Run  `python manage.py migrate` to create the polls models.

4. Start the development server and visit http://127.0.0.1:8000/dsfb/

