==========================
django-sfb
==========================

Superb File Browser is a simple Django app to browse the server file system. 


Quick start
-----------

1. Add "sfb-sfb" to your INSTALLED_APPS setting like this::

    INSTALLED_APPS = [
        ...
        'sfb',
    ]

2. Include the polls URLconf in your project urls.py like this::

    url(r'^sfb/', include('sfb.urls')),

3. sfb has no models, so there is no strict need to Run  `python manage.py migrate` to create the polls models.

4. Start the development server and visit http://127.0.0.1:8000/sfb/

