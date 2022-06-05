from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path("",views.indexPage,name="index"),
    path("signup",views.signUp,name="signup"),
    path("otpverify",views.otpVerify,name="otpverify"),
    path("login",views.logIn,name="login"),
    path("profile/<int:pk>",views.profile,name="profile"),
    path("candidatejobpostlist",views.candidateJobPostList,name="candidatejobpostlist"),
    path("logout",views.logout,name="logout"),
    path("applyjob/<int:pk>",views.applyJob,name="applyjob"),

    ####################### Company Urls ##############################
    path("companyindex",views.companyIndexPage,name="companyindex"),
    path("companyprofile/<int:pk>",views.cprofile,name="companyprofile"),
    path("jobpost/<int:pk>",views.jobPost,name="jobpost"),
    path("jobpostlist",views.jobPostList,name="jobpostlist"),
    path("jobapplylist",views.jobapplylist,name="jobapplylist"),


    ################# Page linking Urls #####################

    path("about",views.about,name="about"),
    path("services",views.services,name="services"),
    path("team",views.team,name="team"),
    path("faq",views.faq,name="faq"),
    path("pricing",views.pricing,name="pricing"),
    path("contact",views.contact,name="contact"),
]