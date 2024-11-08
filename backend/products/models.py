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

    @property
    def sale_price(self):
        discounted_price = float(self.price) * 0.8
        formatted_price = "%.2f" % discounted_price
        return formatted_price
    
    # sample
    def get_discount(self):
        return "122"