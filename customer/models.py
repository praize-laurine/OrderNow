from django.db import models

# Create your models here.
class MenuItem(models.Model):
    name = models.CharField(max_length = 100)
    description = models.TextField()
    image = models.ImageField(upload_to = 'images/', default = 'image.jpeg')
    price = models.DecimalField(max_digits = 5, decimal_places = 2)
    category = models.ManyToManyField('category', related_name = 'item')
    
    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length = 100)

    def __str__(self):
        return self.name  

class OrderModel(models.Model):
    created_on = models.DateTimeField(auto_now_add = True)
    price = models.DecimalField(max_digits= 7, decimal_places = 2)
    items = models.ManyToManyField('MenuItem', related_name = 'Order', blank = True)
    name = models.CharField(max_length = 50, blank = True)
    email = models.CharField(max_length = 50, blank = True)
    street = models.CharField(max_length = 50, blank = True)
    city = models.CharField(max_length = 50, blank = True)
    state = models.CharField(max_length = 15, blank = True)
    zip_code = models.IntegerField(blank = True, null = True)
    is_paid = models.BooleanField(default = False)
    def __str__(self):
        return f'Order:{self.created_on.strftime("%b %d %I: %M %p")}'

class Image(models.Model):
    name = models.CharField(max_length =60)
    description = models.CharField(max_length =200)
    Images_image = models.ImageField(upload_to = 'images/')

    

    
    def save_image(self):
        self.save()
    
    def delete_image(self):
        self.dele
        
    @classmethod
    def update_image(cls, id, value):
        cls.objects.filter(id=id).update(image=value)
    
    @classmethod
    def get_image_by_id(cls, id):
        image = cls.objects.filter(id=id).all()
        return image 
     
     
   
     
     
    
  
    def __str__(self):
        return self.name        



