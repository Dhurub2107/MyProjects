from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from django.contrib import messages
from django.http import HttpResponseRedirect
from .models import Employee,Manager,LeaveData,Department,Company_Holiday,CurrentProject,CompoffData
from datetime import datetime,timedelta
from LMS.settings import EMAIL_HOST_USER
from django.core.mail import send_mail
from django.contrib.auth.models import User
#from cryptography.fernet import Fernet
import base64
import logging
import traceback
from django.conf import settings
import random
import string
from itertools import chain
import calendar
import datetime
import io
from django.http import FileResponse
#from reportlab.pdfgen import canvas
#this is your "password/ENCRYPT_KEY". keep it in settings.py file
#key = Fernet.generate_key() 
#***********************************login View**************************************************************
# Create your views here.
def login(request):
    if request.method=='POST':
        user_name=request.POST['uname']
        password=request.POST['password']
        #print("uname",user_name)
        #print("Pasword",password)
        user=auth.authenticate(username=user_name,password=password)
        #print("user:",user)
        if user is not None:
            auth.login(request,user)
            return redirect('home')
            #messages.info(request,"Welcome")
            
        else:
            messages.info(request,"Wrong Credentials")
            return redirect('login')
    else:
        return render(request,'login.html')

#********************************************Home View*****************************************
def home(request):
    return render(request,'index.html')
#___________________________________________Logout View_____________________________________
def logout(request):
    auth.logout(request)
    return render(request,'index.html')
#*******************************************Leave View******************************************
def Leave(request):
    if request.method=="POST":
        first_name=request.POST['Name_First']
        return render(request,'Policy.html',{'first_name':first_name})
    data=User.objects.filter(username=request.user).values('first_name','email')
    return render(request,'Leave.html',{'data':data})

#*******************************************Policy View*******************************************
def Policy(request):
    return render(request,'Policy.html')

#********************************************LeaveBalance View*****************************************
def LeaveBalance(request):
    try:
        user = request.user
        #print(user.username)
        My_Leave=Employee.objects.filter(Emp_id_id = request.user)
        #My_Leave=Employee.objects.all()
        #print(My_Leave)
        return render(request,'LeaveBalance.html',{"My_Leave":My_Leave})
    except Exception as e:
        messages.info(request,"Can not See Leave Balance Please login First")
        return render(request,'error_404.html')
#*******************************************Back View and Error View************************************************
def Back(request):
    return redirect("home")
def Error(request):
    return render(request,'Error.html')

#*******************************************ManagerName View********************************************************
def ManagerName(request):
    #Emp_Manager=Employee.objects.filter(Emp_id_id = request.user)
    Emp_Manager = Employee.objects.filter(Emp_id_id = request.user)
    #Manager_Name=Manager.objects.filter(Manager_id=Emp_Manager.Manager_id)
    #print(Manager_Name)
    #print(Emp_Manager.query)
    return render(request,'History.html',{'Emp_Manager':Emp_Manager})

#*****************************Goback,Sucess,GoBack,LeaveError Notification View********************
def Goback(request):
    return redirect('Leave')
def Sucess(request):
    return render(request,'Sucess.html')
def SubGoback(request):
    return redirect('home')
def LeaveError(request):
    return render(request,'LeaveBalError.html')
#_____________________________Leave Apply View_____________________________________

