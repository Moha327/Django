from django.db import models
    
class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email_address = models.CharField(max_length=255)
    age = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
def show_db():
    return User.objects.all()

def add_to_db(first_name,last_name,email_address,age):
    return User.objects.create(first_name=first_name,last_name=last_name,email_address=email_address,age=age)