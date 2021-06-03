#!/bin/sh
echo "Migrate the Database at startup of project"
while ! python manage.py migrate  2>&1; do
   echo "Running - DB Migration"
   sleep 3
done
python manage.py createsuperuser --no-input 2>&1 && python manage.py loaddata default || echo DB Found
echo "Django DB Setup Complete."
exec "$@"