def LeaveApp(request):
    if request.method=="POST":
        #Name=request.POST['uname']
        #Email=request.POST['email']
        Contact=request.POST['cnct']
        From=request.POST['From']
        print("From:",From)
        To=request.POST['To']
        Type=request.POST['select']
        Select_Department=request.POST['DepartSelect']
        Reason=request.POST['reason']
        #From=request.POST['From']
        #To=request.POST['To']
        #print(request.user)
        Emp_Manager = Employee.objects.filter(Emp_id_id = request.user).values('Manager_id')
        for Manager in Emp_Manager:
            Manager_id=Manager['Manager_id']
        Dept_id=Employee.objects.filter(Emp_Email=request.user.username).values('Department_id')
        for user_Dept in Dept_id:
            Correct_Dept=user_Dept['Department_id']
        #print("Z:",Correct_Dept)
        Dept=Department.objects.filter(Department_id=Correct_Dept).values('Department_Name')
        for Dept_Name in Dept:
            Correct_DeptName=Dept_Name['Department_Name']
        user = request.user
        #print("x:",Correct_DeptName)
        #Dept_id=str(Dept_id)
        #print(Dept_id)
        #if User.objects.filter(email=request.user.username):
        #Dept_id=Department.objects.get(Department_id=Department_id,Department_Name=Department_Name)
        #print(Dept_id)
        #Leave=Employee.objects.filter().values('Emp_')
        #Input Formating
        #correct_Name=Name.capitalize()#Any Case of Enter Name by Employee
        #correct_Email=Email.capitalize()#For Email  
        #End Input Formating
        #Leave Balance Check
        date_format = "%Y-%m-%d"
        a = datetime.datetime.strptime(str(From), date_format)
        b = datetime.datetime.strptime(str(To), date_format)
        today = datetime.datetime.today().strftime ('%Y-%m-%d')
        Current_Date_Formatted=a.strftime ('%Y-%m-%d')
        #print(Current_Date_Formatted)
        tdy=datetime.datetime.now()
        end_date = tdy + datetime.timedelta(days=3)
        end_date_new=end_date.strftime ('%Y-%m-%d')
        print("End date:",end_date_new)
        print("From:",Current_Date_Formatted)
        print("Today:",today)
        if b>a and Current_Date_Formatted>=today:
            delta = b - a
            days=delta.days
            #print("Days:",days)
        else:
            messages.info(request,"Invalid Dates Entered Please Go back and Check Dates First")
            return redirect('Error')
        Leave_Type=Employee.objects.filter(Emp_Email=request.user.username).values('Emp_ML','Emp_CL','Emp_CompOff')
        #print(Leave_Type)
        for Leave in Leave_Type:
            Leave_Bal_ML=Leave['Emp_ML']
            Leave_Bal_CL=Leave['Emp_CL']
            Leave_Bal_CompOff=Leave['Emp_CompOff']
        #print("ML:",Leave_Bal_ML)
        #print("CL:",Leave_Bal_CL)
        #print("CompOff:",Leave_Bal_CompOff)
        #print(Type )
        #End code here
        #Date formating,extracting date from datetime and conversion datetime object.
        myfromdate=str(a)
        #datetime.datetime.strptime(myfromdate, "%Y-%m-%d")
        dt = datetime.datetime.strptime(myfromdate,'%Y-%m-%d %H:%M:%S')
        dd=dt.date()
        print(dd)
        myfromdate=str(dd)
        mytodate=str(b)
        dy = datetime.datetime.strptime(mytodate,'%Y-%m-%d %H:%M:%S')
        ddate=dy.date()
        mytodate=str(ddate)
        #print("FromDate:",myfromdate)
        year, month, day = (int(i) for i in myfromdate.split('-'))
        year1, month1, day1 = (int(j) for j in mytodate.split('-'))
        check = datetime.date(year, month, day)
        check1 = datetime.date(year1, month1, day1)
        fromday=check.strftime("%A")
        leavetoday=check1.strftime("%A")
        #End Datetime Formate
        ##############################sandwitch Checking test code ###############################
        Email=request.user.email
        latest_leave=LeaveData.objects.filter(Email=Email).values('To_Date','id','Manager_Remark')
        for k in latest_leave:
            sandTo=k['To_Date']
            appid=k['id']
            Mgr_Remark=k['Manager_Remark']
        print("appid:",appid)
        sandTo=sandTo-timedelta(days=1)
        print("AA:",sandTo)
        mydate=str(sandTo)
        print("sandfrom:",sandTo)
        """dt1 = datetime.datetime.strptime(mydate,'%Y-%m-%d %H:%M:%S')
        dd1=dt1.date()
        print(dd1)
        mydate=str(dd1)
        print(mydate)"""
        #datetime.datetime.strptime(myfromdate, "%Y-%m-%d")
        year2, month2, day2 = (int(i) for i in mydate.split('-'))
        check2 = datetime.date(year2, month2, day2)
        sandwichleave=check2.strftime("%A")
        print(sandwichleave)
        print("Last Leave Date:",mydate)
        print("Last Leave Day:",sandwichleave)
        print("Current Leave Day:",fromday)
        print("Current Leave Date:",From)
        date_format = "%Y-%m-%d"
        Last_date = datetime.datetime.strptime(str(mydate), date_format)
        new_apply = datetime.datetime.strptime(str(From), date_format)
        #print(Current_Date_Formatted)
        delta = new_apply - Last_date
        daybetween=delta.days
        print("Between Days:",daybetween)
        print("Manager Remark:",Mgr_Remark)
        #################################################################################
        if end_date_new>=Current_Date_Formatted:
            if sandwichleave!="Friday" or fromday!="Monday" or daybetween>4 or sandwichleave!="Monday" or fromday!="Friday" or Mgr_Remark=="Rejected" :
                if fromday!="Sunday" and leavetoday!="Sunday" and leavetoday!="Saturday":
                    if Correct_DeptName==Select_Department:
                        if Leave_Bal_ML>=days and Type=='ML':
                            Updated_Bal_ML=Leave_Bal_ML-days
                            print(Updated_Bal_ML)
                            Update_Bal=Employee.objects.filter(Emp_Email=request.user.username).update(Emp_ML=Updated_Bal_ML)
                            # Update_Bal.save()
                            email=request.user
                            email=str(email)
                            msg=LeaveData.objects.create(Name=request.user.first_name,Email=email,Contact=Contact,From_Date=From,To_Date=To,Leave_Type=Type,Department=Select_Department,Reason=Reason,No_Days=days,Manager_Id_id=Manager_id)
                            msg.save()
                            messages.info(request,"Application Submitted Sucessfully Go and Check in Status Window")
                            return redirect('Sucess')
                        elif Leave_Bal_CL>=days and Type=='CL':
                            Updated_Bal_CL=Leave_Bal_CL-days
                            #print(Updated_Bal_CL)
                            email=request.user
                            email=str(email)
                            Update_Bal=Employee.objects.filter(Emp_Email=request.user.username).update(Emp_CL=Updated_Bal_CL)
                            msg=LeaveData.objects.create(Name=request.user.first_name,Email=email,Contact=Contact,From_Date=From,To_Date=To,Leave_Type=Type,Department=Select_Department,Reason=Reason,No_Days=days,Manager_Id_id=Manager_id)
                            msg.save()
                            messages.info(request,"Application Submitted Sucessfully Go and Check in Status Window")
                            return redirect('Sucess')
                        elif Leave_Bal_CompOff>=days and Type=='Comp-OFF':
                            Updated_Bal_CompOff=Leave_Bal_CompOff-days
                            #print(Updated_Bal_CompOff)
                            email=request.user
                            email=str(email)
                            Update_Bal=Employee.objects.filter(Emp_Email=request.user.username).update(Emp_CompOff=Updated_Bal_CompOff)
                            msg=LeaveData.objects.create(Name=request.user.first_name,Email=email,Contact=Contact,From_Date=From,To_Date=To,Leave_Type=Type,Department=Select_Department,Reason=Reason,No_Days=days,Manager_Id_id=Manager_id)
                            msg.save()
                            messages.info(request,"Application Submitted Sucessfully Go and Check in Status Window")
                            return redirect('Sucess')
                        else:
                            messages.info(request,"Application Failed Please Go and check Leave Balance")
                            return redirect('LeaveError')
                    else:
                        messages.info(request,"You Does not Belog to this Department as per your Office Details")
                        return redirect('Error')
                else:
                    messages.info(request,"You cant apply leave for Saturday and Sunday")
                    return redirect('Error')
            else:
                days=days+2
                if fromday!="Sunday" and leavetoday!="Sunday" and leavetoday!="Saturday":
                    if Correct_DeptName==Select_Department:
                        if Leave_Bal_ML>=days and Type=='ML':
                            Updated_Bal_ML=Leave_Bal_ML-days
                            print(Updated_Bal_ML)
                            Update_Bal=Employee.objects.filter(Emp_Email=request.user.username).update(Emp_ML=Updated_Bal_ML)
                            #Update_Bal.save()
                            email=request.user
                            email=str(email)
                            msg=LeaveData.objects.create(Name=request.user.first_name,Email=email,Contact=Contact,From_Date=From,To_Date=To,Leave_Type=Type,Department=Select_Department,Reason=Reason,No_Days=days,Manager_Id_id=Manager_id)
                            msg.save()
                            messages.info(request,"Application Submitted Sucessfully Go and Check in Status Window")
                            return redirect('Sucess')
                        elif Leave_Bal_CL>=days and Type=='CL':
                            Updated_Bal_CL=Leave_Bal_CL-days
                            #print(Updated_Bal_CL)
                            email=request.user
                            email=str(email)
                            Update_Bal=Employee.objects.filter(Emp_Email=request.user.username).update(Emp_CL=Updated_Bal_CL)
                            msg=LeaveData.objects.create(Name=request.user.first_name,Email=email,Contact=Contact,From_Date=From,To_Date=To,Leave_Type=Type,Department=Select_Department,Reason=Reason,No_Days=days,Manager_Id_id=Manager_id)
                            msg.save()
                            messages.info(request,"Application Submitted Sucessfully Go and Check in Status Window")
                            return redirect('Sucess')
                        elif Leave_Bal_CompOff>=days and Type=='Comp-OFF':
                            Updated_Bal_CompOff=Leave_Bal_CompOff-days
                            #print(Updated_Bal_CompOff)
                            email=request.user
                            email=str(email)
                            Update_Bal=Employee.objects.filter(Emp_Email=request.user.username).update(Emp_CompOff=Updated_Bal_CompOff)
                            msg=LeaveData.objects.create(Name=request.user.first_name,Email=email,Contact=Contact,From_Date=From,To_Date=To,Leave_Type=Type,Department=Select_Department,Reason=Reason,No_Days=days,Manager_Id_id=Manager_id)
                            msg.save()
                            messages.info(request,"Application Submitted Sucessfully Go and Check in Status Window")
                            return redirect('Sucess')
                        else:
                            messages.info(request,"Application Failed Please Go and check Leave Balance")
                            return redirect('LeaveError')
                    else:
                        messages.info(request,"You Does not Belog to this Department as per your Office Details")
                        return redirect('Error')
                else:
                    messages.info(request,"You cant apply leave for Saturday and Sunday")
                    return redirect('Error')
        else:
            messages.info(request,"You can not choose date of future within 3 days")
            return redirect('Error')


