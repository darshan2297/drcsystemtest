from django.shortcuts import render,redirect
from django.views import View
from rest_app.models import UserProfile, EmailRecords
from hashutils import make_pw_hash, check_pw_hash
import pyotp
from django.http import HttpResponse

# Create your views here.

# Create your views here.
def generateOTP():
    activation_key = pyotp.random_base32()
    totp = pyotp.TOTP(activation_key,interval=86400)
    print(totp.now())
    otp = totp.now()
    return {'activation_key':activation_key,"otp":otp}

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
        if not (emailObj:= EmailRecords.objects.filter(email=email,is_deleted=False).first()):
            return HttpResponse("User not found")
        
        if getUserObj:= UserProfile.objects.filter(id=emailObj.user_id,is_deleted=False).first():
            otpObj = generateOTP()
            getUserObj.otp = otpObj["otp"]
            getUserObj.activation_key = otpObj["activation_key"]
            getUserObj.save()
            return redirect("restapp:otpview")
        else:
            return HttpResponse("User not found")

class OTPView(View):
    
    def get(self, request, *args, **kwargs):
        return render(request,'otpenter.html')
    
    def post(self, request, *args, **kwargs):
        otp= request.POST['otp']
        if getUserObj := UserProfile.objects.filter(otp=otp,is_deleted=False).first():
            activation_key = getUserObj.activation_key
            totp = pyotp.TOTP(activation_key, interval=86400)
            print(totp)
            verify = totp.verify(totp.now())
            if verify:
                user_data = {}
                user_data['id'] = getUserObj.id
                user_data['username'] = getUserObj.username
                request.session['user'] = user_data
                return redirect("restapp:home")
        else:
           return HttpResponse("User not found") 

class HomeView(View):
    
    def get(self, request, *args, **kwargs):
        userData = request.session.get('user')['username']
        return HttpResponse(f"Home Page {userData}")