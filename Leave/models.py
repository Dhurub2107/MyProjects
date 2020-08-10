from django.db import models
from django.conf import settings
# Create your models here.


'''class DataId(models.Model):
    Leave_Id=models.IntegerField(unique=True)
    #Employee_id=models.IntegerField(primary_key=True)
    Department_id=models.IntegerField(unique=True)'''

'''class Leave_Balance(models.Model):
    Leave_id=models.ForeignKey(DataId,on_delete=models.CASCADE)
    Leave_Name=models.CharField(max_length=10)'''
class Manager(models.Model):
    Manager_id=models.IntegerField(primary_key=True)
    Manager_Name=models.CharField(max_length=20)

    def __str__(self):
        return self.Manager_Name
    
class Department(models.Model):
    Department_id=models.IntegerField(primary_key=True)
    Department_Name=models.CharField(max_length=50)
    def __str__(self):
        return self.Department_Name
class Employee(models.Model):
    Emp_Choice=[
        ("1","Yes"),
        ("2","No")
    ]
    Emp_BGV=[
        ("1","Done"),
        ("2","NotDone"),
        ("0","InProgress")
    ]
    Emp_Offer=[
        ("1","Provided"),
        ("2","NotProvided")
        ]
    Emp_id=models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    Emp_name=models.CharField(max_length=20)
    Emp_Prob=models.CharField(max_length=2,choices=Emp_Choice)
    Emp_ML=models.IntegerField()
    Emp_CL=models.IntegerField()
    Emp_CompOff=models.IntegerField()
    Emp_Email=models.EmailField(max_length=50,unique=True,default=None)
    Date=models.DateField(auto_now=True)
    Manager=models.ForeignKey(Manager,on_delete=models.CASCADE)
    Department=models.ForeignKey(Department,on_delete = models.CASCADE)
    Background_Verification=models.CharField(max_length=2,choices=Emp_BGV,default=None)
    Offer_Latter=models.CharField(max_length=2,choices=Emp_Offer,default=None)
    def __str__(self):
        return self.Emp_name+ ' : ' + self.Emp_Email

    #user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,default=1)
'''class ChoseManager(models.Model):
    Manager_id=models.ForeignKey(Employee,on_delete=models.CASCADE)
    Department_id=models.ForeignKey(Employee,on_delete=models.CASCADE)'''
class LeaveData(models.Model):
    Name=models.CharField(max_length=20)
    Email=models.CharField(max_length=40)
    Contact=models.CharField(max_length=12)
    From_Date=models.DateField()
    To_Date=models.DateField()
    Leave_Type=models.CharField(max_length=20)
    Department=models.CharField(max_length=30)
    Reason=models.CharField(max_length=200)
    No_Days=models.IntegerField()
    Manager_Id=models.ForeignKey(Manager,on_delete=models.CASCADE)
    Apply_Date=models.DateField(auto_now=True)
    Manager_Remark=models.CharField(max_length=20,default="Pending")

class Company_Holiday(models.Model):
    Holiday_Type=[
        ("Holiday","Holiday"),
        ("Restricted Holiday","Restricted Holiday"),
        ("National Holiday","National Holiday")
    ]
    Holiday_List=[
        ("Republic Day","Republic Day"),
        ("Holi","Holi"),
        ("Good Friday","Good Friday"),
        ("Independence Day","Independence Day"),
        ("Rakshabandhan","Rakshabandhan"),
        ("Gandhi Jayanti","Gandhi Jayanti"),
        ("Dashera","Dashera"),
        ("Deepawali","Deepawali"),
        ("Christmas","Christmas")
    ]
    Date=models.DateField()
    Festival_Name=models.CharField(max_length=30,choices=Holiday_List)
    Type=models.CharField(max_length=20,choices=Holiday_Type)
    def __str__(self):
        return self.Festival_Name
    
class CurrentProject(models.Model):
    Project_Priorty=[
        ("Low","Low"),
        ("Medium","Medium"),
        ("High","High"),

    ]
    Priorty=models.CharField(max_length=20,choices=Project_Priorty)
    ProjectName=models.CharField(max_length=60)
    def __str__(self):
        return self.ProjectName+":"+self.Priorty
class CompoffData(models.Model):
    Name=models.CharField(max_length=20)
    Email=models.CharField(max_length=40)
    Contact=models.CharField(max_length=12)
    From_Date=models.DateField()
    To_Date=models.DateField()
    Project_Name=models.CharField(max_length=60)
    Department=models.CharField(max_length=30)
    Reason=models.CharField(max_length=200)
    No_Days=models.IntegerField()
    Manager_Id=models.ForeignKey(Manager,on_delete=models.CASCADE)
    Apply_Date=models.DateField(auto_now=True)
    Manager_Remark=models.CharField(max_length=20,default="Pending")


    
   


    
