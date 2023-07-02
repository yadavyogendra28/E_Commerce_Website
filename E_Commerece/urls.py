from django.contrib import admin
from django.urls import path,include
from . import views
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('admin', admin.site.urls),
    path('',views.index,name="/"),
    # path('User_login',views.User_login),
    path('user_logined/',views.User_logined,name="user_logined"),
    path('SignUP',views.SignUP_method,name="SignUP"),
    path('LogOut',views.LogOut_method),
    path('AddCart',views.AddCart_method,name="AddCart"),
    path("BuyProduct",views.BuyProduct_method,name="Buy"),
    path("Grocery",views.Grocery_method,name="Grocery"),
    path("Mobiles",views.Mobiles_method,name="Mobiles"),
    path("Fashion",views.Fashion_method,name="Fashion"),
    path("Electronics",views.Electronics_method,name="Electronics"),
    path("Home_Product",views.Home_Product_method,name="Home_Product"),
    path("Search_data",views.Search_method,name="search"),
    path("Rating_Review",views.Rating_Review_method),

    path('User_login',include('product.urls')), # login function in my app 
    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
