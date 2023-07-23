from django.db import models
import re



class UserManager(models.Manager):
    def regValidator(self, postData):
        errors = {}
        if len(postData['username']) < 2:
            errors['username'] = "First Name should atleast be 2 charecters"
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        if not EMAIL_REGEX.match(postData['email']):    # test whether a field matches the pattern            
            errors['email'] = "Invalid email address!"
        if User.objects.filter(email=postData['email']).exists():
            errors['email'] = "This email is already registered!"
        if len(postData['password'] or postData['password_conf']) < 8:
            errors['password_len'] = "Password should atleast be 8 charecters"
        if postData['password'] != postData['password_conf']:
            errors['password_match'] = "Passwords do not match"
        return errors 

    def loginValidator(self, postData):
        errors = {}  
        if not (User.objects.filter(email=postData['email2']) and User.objects.filter(password=postData['password2'])):
            errors['login'] = "Login failed! Check email and password"
        return errors 
    
    def addValidator(self, postData):
        errors = {}
        if len(postData['name']) < 1:
            errors['name'] = "Name is required"
        if len(postData['model']) < 1:
            errors['model'] = "Model is required"
        elif not postData['model'].isdigit():
            errors['model'] = "Model must be a number"
        if len(postData['color']) < 1:
            errors['color'] = "Color is required"
        if len(postData['fuelType']) < 1:
            errors['fuelType'] = "Fuel Type is required"
        if len(postData['price']) < 1:
            errors['price'] = "Price is required"
        elif not postData['price'].isdigit():
            errors['price'] = "Price must be a number"
        return errors 
    
    def editValidator(self, postData):
        errors = {}
        if len(postData['name']) < 1:
            errors['name'] = "Name is required"
        if len(postData['model']) < 1:
            errors['model'] = "Model is required"
        elif not postData['model'].isdigit():
            errors['model'] = "Model must be a number"
        if len(postData['color']) < 1:
            errors['color'] = "Color is required"
        if len(postData['fuelType']) < 1:
            errors['fuelType'] = "Fuel Type is required"
        if len(postData['price']) < 1:
            errors['price'] = "Price is required"
        elif not postData['price'].isdigit():
            errors['price'] = "Price must be a number"
        return errors 


class User(models.Model):
    username = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    isAdmin = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()   
    
class Car(models.Model): 
    name = models.CharField(max_length=255)
    model = models.CharField(max_length=255)
    color = models.CharField(max_length=255)
    fuelType = models.CharField(max_length=255)
    price = models.IntegerField()
    user = models.ForeignKey(User, related_name="users", on_delete = models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True) 
    objects = UserManager()