from django.conf.urls import url
from django.urls import path
from . import views
urlpatterns = [
    
    path('login',views.login,name="login"),
    path('home',views.home,name="home"),
    path('logout',views.logout,name="logout"),
    path('Leave',views.Leave,name="Leave"),
    path('Policy',views.Policy,name="Policy"),
    path('Balance',views.LeaveBalance,name="Balance"),
    path('Back',views.Back,name="Back"),
    path('LeaveApp',views.LeaveApp,name="LeaveApp"),
    path('History',views.LeaveHistory,name="History"),
    path('Error',views.Error,name="Error"),
    path('Goback',views.Goback,name="Goback"),
    path('Sucess',views.Sucess,name="Sucess"),
    path('SubGoback',views.SubGoback,name="SubGoback"),
    path('LeaveError',views.LeaveError,name="LeaveError"),
    path('Leaverequest',views.LeavePending,name="Leaverequest"),
    path('LeaveApprove',views.LeaveApprove,name="LeaveApprove"),
    path('LeaveReject',views.LeaveReject,name="LeaveReject"),
    path('LeaveForword',views.LeaveForword,name="LeaveForword"),
    path('ForwordedApprove',views.ForwordedApprove,name="ForwordedApprove"),
    path('ForwordedReject',views.ForwordedReject,name="ForwordedReject"),
    path('ForwordedRequest',views.ForwordedRequest,name="ForwordedRequest"),
    path('ChangePassword',views.ChangePassword,name="ChangePassword"),
    path('Changepass',views.Changepass,name="Changepass"),
    path('festival',views.festival,name="festival"),
    path('forgot',views.Forgot,name="forgot"),
    path('forgotpass',views.ForgotPass,name="forgotpass"),
    path('some_view',views.some_view,name="some_view"),
    path('CompApp',views.CompApp,name="CompApp"),
    path('SubCompoff',views.SubCompoff,name="SubCompoff"),
    path('test',views.test,name="test"),#test
    #url(r'^(?P<question_id>\d+)/Leaverequest/$', views.LeavePending, name='Leaverequest'),
]
