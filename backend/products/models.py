from django.db import models

# update db
# python manage.py makemigrations
# python manage.py migrate

# create superuser
# 1 - python manage.py shell
# 2 - python manage.py createsuperuser

class Product(models.Model):
    title = models.CharField(max_length=120)
    content = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=15, decimal_places=2, default=99.99)