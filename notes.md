# Part 1
- Download django: pip instll django
- Check django version: python -m django --version
- Create project: django-admin startproject NAME
- Run server: python manage.py runserver

# Part 2
- A project can have multiple apps
- An app is like a page
- The urls direct through the main 'urls.py' file then will match it and forward them to the according app urls.py

# Part 3
- Designing a html from scratch will make the code unreadable and messy.
- Create a template and a template directory in the specific app  folder. 

# Part 4
- python manage.py makemigrations ~ Makes changes and prepares django to update the database
- python manage.py migrate
- Start on admin page

# Part 5
- Object Relational Mapping (ORM) - Models
- python manage.py makemigrations
- To view SQL: python manage.py sqlmigrate blog 0001
- python manage.py migrate
- Migrations are useful as it allows us to update our database strucure without affecting the database filled with data.
- python manage.py shell