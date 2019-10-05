from django.urls import path
from . import views
from django.conf.urls import url
from django.conf import settings


urlpatterns=[
    path('dashboard/',views.dashboard,name="dashboard"),
    path('alumini/',views.alumini,name="alumini"),
    path('joinus/',views.joinUs,name="joinUs"),
    path('aboutus/',views.aboutUs,name="aboutUs"),
    path('contactus/',views.contactUs,name="contactUs"),
    path('login/',views.login,name="login"),
    path('student_join/',views.students_join,name="student_join"),
    path('teacher_join/',views.teachers_join,name="teacher_join"),
    path('signup/',views.signup,name="signup"),
    path('authenticate/',views.authenticate,name="authenticate"),
    url(r'^',views.url_redirect),
]