#_____________________________Employee Leave History View__________________________

def LeaveHistory(request):
    Email=request.user.email
    Leave_history=LeaveData.objects.filter(Email=Email).order_by('-Apply_Date')[:10]
    return render(request,'History.html',{'Leave_history':Leave_history})

#_____________________________Leave Pending View__________________________________

def LeavePending(request):
    #print(question_id)
    #user=request.user
    #print(id)
    try:
        ManagerId=Manager.objects.filter(Manager_Name=request.user.first_name).values('Manager_id')
        #print(ManagerId)
        for MGR in ManagerId:
            Managerid=MGR['Manager_id']
        #print(Managerid)
        Emp=LeaveData.objects.filter(Manager_Id_id=Managerid,Manager_Remark="Pending")
        #appid = request.POST.get('app_id')
        #print("appid:",appid)
        Mgr=Manager.objects.all()
        return render(request,'PendingRequests.html',{'Emp':Emp,'Mgr':Mgr})
    except Exception as e:
        messages.info(request,"You Dont have Permision of this page.")
        return render(request,'error_404.html')

#____________________________________Leave Approval View______________________________________
def LeaveApprove(request):
    try:
        your_parameter = request.GET['parameter']
        #print(your_parameter)
        #appid = request.POST.get('app_id')
        #prin t("appid:",appid)
        Approval=LeaveData.objects.filter(id=your_parameter).update(Manager_Remark="Approved")
        MyLeaveData=LeaveData.objects.filter(id=your_parameter).values('Email','No_Days','Leave_Type','Name','From_Date','To_Date')
        for j in MyLeaveData:
            Email=j['Email']
            Name=j['Name']
            From=j['From_Date']
            To=j['To_Date']
        print(Name)
        subject = 'Leave Approval'
        message = "Dear"+" "+str(Name)+","+"\n\nThis is to informed you that your leave has been Approved From """+str(From)+" To "+str(To)+" For more details go and check Leave Portal.\nplease do not reply this mail this is system genrated mail."+"\n\nThanks,\n\"IwebServices"
        emp_email= str(Email)
        recepient=["iwebdhurub@gmail.com"]
        recepient.append(emp_email)
        send_mail(subject, message, EMAIL_HOST_USER, recepient, fail_silently = False)
        return redirect("Leaverequest")
    except Exception as e:
        messages.info(request,"You Dont have Permision of this page.")
        return render(request,'error_404.html')

