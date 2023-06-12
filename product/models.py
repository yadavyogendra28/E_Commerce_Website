from django.db import models
from django.contrib.auth.models import User


class product(models.Model):
    user_name= models.CharField(max_length=10)
    password=models.CharField(max_length=10)
    


class product_add(models.Model):
    img=models.ImageField(upload_to='Media')
    title=models.CharField(max_length=50)
    qnty=models.CharField(max_length=5)
    about_p=models.TextField()

# -------------------------------------------------------------------------------------------







class product_Grocery(models.Model):
    img=models.ImageField(upload_to='Media')
    title=models.CharField(max_length=50)
    Quantity=models.IntegerField()
    Price=models.IntegerField()
    about_p=models.TextField()


class product_Mobiles(models.Model):
    img=models.ImageField(upload_to='Media')
    title=models.CharField(max_length=50)
    Quantity=models.IntegerField()
    Price=models.IntegerField() 
    about_p=models.TextField()

class product_Fashion(models.Model):
    img=models.ImageField(upload_to='Media')
    title=models.CharField(max_length=50)
    Quantity=models.IntegerField()
    Price=models.IntegerField()
    about_p=models.TextField()

class product_Electronics(models.Model):
    img=models.ImageField(upload_to='Media')
    title=models.CharField(max_length=50)
    Quantity=models.IntegerField()
    Price=models.IntegerField()
    about_p=models.TextField()


class product_Home(models.Model):
    img=models.ImageField(upload_to='Media')
    title=models.CharField(max_length=50)
    Quantity=models.IntegerField()
    Price=models.IntegerField()
    about_p=models.TextField()


class Rating(models.Model):
    appuser=models.ForeignKey(User,on_delete=models.CASCADE)
    rating=models.CharField(max_length=30)
    feedback=models.CharField(max_length=30)


class product_Add_Cart(models.Model):
    user_name= models.CharField(max_length=50)
    img=models.ImageField(upload_to='Media')
    category=models.CharField(max_length=20)
    title=models.CharField(max_length=50)
    Quantity=models.IntegerField()
    Price=models.IntegerField()
    about_p=models.TextField()
    

class Address_Add(models.Model):
    user_login= models.CharField( max_length=40, primary_key=True)
    user_name=models.CharField(max_length=40)
    address=models.CharField(max_length=100)
    landmark=models.CharField(max_length=50)
    city=models.CharField(max_length=20)
    state=models.CharField(max_length=50)
    pincode=models.IntegerField()



     

  
    