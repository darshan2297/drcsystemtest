from django.db import models
from django.contrib.auth.models import User
from datetime import datetime,timezone
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.conf import settings
from django.core.mail import send_mail
from django.core.mail import EmailMultiAlternatives
from django.template.loader import get_template
from django.template.loader import render_to_string

# Create your models here.
class UserProfile(models.Model):
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=25,null=False, blank=False,default="",unique=True)
    mobile = models.CharField(max_length=15,null=False, blank=False,default="")
    password = models.CharField(max_length=100,null=False, blank=False,default="")
    otp = models.IntegerField(null=False, blank=False, default=None)
    activation_key = models.CharField(max_length=70,null=True, blank=True,default="")
    createAt = models.DateTimeField(auto_now_add=True)
    updateAt = models.DateTimeField(auto_now=True)
    deleteAt = models.DateTimeField(null=True, blank=True)
    is_deleted = models.BooleanField(default=False)
    
    def __str__(self):
        return f'{self.id}) {self.username}'
    
    def softDelete(self):
        self.is_deleted = True
        self.deleted = datetime.now(timezone.utc)
        self.save()
        
    # Signal create new user profile after create user
@receiver(post_save, sender=UserProfile)
def emailsend(sender,instance , created, **kwargs):
    #email
    # obj = EmailRecords.objects.filter(user_id=instance.id)
    # subject = "Congrats on your Rgistration Successfull.🥳"
    msg =f"""
    Dear, {instance.username}
    
        Congrats on your Rgistration Successfull.🥳
        
    Thanks.
    """
    print(msg)
    # send_mail(subject,msg,
    #     settings.EMAIL_HOST_USER,
    #     [obj.email],
    # )

class EmailRecords(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(UserProfile,on_delete=models.CASCADE)
    email = models.EmailField(max_length=150,null=False,blank=False,default="")
    is_primary_email = models.BooleanField(default=False)
    createAt = models.DateTimeField(auto_now_add=True)
    updateAt = models.DateTimeField(auto_now=True)
    deleteAt = models.DateTimeField(null=True, blank=True)
    is_deleted = models.BooleanField(default=False)
    
    def softDelete(self):
        self.is_deleted = True
        self.deleted = datetime.now(timezone.utc)
        self.save()