#__________________________________Leave Rejection View___________________________________________
def LeaveReject(request):
    your_parameter = request.GET['parameter']
    #your_parameter2 = request.GET['parameter2']
    #print(your_parameter2)
    Approval=LeaveData.objects.filter(id=your_parameter).update(Manager_Remark="Rejected")
    MyLeaveData=LeaveData.objects.filter(id=your_parameter).values('Email','No_Days','Leave_Type','Name','From_Date','To_Date')
    for j in MyLeaveData:
        Email=j['Email']
        Days=j['No_Days']
        Type=j['Leave_Type']
        Name=j['Name']
        From=j['From_Date']
        To=j['To_Date']
    Leave_Type=Employee.objects.filter(Emp_Email=Email).values('Emp_ML','Emp_CL','Emp_CompOff')
    #print(Email,Days,Type)
    for Leave in Leave_Type:
        Leave_Bal_ML=Leave['Emp_ML']
        Leave_Bal_CL=Leave['Emp_CL']
        Leave_Bal_CompOff=Leave['Emp_CompOff']
    #print("ML:",Leave_Bal_ML)
    #print("CL:",Leave_Bal_CL)
    #print("CompOff:",Leave_Bal_CompOff)
    #print(Type )
    subject = 'Leave Rejection'
    message = "Dear"+" "+str(Name)+","+"\n\nThis is to informed you that your leave has been Rejected From """+str(From)+" To "+str(To)+" and credited "+str(Days)+"Leaves in your Leave Balance For more details go and check Leave Portal please do not reply this mail this is system genrated mail."+"\n\nThanks,\n\"IwebServices"
    emp_email= str(Email)
    recepient=["iwebdhurub@gmail.com"]
    recepient.append(emp_email)
    send_mail(subject, message, EMAIL_HOST_USER, recepient, fail_silently = False)
    if Type=='ML':
        Updated_Bal_ML=Leave_Bal_ML+Days
        Update_Bal=Employee.objects.filter(Emp_Email=Email).update(Emp_ML=Updated_Bal_ML)
        return redirect("Leaverequest")
    elif Type=='CL':
        Updated_Bal_CL=Leave_Bal_CL+Days
        #print(Updated_Bal_CL)
        Update_Bal=Employee.objects.filter(Emp_Email=Email).update(Emp_CL=Updated_Bal_CL)
        return redirect("Leaverequest")
    else:
        Updated_Bal_CompOff=Leave_Bal_CompOff+Days
        #print(Updated_Bal_CompOff)
        Update_Bal=Employee.objects.filter(Emp_Email=Email).update(Emp_CompOff=Updated_Bal_CompOff)
        return redirect("Leaverequest")

