from django.contrib import admin
from product.models import product,product_add,product_Grocery,\
product_Mobiles,product_Fashion,product_Electronics,product_Home,Rating,product_Add_Cart,Address_Add


class productAdmin(admin.ModelAdmin):
    list_display=('user_name','password')

# admin.site.register(product,productAdmin)
# admin.site.register(product_add)
admin.site.register(product_Grocery)
admin.site.register(product_Mobiles)
admin.site.register(product_Fashion)
admin.site.register(product_Electronics)
admin.site.register(product_Home)
admin.site.register(Rating)
admin.site.register(product_Add_Cart)
admin.site.register(Address_Add)



# Register your models here.
