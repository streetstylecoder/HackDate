from django.contrib import admin
from django.conf import settings
from django.urls import path, include
from django.conf.urls.static import static

from main.views import IndexPageView, ChangeLanguageView
from hackathons.views import hack_submit, fest_submit, Es_submit,events,home,teamsearch,addteamreq,team_analysis,maketeamreq,myteamrequests,swipecards,hackregister

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', IndexPageView.as_view(), name='index'),

    path('i18n/', include('django.conf.urls.i18n')),
    path('language/', ChangeLanguageView.as_view(), name='change_language'),

    path('accounts/', include('accounts.urls')),
    path('events/hack_submit',hack_submit, name='hack_reg'),
    path('fest_submit',fest_submit, name='fest_reg'),
    path('events/es_submit',Es_submit, name='es_reg'),
    path('events/',events, name='events'),
    path('home/',home,name="home"),
    path('teamsrch',teamsearch,name="teamsearch"),
    path('addteamreq/',addteamreq,name="addteamreq"),
    path('team_analysis/<str:slug>/', team_analysis, name='team_analysis'),
    path('teamsrch/team_analysis/<str:slug>/', team_analysis, name='team_analysis'),
    path('maketeamreq/<str:slug>/', maketeamreq, name='maketeamreq'),
    path('myteamrequests/', myteamrequests, name='myteamrequests'),
    path('swipecards',swipecards,name="swipecards"),
     path('hackregister/<str:slug>/', hackregister, name='hackregister'),
    

    
    
]

if settings.DEBUG:  
        urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)  