#__________________________________Leave Forword one Manager to  another__________________
def LeaveForword(request):
    your_parameter = request.GET['appid']
    mgrid=request.GET['managerid']
    print(your_parameter)
    print(mgrid)
    ###################### Extract Name For Mail################################################
    App_Manager=LeaveData.objects.filter(id=your_parameter).values('Manager_Id_id')
    for s in App_Manager:
        Cur_Mgr_id=s['Manager_Id_id']
    print(Cur_Mgr_id)
    Current_Manager=Manager.objects.filter(Manager_id=Cur_Mgr_id).values('Manager_Name')
    for r in Current_Manager:
        Current_Manager_Name=r['Manager_Name']
    print(Current_Manager_Name)
    MgrName=Manager.objects.filter(Manager_id=mgrid).values('Manager_Name')
    for x in MgrName:
        Forword_Manager=x['Manager_Name']
    print(Forword_Manager)
    ######################END##############################################
    #print(Mgr_id)
    Managerid=LeaveData.objects.filter(id=your_parameter).values('Manager_Id_id')
    """##############################testing Code####################################
    UpdateManager=Manager.objects.filter(Manager_Name=Mgr_name).values('Manager_id')
    MyLeaveData=LeaveData.objects.filter(id=your_parameter).update(Manager_Id_id=UpdateManager)
    LeaveData.objects.filter(id=your_parameter).update(Manager_Remark="Forworded")
    return redirect("Leaverequest")
    #############################################################################"""
    for Mgr in Managerid:
        Mgr_id=Mgr['Manager_Id_id']

    MyLeaveData=LeaveData.objects.filter(id=your_parameter).update(Manager_Id_id=mgrid)
    LeaveData.objects.filter(id=your_parameter).update(Manager_Remark="Forworded")
    MyLeaveData=LeaveData.objects.filter(id=your_parameter).values('Name','Email')
    for j in MyLeaveData:
        Name=j['Name']
        Email=j['Email']
    subject = 'Application Forworded'
    message = "Dear"+" "+str(Name)+","+"\n\nThis is to informed you that your Leave Application has been Foworded From "+str(Current_Manager_Name)+" To "+str(Forword_Manager)+ ".\nFor more details go and check Employee Portal.Please do not reply this mail this is system genrated mail."+"\n\nThanks,\n\"IwebServices"
    emp_email= str(Email)
    recepient=["iwebdhurub@gmail.com"]
    recepient.append(emp_email)
    send_mail(subject, message, EMAIL_HOST_USER, recepient, fail_silently = False)
    return redirect("Leaverequest")

