from django.db import models

class Dojo(models.Model):
    name = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    state = models.CharField(max_length=2)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
class Ninja(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    dojo = models.ForeignKey(Dojo, related_name="ninjas", on_delete = models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

def show_dojos():
    return Dojo.objects.all()

def add_dojo(dojo_name,dojo_city,dojo_state):
    Dojo.objects.create(name=dojo_name,city=dojo_city,state=dojo_state)

def add_ninja(ninja_select_dojo,ninja_first_name,ninja_last_name):
    Ninja.objects.create(dojo=Dojo.objects.get(name=ninja_select_dojo),first_name=ninja_first_name,last_name=ninja_last_name)

def Delete(ID):
    Dojo.objects.get(id=ID).delete()