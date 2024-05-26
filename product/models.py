from django.db import models

# Create your models here.


class Category(models.Model):
    parent = models.ForeignKey('self', blank=True,null=True,on_delete=models.CASCADE,related_name='subs')
    title = models.CharField(max_length=100)
    slug = models.SlugField()


    def __str__(self):
        return self.title

class Size(models.Model):
    title = models.CharField(max_length=10)


    def __str__(self):
        return self.title


class Color(models.Model):
    title = models.CharField(max_length=10)

    def __str__(self):
        return self.title

class product(models.Model):
    category = models.ManyToManyField(Category,blank=True)
    category_name = models.CharField(max_length=50)
    title = models.CharField(max_length=40)
    description = models.TextField()
    price = models.IntegerField()
    discount = models.SmallIntegerField()
    image = models.ImageField(upload_to="product")
    size = models.ManyToManyField(Size, related_name="products")
    color = models.ManyToManyField(Color, related_name="products")
    slug = models.SlugField()


    def __str__(self):
        return self.title



class Information(models.Model):
    Product = models.ForeignKey(product, on_delete=models.CASCADE, related_name="information")
    text = models.TextField()

    def __str__(self):
        return self.text[:30]