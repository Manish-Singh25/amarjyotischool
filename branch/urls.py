from django.urls import path
from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
    path('bhayander/',views.bhayander_index,name="bhayander_index"),
    path('nalasopara/',views.nalasopara_index,name="nalasopara_index"),
    path('virar/',views.virar_index,name="virar_index"),
    path('bhayander_kinderGarten/',views.bhayander_course_kinderGarten,name="bhayander_course_kinderGarten"),
    path('bhayander_course_primary/',views.bhayander_course_primary,name="bhayander_course_primary"),
    path('bhayander_course_secondary/',views.bhayander_course_secondary,name="bhayander_course_secondary"),
    path('bhayander_course_college/',views.bhayander_course_college,name="bhayander_course_college"),
    path('nalasopara_kinderGarten/',views.nalasopara_course_kinderGarten,name="nalasopara_course_kinderGarten"),
    path('nalasopara_course_primary/',views.nalasopara_course_primary,name="nalasopara_course_primary"),
    path('nalasopara_course_secondary/',views.nalasopara_course_secondary,name="nalasopara_course_secondary"),
    path('virar_course_primary/',views.virar_course_primary,name="virar_course_primary"),
    path('virar_course_secondary/',views.virar_course_secondary,name="virar_course_secondary"),
    url(r'^',views.branch_url_redirect),
]