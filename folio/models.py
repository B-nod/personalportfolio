from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.
class Prot(models.Model):
    fname = models.CharField(max_length=120, null=True)
    lname = models.CharField(max_length=120, null=True)
    position = models.CharField(max_length=200)
    email= models.EmailField(max_length=200)
    contact = PhoneNumberField(null=False, blank=False, unique=True, region='NP')
    address = models.CharField(max_length=200)
    dob = models.DateField()
    description = models.TextField(null=True)
    image = models.FileField(upload_to='static/uploads', null=True)
    create_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.fname
    
class Skill(models.Model):
    name = models.CharField(max_length=120, null=True)
    percentage = models.IntegerField()

    def __str__(self):
        return self.name

class Education(models.Model):
    college_name = models.CharField(max_length=200, null=True)
    college_address = models.CharField(max_length=200, null=True)
    date_frm = models.DateField()
    date_end = models.DateField()
    description = models.TextField()

    def __str__(self):
        return self.college_name
    
    
    def yearstart(self):
        return self.date_frm.strftime('%Y')
    
    def yearend(self):
        return self.date_end.strftime('%Y')

class Experience(models.Model):
    STATUS = (
        ('Available','Available'),
        ('Unavailable', 'Unavailable')
    )
    position = models.CharField(max_length=200, null=True)
    company_name = models.CharField(max_length=200, null=True)
    company_address = models.CharField(max_length=200, null=True)
    date_frm = models.DateField()
    date_end = models.DateField()
    status = models.CharField(max_length=200, choices=STATUS)

    def __str__(self):
        return self.company_name
    
class Client(models.Model):
     name = models.CharField(max_length=200, null=True)
     position = models.CharField(max_length=200, null=True)
     description = models.TextField()
     image = models.FileField(upload_to='static/uploads', null=True)

     def __str__(self):
        return self.name
     
class Project(models.Model):
    title = models.CharField(max_length=200, null=True)
    image = models.FileField(upload_to='static/uploads', null=True)
    link = models.URLField(max_length=200, null=True)
    
    def __str__(self):
        return self.title
     

class Service(models.Model):
    name = models.CharField(max_length=200)
    def __str__(self):
        return self.name
    
class Contact(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    subject = models.ForeignKey(Service, on_delete=models.CASCADE)
    message = models.TextField()

    def __str__(self):
        return self.name


    
    

      