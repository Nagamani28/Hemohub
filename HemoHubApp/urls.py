from django.urls import path
from HemoHubApp import views

urlpatterns = [
    path('', views.index, name='index'),
    path('index.html', views.home, name='home'),
    path('about.html', views.about, name='about'),
    path('contact.html', views.contact, name='contact'),
    path('signup.html', views.signup, name='signup'),
    path('company_login.html', views.company_login, name='company_login'),
    path('redcross.html', views.redcross, name='redcross'),
    path('redcross_dashboard.html', views.redcross_dashboard, name='redcross_dashboard'),
    path('redcross_donors_list.html', views.redcross_donors_list, name='redcross_donors_list'),
    path('redcross_blood_stock.html', views.redcross_blood_stock, name='redcross_blood_stock'),
    path('redcross_donor_registration.html', views.redcross_donor_registration, name='redcross_donor_registration'),
    path('redcross_request_blood.html', views.redcross_request_blood, name='redcross_request_blood'),
    path('redcross_blood_donation_camps.html', views.redcross_blood_donation_camps, name='redcross_blood_donation_camps'),
    path('redcross_about.html', views.redcross_about, name='redcross_about'),
    path('redcross_contact.html', views.redcross_contact, name='redcross_contact'),
    path('redcross_profile.html', views.redcross_profile, name='redcross_profile'),
    path('redcross_logout.html', views.redcross_logout, name='redcross_logout'),
    path('dummy_dashboard.html', views.dummy_dashboard, name='dummy_dashboard'),
   ## path('accept_notification/<int:notification_id>/', views.accept_notification, name='accept_notification'),
   # path('reject_notification/<int:notification_id>/', views.reject_notification, name='reject_notification'),

    path('company1_dashboard.html', views.company1_dashboard, name='company1_dashboard'),
    path('company1_donors_list', views.company1_donors_list, name='company1_donors_list'),
    path('company1_blood_stock.html', views.company1_blood_stock, name='company1_blood_stock'),
    path('company1_donor_registration.html', views.company1_donor_registration, name='company1_donor_registration'),
    path('company1_request_blood.html', views.company1_request_blood, name='company1_request_blood'),
    path('company1_blood_donation_camps.html', views.company1_blood_donation_camps, name='company1_blood_donation_camps'),
    path('company1_about.html', views.company1_about, name='company1_about'),
    path('company1_contact.html', views.company1_contact, name='company1_contact'),
    path('company1_profile.html', views.company1_profile, name='company1_profile'),
    path('company1_logout.html', views.company1_logout, name='company1_logout'),

    path('company2_dashboard.html', views.company2_dashboard, name='company2_dashboard'),
    path('company2_donors_list.html', views.company2_donors_list, name='company2_donors_list'),
    path('company2_blood_stock.html', views.company2_blood_stock, name='company2_blood_stock'),
    path('company2_donor_registration.html', views.company2_donor_registration, name='company2_donor_registration'),
    path('company2_request_blood.html', views.company2_request_blood, name='company2_request_blood'),
    path('company2_blood_donation_camps.html', views.company2_blood_donation_camps, name='company2_blood_donation_camps'),
    path('company2_about.html', views.company2_about, name='company2_about'),
    path('company2_contact.html', views.company2_contact, name='company2_contact'),
    path('company2_profile.html', views.company2_profile, name='company2_profile'),
    path('company2_logout.html', views.company2_logout, name='company2_logout'),
    path('notification/accept/<int:notification_id>/', views.accept_notification, name='accept_notification'),
    path('notification/reject/<int:notification_id>/', views.reject_notification, name='reject_notification'),
]