from django.contrib import admin
#from .models import Leave_Balance,DataId,Manager,Employee
from .models import Manager,Employee,Department,Company_Holiday,CurrentProject
# Register your models here
#admin.site.register(Leave_Balance)
#admin.site.register(DataId)
admin.site.register(Manager)
admin.site.register(Department)
admin.site.register(Employee)
admin.site.register(Company_Holiday)
admin.site.register(CurrentProject)
