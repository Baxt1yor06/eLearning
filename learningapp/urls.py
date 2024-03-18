from django.urls import path
from .views import index, about, courses, team, testimonial, contact, error, \
    detail1, detail3, detail4, detail5, detail6, detail7, \
    CarouselDeleteView, CarouselUpdateView, AboutDeleteView, AboutUpdateView, CoursesDeleteView, CoursesUpdateView, \
    PopularDeleteView, PopularUpdateView, InstructorsDeleteView, InstructorsUpdateView, ClientDeleteView, ClientUpdateView


urlpatterns = [


# Base urls
    
    path('', index, name='index'),
    path('about', about, name='about'),
    path('courses', courses, name='courses'),
    path('our_team', team, name='team'),
    path('404-Error', error, name='error'),
    path('contact', contact, name='contact'),
    path('testimonial', testimonial, name='testimonial'),

# Details urls

    path('home1/<slug:home1>', detail1, name='detail1'),
    path('home3/<slug:home3>', detail3, name='detail3'),
    path('home4/<slug:home4>', detail4, name='detail4'),
    path('home5/<slug:home5>', detail5, name='detail5'),
    path('home6/<slug:home6>', detail6, name='detail6'),
    path('home7/<slug:home7>', detail7, name='detail7'),
# Change urls

    path('home1/update/<slug>/', CarouselUpdateView.as_view(), name='CarouselUpdateView'),
    path('home1/delete/<slug>/', CarouselDeleteView.as_view(), name='CarouselDeleteView'),
    path('home3/update/<slug>/', AboutUpdateView.as_view(), name='AboutUpdateView'),
    path('home3/delete/<slug>/', AboutDeleteView.as_view(), name='AboutDeleteView'),
    path('home4/update/<slug>/', CoursesUpdateView.as_view(), name='CoursesUpdateView'),
    path('home4/delete/<slug>/', CoursesDeleteView.as_view(), name='CoursesDeleteView'),
    path('home5/update/<slug>/', PopularUpdateView.as_view(), name='PopularUpdateView'),
    path('home5/delete/<slug>/', PopularDeleteView.as_view(), name='PopularDeleteView'),
    path('home6/update/<slug>/', InstructorsUpdateView.as_view(), name='InstructorsUpdateView'),
    path('home6/delete/<slug>/', InstructorsDeleteView.as_view(), name='InstructorsDeleteView'),
    path('home7/update/<slug>/', ClientUpdateView.as_view(), name='ClientUpdateView'),
    path('home7/delete/<slug>/', ClientDeleteView.as_view(), name='ClientDeleteView'),


]
