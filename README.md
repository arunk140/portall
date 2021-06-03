## Portall - Homepage/New Tab Page for your Favorite Sites

### A simple Django App to manage shortcuts to all your favorite website.

---

Deploy using Docker -
 - Git clone this Repository
 - Edit the dash/.env file for the following Enviorment Variables
 
    - DEBUG
    - SECRET_KEY
    - DJANGO_ALLOWED_HOSTS
    - DJANGO_SUPERUSER_EMAIL
    - DJANGO_SUPERUSER_USERNAME
    - DJANGO_SUPERUSER_PASSWORD

 - The Enviorment Variables DJANGO_SUPERUSER_PASSWORD and DJANGO_SUPERUSER_USERNAME will be used to login to the Admin panel.

 - Run `docker-compose up -d` to run the service.
 - By default the Site runs on Port 8090 (Can be edited in the docker-compose.yml)
 - Go to `localhost:8090` to view the site
 - Go to `localhost:8090/admin` to configure the Shortcuts, edit the Site Title/Logo/Default Search Engine and Create/Edit User Accounts.
 