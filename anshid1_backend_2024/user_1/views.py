from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from user_1.models import Registration,Docters,Staffs,Patients,Bookings
from django.contrib.auth.hashers import make_password,check_password
from django.views.decorators.csrf import csrf_exempt
from .serializer import registerserializer
from django.contrib.auth import login,logout,authenticate
from django.middleware.csrf import get_token
# Create your views here.   

def get_csrf_token(request):
    csrf_token=get_token(request)
    return JsonResponse({"csrftoken":csrf_token})

@csrf_exempt
def registerform(request):
    if request.method == 'POST':
        Name = request.POST.get('name')
        User_name = request.POST.get('username')
        Category = request.POST.get('category')        
        Email = request.POST.get('email')
        Phone = request.POST.get('phone')
        Password = request.POST.get('password')
        if Registration.objects.filter(USER_NAME=User_name).exists():
            return JsonResponse({'error':'user name already exists'})
        else:
            if Category == 'Doctor':
                Docters.objects.create(NAME=Name,USER_NAME=User_name,CATAGORY=Category,EMAIL=Email,PHONE=Phone)
                Registration.objects.create(NAME=Name,USER_NAME=User_name,CATAGORY=Category,EMAIL=Email,PHONE=Phone,PASSWORD=make_password(Password))
            elif Category == 'Staff':
                Staffs.objects.create(NAME=Name,USER_NAME=User_name,CATAGORY=Category,EMAIL=Email,PHONE=Phone)
                Registration.objects.create(NAME=Name,USER_NAME=User_name,CATAGORY=Category,EMAIL=Email,PHONE=Phone,PASSWORD=make_password(Password))
            else:
                Patients.objects.create(NAME=Name,USER_NAME=User_name,CATAGORY=Category,EMAIL=Email,PHONE=Phone)
                Registration.objects.create(NAME=Name,USER_NAME=User_name,CATAGORY=Category,EMAIL=Email,PHONE=Phone,PASSWORD=make_password(Password))
                
            return JsonResponse({'status':'REGISTRATION SUCCESS'})
    else:
        return JsonResponse({'error':'no data'})
    
# @csrf_exempt    
def Login(request):
    if request.method=='POST':
        User_name = request.POST.get('username')
        Password = request.POST.get('password')
        if request.session.get('user_id'):
            return JsonResponse({
                'message':'USER ALREADY LOGGED IN',
                'status':'success',
                'username':request.session.get('username')
            })
        if Registration.objects.filter(USER_NAME = User_name).exists():
            user = Registration.objects.get(USER_NAME = User_name)
            if User_name==user.USER_NAME and check_password(Password , user.PASSWORD):
                response= JsonResponse({'status':'LOGIN SUCCESS'})
                response.set_cookie('login_cookie','cookie_value',max_age=3600)
                
                request.session['username']=user.USER_NAME
                request.session['user_id']=user.id
                
                csrf_token = get_token(request)
                response.set_cookie('csrftoken',csrf_token)
                return response
            else:
                return JsonResponse({'error':'INCORRECT PASSWORD'})
        else:
            return JsonResponse({'error':'USER NOT FOUND'})
    else:
        return JsonResponse({'error':'NO DATA'})
    
# @csrf_exempt
def logouts(request):
    logout(request)
    response = JsonResponse({'message':'logout'})
    response.delete_cookie('login_cookie')
    response.delete_cookie('csrftoken')
    return response
@csrf_exempt
def displaydetailes(request):
    if request.method == 'POST':
        User_Name = request.POST.get('username')
        if Registration.objects.filter(USER_NAME=User_Name).exists():
            userr=Registration.objects.get(USER_NAME=User_Name)
            serializer = registerserializer(userr)
            return JsonResponse({'status':'success','data': serializer.data})
        else:
            return JsonResponse({'error':'USER NOT FOUND'})
    else:
        return JsonResponse({'error':'NO DATA'})
    
@csrf_exempt
def updatedetails(request):
    if request.method == 'POST':
        Username = request.POST.get('username')
        Name = request.POST.get('name')
        Category = request.POST.get('category') 
        Email = request.POST.get('email')
        Phone = request.POST.get('phone')       
        if Registration.objects.filter(USER_NAME=Username).exists():         
            data = Registration.objects.get(USER_NAME=Username)
            data.NAME = Name
            data.EMAIL = Email
            data.PHONE = Phone
            data.save()
            if Category == 'Docter':
                Docters.objects.update(NAME=Name,EMAIL=Email, PHONE=Phone)
            elif Category == 'Staff':
                Staffs.objects.update(NAME=Name,EMAIL=Email, PHONE=Phone)
            elif Category == 'Patient':
                Patients.objects.update(NAME=Name,EMAIL=Email,PHONE=Phone)      
            return JsonResponse({'status': 'UPDATED YOUR DATA'})
        else:
            return JsonResponse({'error': 'USER NOT FOUND'})
    else:
        return JsonResponse({'error': 'NO DATA'})
    
@csrf_exempt
def deletedetails(request):
    if request.method == 'POST':
        Username = request.POST.get('username')
        if Registration.objects.filter(USER_NAME=Username).exists():
            data = Registration.objects.get(USER_NAME=Username)
            category = data.CATAGORY
            if category == 'Docter':
                Docters.objects.get(USER_NAME=Username).delete()
                Registration.objects.get(USER_NAME=Username).delete()
                return JsonResponse({'status':'SUCCESSFULLY DELETED YOUR DATAS'})
            elif category == 'Staff':
                Staffs.objects.get(USER_NAME=Username).delete()
                Registration.objects.get(USER_NAME=Username).delete()
                return JsonResponse({'status':'SUCCESSFULLY DELETED YOUR DATAS'})
            elif category == 'Patient':
                Patients.objects.get(USER_NAME=Username).delete()
                Registration.objects.get(USER_NAME=Username).delete()
                return JsonResponse({'status':'SUCCESSFULLY DELETED YOUR DATAS'})
            else:
                return JsonResponse({'status':'INVALID CATEGORY'})
        else:
            return JsonResponse({'status':'USER NOT FOUND'})
    else:
        return JsonResponse({'status':'NO DATA'})
    
@csrf_exempt
def bookingdetails(request):
    if request.method == 'POST':
        Name = request.POST.get('name')
        Age = request.POST.get('age')
        Phone = request.POST.get('phone')
        Email = request.POST.get('email')
        if Bookings.objects.filter(PHONE=Phone).exists():
            return JsonResponse({'error':'YOUR ALREADY BOOKED'})
        else:
            try:
               last_token = Bookings.objects.all().order_by('TOKEN').last()
               new_token = last_token.TOKEN+1
               Bookings.objects.create(NAME=Name,AGE=Age,PHONE=Phone,EMAIL=Email,TOKEN=new_token)
               return HttpResponse(f'booking successfull, Token number is {new_token}')
            except:
                Bookings.objects.create(NAME=Name,AGE=Age,PHONE=Phone,EMAIL=Email)
                return HttpResponse(f'booking successfull, Token number is {1}')
    else:
        return JsonResponse({'error':'METHOD IS WRONG'})
    
def searchdetails(request,name):
    if name:
        data = Registration.objects.filter(NAME__icontains=name) | Registration.objects.filter(USER_NAME__icontains=name) | Registration.objects.filter(PHONE__icontains=name) | Registration.objects.filter(EMAIL__icontains=name)
        serializer = registerserializer(data,many=True)
        return JsonResponse({'status':'SUCCESS','data':serializer.data})
    else :
        return JsonResponse({'error':'USER NOT FOUND'})