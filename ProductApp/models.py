from django.db import models
from django.contrib.auth.models import User
import uuid


def img_upload(instance,filename):
    ext = filename.split('.')[-1]
    i = instance
    fn = 'media/images/{}/{}/{}/{}.{}'.format(i.user,i.category,i.name,uuid.uuid4(),ext)
    return fn
# Create your models here.
class ModelStore(models.Model):
    user = models.ForeignKey(User, related_name='user_product', on_delete=models.CASCADE)
    name = models.CharField(max_length=150)
    description = models.TextField(max_length=10000,null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    old_price = models.DecimalField(max_digits=10, decimal_places=2)
    solde = models.BooleanField(default=False)
    h_img = models.ImageField(upload_to=img_upload,null=True)
    category = models.ForeignKey("Category",related_name='prod_category', on_delete=models.CASCADE,null=True)

    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length = 50)
    def __str__(self):
        return self.name