#*****************************************Forworded Request View********************************
def ForwordedRequest(request):
    ManagerId=Manager.objects.filter(Manager_Name=request.user.first_name).values('Manager_id')
    #print(ManagerId)
    for MGR in ManagerId:
        Managerid=MGR['Manager_id']
    #print(Managerid)
    Emp=LeaveData.objects.filter(Manager_Id_id=Managerid,Manager_Remark="Forworded")
    return render(request,'Forword.html',{'Emp': Emp})

#***********************************Change Password Option View*****************************
def Changepass(request):
    """all_models_dict = {
        "extra_context" : {"role_list" : Manager.objects.all(),
                           "venue_list": LeaveData.objects.all(),
                           #and so on for all the desired models...
                          }
    }"""
    Lvdata=LeaveData.objects.all().values('id')
    Mgrdata=Manager.objects.all().values('Manager_Name')
    #Mgrdata=Lvdata.union(Mgr)
    result_list = list(chain(Lvdata, Mgrdata))
    print(result_list)
    return render(request,'Changepassword.html',{'result_list':result_list})
    #Mgrdata=LeaveData.objects.all()
    #Mgrdata=Managers.objects.all()
    #return render(request,'Changepassword.html',{'manager':Mgrdata})

#******************************ChangePassword  View***************************************
def ChangePassword(request):
    letters = string.ascii_letters
    newpass=''.join(random.choice(letters) for i in range(8))
    Emp=User.objects.filter(first_name=request.user.first_name,email=request.user).values('first_name','email')
    for Mydata in Emp:
        Name=Mydata['first_name']
        Email=Mydata['email']
    subject = 'Change Password'
    message = "Dear"+" "+str(Name)+","+"\n\nIt looks like you requested a new password this is your new password:\" " +str(newpass)+"\""+"\nplease do not reply this mail this is system genrated mail."+"\n\nThanks,\n\"IwebServices\""
    emp_email= str(Email)
    recepient=[]
    recepient.append(emp_email)
    send_mail(subject, message, EMAIL_HOST_USER, recepient, fail_silently = False)
    u = User.objects.get(username=request.user)
    u.set_password(newpass)
    u.save()
    return redirect("home")
#__________________________For Forworded Approve______________________________________
def ForwordedApprove(request):
    try:
        your_parameter = request.GET['parameter']
        #print(your_parameter)
        #appid = request.POST.get('app_id')
        #prin t("appid:",appid)
        Approval=LeaveData.objects.filter(id=your_parameter).update(Manager_Remark="Approved")
        MyLeaveData=LeaveData.objects.filter(id=your_parameter).values('Email','No_Days','Leave_Type','Name','From_Date','To_Date')
        for j in MyLeaveData:
            Email=j['Email']
            Name=j['Name']
            From=j['From_Date']
            To=j['To_Date']
        print(Name)
        subject = 'Leave Approval'
        message = "Dear"+" "+str(Name)+","+"\n\nThis is to informed you that your leave has been Approved From """+str(From)+" To "+str(To)+" For more details go and check Leave Portal.\nplease do not reply this mail this is system genrated mail."+"\n\nThanks,\n\"IwebServices"
        emp_email= str(Email)
        recepient=["iwebdhurub@gmail.com"]
        recepient.append(emp_email)
        send_mail(subject, message, EMAIL_HOST_USER, recepient, fail_silently = False)
        return redirect("ForwordedRequest")
    except Exception as e:
        messages.info(request,"You Dont have Permision of this page.")
        return render(request,'error_404.html')
