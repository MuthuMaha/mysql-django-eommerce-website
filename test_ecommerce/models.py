from django.db import models

# Create your models here.
class Product(models.Model):
    name=models.CharField(max_length=100)
    img=models.ImageField(upload_to='pics')
    desc=models.TextField()
    price=models.IntegerField(default=0)
    discount_price=models.IntegerField(default=0)
    rating=models.IntegerField(default=100)
    doc=models.FileField(upload_to='docs')
    uploaded_at=models.DateTimeField(auto_now_add=True)
    flag=models.CharField(max_length=2)