from django.urls import path
from .views import index, about, courses, team, testimonial, contact, error, \
     detail1, detail3, detail4, detail5, detail6, detail7

urlpatterns = [


    path('', index, name='index'),
    path('about', about, name='about'),
    path('courses', courses, name='courses'),
    path('our_team', team, name='team'),
    path('home3/<slug:home3>', detail3, name='detail3'),
    path('home4/<slug:home4>', detail4, name='detail4'),
    path('home5/<slug:home5>', detail5, name='detail5'),
    path('home6/<slug:home6>', detail6, name='detail6'),
    path('home7/<slug:home7>', detail7, name='detail7'),
    path('testimonial', testimonial, name='testimonial'),
    path('contact', contact, name='contact'),
    path('home1/<slug:home1>', detail1, name='detail1'),
    path('404-Error', error, name='error')

]