#__________________________________Forworded Leave Reject______________________________-
def ForwordedReject(request):
    your_parameter = request.GET['parameter']
    #your_parameter2 = request.GET['parameter2']
    #print(your_parameter2)
    Approval=LeaveData.objects.filter(id=your_parameter).update(Manager_Remark="Rejected")
    MyLeaveData=LeaveData.objects.filter(id=your_parameter).values('Email','No_Days','Leave_Type','Name','From_Date','To_Date')
    for j in MyLeaveData:
        Email=j['Email']
        Days=j['No_Days']
        Type=j['Leave_Type']
        Name=j['Name']
        From=j['From_Date']
        To=j['To_Date']
    Leave_Type=Employee.objects.filter(Emp_Email=Email).values('Emp_ML','Emp_CL','Emp_CompOff')
    #print(Email,Days,Type)
    for Leave in Leave_Type:
        Leave_Bal_ML=Leave['Emp_ML']
        Leave_Bal_CL=Leave['Emp_CL']
        Leave_Bal_CompOff=Leave['Emp_CompOff']
    #print("ML:",Leave_Bal_ML)
    #print("CL:",Leave_Bal_CL)
    #print("CompOff:",Leave_Bal_CompOff)
    #print(Type )
    subject = 'Leave Rejection'
    message = "Dear"+" "+str(Name)+","+"\n\nThis is to informed you that your leave has been Rejected From """+str(From)+" To "+str(To)+" and credited "+str(Days)+"Leaves in your Leave Balance For more details go and check Leave Portal please do not reply this mail this is system genrated mail."+"\n\nThanks,\n\"IwebServices"
    emp_email= str(Email)
    recepient=["iwebdhurub@gmail.com"]
    recepient.append(emp_email)
    send_mail(subject, message, EMAIL_HOST_USER, recepient, fail_silently = False)
    if Type=='ML':
        Updated_Bal_ML=Leave_Bal_ML+Days
        Update_Bal=Employee.objects.filter(Emp_Email=Email).update(Emp_ML=Updated_Bal_ML)
        return redirect("ForwordedRequest")
    elif Type=='CL':
        Updated_Bal_CL=Leave_Bal_CL+Days
        #print(Updated_Bal_CL)
        Update_Bal=Employee.objects.filter(Emp_Email=Email).update(Emp_CL=Updated_Bal_CL)
        return redirect("ForwordedRequest")
    else:
        Updated_Bal_CompOff=Leave_Bal_CompOff+Days
        #print(Updated_Bal_CompOff)
        Update_Bal=Employee.objects.filter(Emp_Email=Email).update(Emp_CompOff=Updated_Bal_CompOff)
        return redirect("ForwordedRequest")

########################################################################################
def test(request):
    Lvdata=LeaveData.objects.all().values('id')
    Mgrdata=Manager.objects.all().values('Manager_Name')
    #Mgrdata=Lvdata.union(Mgr)
    ManagerId=Manager.objects.filter(Manager_Name=request.user.first_name).values('Manager_id')
    #print(ManagerId)
    for MGR in ManagerId:
        Managerid=MGR['Manager_id']
    #print(Managerid) 
    Emp=LeaveData.objects.filter(Manager_Id_id=Managerid,Manager_Remark="Pending")
    #appid = request.POST.get('app_id')
    #print("appid:",appid)
    #Emp = list(chain(Lvdata, Mgrdata,Emp,ManagerId))
    print(Emp)
    Mgr=Manager.objects.all()
    #mlist=[]
    """for mgname in Mgr:
        Mname=mgname['Manager_Name']
        mlist.append(Mname)"""
    print(Mgr)
    return render(request,'test.html',{'Emp':Emp,'Mgr':Mgr})

def festival(request):
    holiday=Company_Holiday.objects.all().order_by("Date")
    return render(request,"nationalfestival.html",{"holiday":holiday})

def Forgot(request):
        return render(request,"Forgot.html")
def ForgotPass(request):
    Email=request.POST['emailF']
    print(Email)
    alluser=User.objects.all().values("email")
    print(alluser)
    res = [ sub['email'] for sub in alluser ]
    if Email in res:
        letters = string.ascii_letters
        newpass=''.join(random.choice(letters) for i in range(8))
        emp_email= str(Email)
        z=emp_email.split(".")
        Name=z[0].capitalize()
        subject = 'Forgot Password'
        message = "Dear"+" "+str(Name)+","+"\n\nIt looks like you requested a new password this is your new password:\" " +str(newpass)+"\""+"\nplease do not reply this mail this is system genrated mail."+"\n\nThanks,\n\"IwebServices\""

        recepient=[]
        recepient.append(emp_email)
        send_mail(subject, message, EMAIL_HOST_USER, recepient, fail_silently = False)
        u = User.objects.get(username=emp_email)
        u.set_password(newpass)
        u.save()
        return redirect("login")
    else:  
        messages.info(request,"Invalid Account")
        #return redirect("forgotpass")
        return render(request,"Error_Forgot.html")
    #####################################End Code############################

