from django.contrib import admin
from .models import Car_Db, Category_Db
from Web_Pages.models import UserDB, TestDriveDB, EnquiryDB

# Register your models here.
admin.site.register(Car_Db)
admin.site.register(Category_Db)
admin.site.register(UserDB)
admin.site.register(TestDriveDB)
admin.site.register(EnquiryDB)