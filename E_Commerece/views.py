from django.shortcuts import render
from product.models import product,product_add,product_Grocery,product_Mobiles,product_Fashion,product_Electronics,product_Home
from django.http import HttpResponse,HttpResponseRedirect
import random
from django.contrib.auth.forms import AuthenticationForm,UserCreationForm
from django.contrib.auth import authenticate,login,logout



def index(req):
   product_data=product_add.objects.all()

   product_GroceryR=list(product_Grocery.objects.all())
   product_GroceryRan=random.sample(product_GroceryR,3)

   product_MobilesR=list(product_Mobiles.objects.all())
   product_MobilesRan=random.sample(product_MobilesR,3)

   product_FashionR=list(product_Fashion.objects.all())
   product_FashionRan=random.sample(product_FashionR,3)
  
   product_ElectronicsR=list(product_Electronics.objects.all())
   product_ElectronicsRan=random.sample(product_ElectronicsR,3)

   product_HomeR=list(product_Home.objects.all())
   product_HomeRan=random.sample(product_HomeR,3)

   return render(req,'index.html',{'p_data':product_data,'p_dataG':product_GroceryRan,'p_dataM':product_MobilesRan,
                  'p_dataF':product_FashionRan,'p_dataE':product_ElectronicsRan,'p_dataH':product_HomeRan})




#  SignUP Function :: 

def SignUP_method(req):
   if req.method=="POST":
      fm=UserCreationForm(req.POST)
      if fm.is_valid():
         fm.save()
   else:
    fm=UserCreationForm()
   return render(req,'Signup.html',{'form':fm})



  #   # Login funcrion ::

# def User_login(req):
#       if req.method=="POST":
#          fm=AuthenticationForm(request=req,data=req.POST)
#          if fm.is_valid():
#             uname= fm.cleaned_data['username']
#             upass= fm.cleaned_data['password']
#             user=authenticate(username=uname,password=upass)
#             if user is not None:
#                login(req,user)
#                # url="user_logined/?user={}".format(user)
#                return HttpResponseRedirect('user_logined/')
              
              
#          else:
#            return HttpResponse(" <h1> Sorry !! Username and password is invalid !</h1>") 

#       else:
#         fm=AuthenticationForm()
#       return render(req,'loginpage.html',{'form':fm})
   


def User_logined(req):
  if req.user.is_authenticated:
   if req.method=="GET":
      user=req.GET.get('user')

      product_GroceryR=list(product_Grocery.objects.all())
      product_GroceryRan=random.sample(product_GroceryR,3)

      product_MobilesR=list(product_Mobiles.objects.all())
      product_MobilesRan=random.sample(product_MobilesR,3)

      product_FashionR=list(product_Fashion.objects.all())
      product_FashionRan=random.sample(product_FashionR,3)
  
      product_ElectronicsR=list(product_Electronics.objects.all())
      product_ElectronicsRan=random.sample(product_ElectronicsR,3)

      product_HomeR=list(product_Home.objects.all())
      product_HomeRan=random.sample(product_HomeR,3)


      return render(req,'index_login.html',{'user':req.user, 'p_dataG':product_GroceryRan,'p_dataM':product_MobilesRan,
                  'p_dataF':product_FashionRan,'p_dataE':product_ElectronicsRan,'p_dataH':product_HomeRan})
  else:
     return HttpResponseRedirect('User_login')


def LogOut_method(req):
   u=req.user
   global user5
   user5=req.user
   logout(req)
   url="Rating_Review?user={}".format(u)
   
   return HttpResponseRedirect(url)


def Rating_Review_method(req):
   user=req.GET.get('user')
   return render(req,'Rating_Review.html',{'user':user})





def AddCart_method(req):
   if req.method=="GET":
      fm=AuthenticationForm()
      return render(req,'loginpage.html',{'form':fm})
   

def BuyProduct_method(req):
   if req.method=="GET":
       fm=AuthenticationForm()
       return render(req,'loginpage.html',{'form':fm})
   


def Grocery_method(req):
   product_GroceryR=list(product_Grocery.objects.all())
   c=product_Grocery.objects.all().count()
   product_GroceryRan=random.sample(product_GroceryR,c)
   return render(req,"Grocery.html",{"p_data":product_GroceryRan})


def Mobiles_method(req):
   product_MobilesR=list(product_Mobiles.objects.all())
   c=product_Mobiles.objects.all().count()
   product_MobilesRan=random.sample(product_MobilesR,c)
   return render(req,"Mobiles.html",{"p_data":product_MobilesRan})


def Fashion_method(req):
   product_FashionR=list(product_Fashion.objects.all())
   c=product_Fashion.objects.all().count()
   product_FashionRan=random.sample(product_FashionR,c)
   return render(req,'Fashion.html',{"p_data":product_FashionRan})



def Electronics_method(req):
   product_ElectronicsR=list(product_Electronics.objects.all())
   c=product_Electronics.objects.all().count()
   product_ElectronicsRan=random.sample(product_ElectronicsR,c)
   return render(req,'Electronics.html',{'p_data':product_ElectronicsRan})


def Home_Product_method(req):
   Home_ProductR=list(product_Home.objects.all())
   c= product_Home.objects.all().count()
   Home_ProductRan=random.sample(Home_ProductR,c)
   return render(req,'Home_Product.html',{"p_data":Home_ProductRan})




def Search_method(req):
   if req.method=="POST":
      nm=req.POST.get("searchdata")
      d1=product_Grocery.objects.filter(title=nm)
      d2=product_Mobiles.objects.filter(title=nm)
      d3=product_Fashion.objects.filter(title=nm)
      d4=product_Electronics.objects.filter(title=nm)
      d5=product_Home.objects.filter(title=nm)

      if d1 or d2 or d3 or d4 or d5:
         return render(req,'search.html',{"p_data1":d1,"p_data2":d2,"p_data3":d3,"p_data4":d4,"p_data5":d5,})
      else:
         return HttpResponse("No Data Found !")