def some_view(request):
    # Create a file-like buffer to receive PDF data.
    buffer = io.BytesIO()

    # Create the PDF object, using the buffer as its "file."
    p = canvas.Canvas(buffer)


    # Draw things on the PDF. Here's where the PDF generation happens.
    # See the ReportLab documentation for the full list of functionality.
    data=LeaveData.objects.filter(Email="Dhurub.saxena@iwebservices.com")
    p.drawString(100, 100, data)

    # Close the PDF object cleanly, and we're done.
    p.showPage()
    p.save()

    # FileResponse sets the Content-Disposition header so that browsers
    # present the option to save the file.
    buffer.seek(0)
    return FileResponse(buffer, as_attachment=True, filename='hello.pdf')

def CompApp(request):
    data=User.objects.filter(username=request.user).values('first_name','email')
    Project=CurrentProject.objects.all()
    return render(request,'Comp_off.html',{'data':data,'Project':Project})

def SubCompoff(request):
        #Name=request.POST['uname']
        #Email=request.POST['email']
        Contact=request.POST['cnct']
        From=request.POST['From']
        print("From:",From)
        To=request.POST['To']
        Project_Name=request.POST['select']
        Select_Department=request.POST['DepartSelect']
        Reason=request.POST['reason']
        Emp_Manager = Employee.objects.filter(Emp_id_id = request.user).values('Manager_id')
        for Manager in Emp_Manager:
            Manager_id=Manager['Manager_id']
        Dept_id=Employee.objects.filter(Emp_Email=request.user.username).values('Department_id')
        for user_Dept in Dept_id:
            Correct_Dept=user_Dept['Department_id']
        #print("Z:",Correct_Dept)
        Dept=Department.objects.filter(Department_id=Correct_Dept).values('Department_Name')
        for Dept_Name in Dept:
            Correct_DeptName=Dept_Name['Department_Name']
        user = request.user
        date_format = "%Y-%m-%d"
        a = datetime.datetime.strptime(str(From), date_format)
        b = datetime.datetime.strptime(str(To), date_format)
        today = datetime.datetime.today().strftime ('%Y-%m-%d')
        Current_Date_Formatted=a.strftime ('%Y-%m-%d')
        if b>a and Current_Date_Formatted<=today:
            delta = b - a
            days=delta.days
            #print("Days:",days)
        else:
            messages.info(request,"Invalid Dates Entered Please Go back and Check Dates First")
            return redirect('Error')
        ####################################
        myfromdate=str(a)
        #datetime.datetime.strptime(myfromdate, "%Y-%m-%d")
        dt = datetime.datetime.strptime(myfromdate,'%Y-%m-%d %H:%M:%S')
        dd=dt.date()
        print(dd)
        myfromdate=str(dd)
        mytodate=str(b)
        dy = datetime.datetime.strptime(mytodate,'%Y-%m-%d %H:%M:%S')
        ddate=dy.date()
        mytodate=str(ddate)
        #print("FromDate:",myfromdate)
        year, month, day = (int(i) for i in myfromdate.split('-'))
        year1, month1, day1 = (int(j) for j in mytodate.split('-'))
        check = datetime.date(year, month, day)
        check1 = datetime.date(year1, month1, day1)
        fromday=check.strftime("%A")
        leavetoday=check1.strftime("%A")
        if fromday=="Sunday" or fromday=="Saturday":
            if Correct_DeptName==Select_Department:
                complete=CompoffData.objects.create(Name=request.user.first_name,Email=request.user.email,Contact=Contact,From_Date=From,To_Date=To,Project_Name=Project_Name,Department=Select_Department,Reason=Reason,No_Days=days,Manager_Id_id=Manager_id)
                # Update_Bal.save()
                #email=request.user
                #email=str(email)
                #msg=LeaveData.objects.create(Name=request.user.first_name,Email=email,Contact=Contact,From_Date=From,To_Date=To,Project_Name=Project_Name,Department=Select_Department,Reason=Reason,No_Days=days,Manager_Id_id=Manager_id)
                complete.save()
                messages.info(request,"Application Submitted Sucessfully Go and Check in Status Window")
                return redirect('Sucess')
            else:
                messages.info(request,"You are not belong to this Department")
                return redirect('Error')
        else:
            messages.info(request,"You can not appply Compoff for Weekdays")
            return redirect('Error')
    








        

