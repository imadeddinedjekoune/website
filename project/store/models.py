from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Subcategory(models.Model):
    name = models.CharField(max_length=100)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    subcategory = models.ForeignKey(Subcategory, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image_0 = models.ImageField(upload_to='products/images/list/')
    image_1 = models.ImageField(upload_to='products/images/list/')
    image_2 = models.ImageField(upload_to='products/images/list/')
    image_3 = models.ImageField(upload_to='products/images/list/',blank=True, null=True)
    image_4 = models.ImageField(upload_to='products/images/list/',blank=True, null=True)
    image_5 = models.ImageField(upload_to='products/images/list/',blank=True, null=True)
    image_6 = models.ImageField(upload_to='products/images/list/',blank=True, null=True)
    image_7 = models.ImageField(upload_to='products/images/list/',blank=True, null=True)
    image_8 = models.ImageField(upload_to='products/images/list/',blank=True, null=True)
    image_9 = models.ImageField(upload_to='products/images/list/',blank=True, null=True)
    image_10 = models.ImageField(upload_to='products/images/list/',blank=True, null=True)
    new = models.BooleanField(default = False)
    promotion = models.PositiveIntegerField(null=True,blank=True,default=0)
    promotion_prix = models.FloatField(blank=True,null=True,default=0)
    small_description = models.TextField(blank=True)
    desc_specifications = models.TextField(blank=True)

    def __str__(self):
        return self.name

class ScaledImage(models.Model):
    original_image = models.ForeignKey(Product, on_delete=models.CASCADE)
    scaled_image_100x100 = models.ImageField(upload_to='scaled_images_100x100/',default="")
    scaled_image_510xH = models.ImageField(upload_to='scaled_images_510xH/',default="")
    scaled_image_247x296 = models.ImageField(upload_to='scaled_images_247x296/',default="")


class Promotion(models.Model):
    promo = models.DateTimeField()


class Product_Page_Left(models.Model):
    product = models.ForeignKey(Product, on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.product.name

class Product_Page_Down(models.Model):
    product = models.ForeignKey(Product, on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.product.name

class Index_Page_UP(models.Model):
    product = models.ForeignKey(Product, on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.product.name

class Wilaya(models.Model):
    name = models.CharField(max_length=200)
    price_livraison_domicile = models.FloatField(default=0)
    price_livraison_desk = models.FloatField(default=0)

    def __str__(self):
        return self.name

class Commune(models.Model):
    name = models.CharField(max_length=200)
    wilaya = models.ForeignKey(Wilaya, on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.name


class Client(models.Model):
    fname = models.CharField(max_length=200)
    lname = models.CharField(max_length=200)
    wilaya = models.CharField(max_length=200)
    commune = models.CharField(max_length=200)
    adresse = models.CharField(max_length=200)
    phone = models.CharField(max_length=200)
    produit = models.CharField(max_length=200,blank=True)
    qte = models.CharField(max_length=200,blank=True)
    prix = models.CharField(max_length=200,blank=True)


    
    def __str__(self):
        return "{0} {1}".format(self.fname,self.lname)
