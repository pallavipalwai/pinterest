from django.conf.urls.static import static
from django.urls import path
from django.conf.urls import url

from pinterestapp.views.auth import *

urlpatterns=[

    path('signup/',SignUp_controller.as_view(),name="signup"),
    path('login/',Login_controller.as_view(),name="login"),
    path('logout/',Logout_controller.as_view(),name="logout"),

    path('thankyou/',thankyou.as_view(),name="thankyou"),
    path('home/',home.as_view(),name="home"),
    path('following/',following,name="following"),


    path('pins/create/', CreatePin.as_view(), name="createpin"),
    path('pin/<int:id>/',ViewPin.as_view(),name="viewpin"),

    path('profile/<str:username>/', get_user_profile, name="get_user_profile"),
    path('profile/<str:username>/pins/',ViewAllPins,name="viewallpins"),
    path('profile/<str:username>/topics/', topics, name="topics"),

    path('selecttopics/',selecttopics,name="selecttopics"),
    path('savepin/',savepin.as_view(),name="savepin"),

]

if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)