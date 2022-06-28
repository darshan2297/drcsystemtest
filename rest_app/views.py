from django.shortcuts import render,redirect
from django.views import View
from rest_app.models import UserProfile, EmailRecords
from hashutils import make_pw_hash, check_pw_hash
import pyotp


# Create your views here.

# Create your views here.
def generateOTP():
    random32 = pyotp.random_base32()
    totp = pyotp.TOTP(random32,interval=600)
    print(totp.now())
    return totp.now()

class RegisterView(View):
    
    def get(self, request, *args, **kwargs):
        return render(request,"Register.html")
    
    def post(self, request, *args, **kwargs):
        email = request.POST['email']
        username = request.POST['username']
        mobile = request.POST['mobile']
        password = request.POST['password']
        enc_password = make_pw_hash(password)

        userObj = UserProfile.objects.create(username=username,mobile=mobile,password=enc_password)
        
        EmailRecords.objects.create(user_id=userObj.id,email=email)
        
        return redirect("restapp:login")

class LoginView(View):
    
    def get(self, request, *args, **kwargs):
        return render(request,'Login.html')
    
    def post(self, request, *args, **kwargs):
        email = request.POST['email']
        
class OTPView(View):
    
    def get(self, request, *args, **kwargs):
        generateOTP()
        return render(request,'')
        
        
        
        