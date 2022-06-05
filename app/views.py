from django.shortcuts import render,redirect
from .models import *
from django.contrib import messages
from random import randint
# Create your views here.

def indexPage(request):
    return render(request,'index.html')

# Sign up process
def signUp(request):
    if request.method == 'POST':
        if request.POST['role'] == "1":
            role = request.POST['role']
            firstname = request.POST['firstname']
            lastname = request.POST['lastname']
            email = request.POST['email']
            password = request.POST['password']
            cpassword = request.POST['cpassword']
            
            user = UserMaster.objects.filter(email=email)
            if user:
                messages.error(request, "This email has been already registered.")
                return render(request, 'signup.html')
            else:
                if password == cpassword:
                    otp = randint(100000, 999999)
                    newuser = UserMaster(role=role, email=email, password=password,otp=otp)
                    newcand = Candidate(firstname=firstname, lastname=lastname)
                    return render(request, 'otp.html')

                else:
                    messages.error(request, "Password doesn not match.")
                    return render(request, 'signup.html')

        else:
            role = request.POST['role']
            firstname = request.POST['firstname']
            lastname = request.POST['lastname']
            email = request.POST['email']
            password = request.POST['password']
            cpassword = request.POST['cpassword']

            user = UserMaster.objects.filter(email=email)
            if user:
                messages.error(request, "This email has been already registered")
                return render(request, 'signup.html')

            else:
                if password == cpassword:
                    otp = randint(100000, 999999)
                    newuser = UserMaster(role=role, email=email, password=password,otp=otp)
                    newuser.save()
                    newcand = Company(user_id=newuser,firstname=firstname, lastname=lastname)
                    newcand.save()
                    return render(request, 'otp.html' ,{'email':email})

                else:
                    messages.error(request, "Password doesn not match.")
                    return render(request, 'signup.html')

    return render(request, 'signup.html')

#OTP verification process
def otpVerify(request):
    if request.method == 'POST':
        email = request.POST['email']
        otp = int(request.POST['otp'])

        user = UserMaster.objects.filter(email=email)
        if user:
            user = UserMaster.objects.get(email=email)
            if user.otp == otp:
                messages.success(request,"OTP verified succesfully.")
                return render(request,'login.html')

            else:
                messages.error(request,"OTP is incorrect.")
                return render(request,'otp.html')

        else:
            messages.error(request, "User not found.")
            return render(request,'signup.html')
    return render(request, 'otp.html')


### Login process

def logIn(request):
    if request.method =='POST':
        if request.POST['loginrole']=="1":
            role = request.POST['loginrole']
            email =request.POST['loginemail']
            password =request.POST['loginpassword']

            user = UserMaster.objects.filter(email=email)

            if user:
                user = UserMaster.objects.get(email=email)
                if user.password==password and user.role==role:
                    can = Candidate.objects.get(user_id=user)
                    request.session['id']=user.id
                    request.session['firstname']=can.firstname
                    request.session['lastname']=can.lastname
                    request.session['role']=user.role
                    request.session['password']=user.password
                    request.session['email']=user.email
                    return redirect('index')
                else:
                    messages.error(request,"Password does not match.")
                    return render(request,'login.html')

            else:
                messages.error(request, "Email is invalid.")
                return render(request,'login.html')

        else:
        
            if request.POST['loginrole']=="2":
                role = request.POST['loginrole']
                email =request.POST['loginemail']
                password =request.POST['loginpassword']

                user = UserMaster.objects.filter(email=email)

                if user:
                    user = UserMaster.objects.get(email=email)
                    if user.password==password and user.role==role:
                        can = Company.objects.get(user_id=user)
                        request.session['id']=user.id
                        request.session['firstname']=can.firstname
                        request.session['lastname']=can.lastname
                        request.session['role']=user.role
                        request.session['password']=user.password
                        request.session['email']=user.email
                        return redirect('companyindex')
                    else:
                        messages.error(request,"Password does not match.")
                        return render(request,'login.html')

                else:
                    messages.error(request, "Email is invalid.")
                    return render(request,'login.html')
    return render(request, 'login.html')


def profile(request,pk):
    user = UserMaster.objects.get(pk=pk)
    can = Candidate.objects.get(user_id=user)
    if request.method=='POST':
        can.jobtype = request.POST['jobtype']
        can.job_category = request.POST['jobcategory']
        can.city = request.POST['city']
        can.state = request.POST['jobtype']
        can.min_salary = request.POST['minsalary']
        can.max_salary = request.POST['maxsalary']
        can.education = request.POST['education']
        can.experience = request.POST['experience']
        can.contact = request.POST['phone']
        can.gender = request.POST['gender']
        can.job_description = request.POST['jobdescription']
        can.profile_pic = request.POST['upload']
        can.firstname = request.POST['firstname']
        can.lastname = request.POST['lastname']
        
        can.save()
    
    return render(request, 'profile.html',{'user':user,'can':can}) 

def logout(request):
    del request.session['email']
    del request.session['password']
    del request.session['id']
    del request.session['firstname']
    del request.session['lastname']
    del request.session['role']
    return redirect('index')

def candidateJobPostList(request):
    jobposts = JobDetails.objects.all()
    return render(request,'job-list.html',{'jobposts':jobposts})


def applyJob(request,pk):
    user = request.session['id']
    can = Candidate.objects.get(user_id=user)
    job = JobDetails.objects.get(id=pk)
    if request.method=='POST':
        education = request.POST['education']
        city = request.POST['city']
        state = request.POST['state']
        email = request.POST['email']
        experience = request.POST['experience']
        gender  = request.POST['gender']
        resume = request.FILES['resume']

        newapply = ApplyJob(candidate=can,job=job,state=state,city=city,email=email,education=education,experience=experience,gender=gender,resume=resume)
        newapply.save()
        return redirect('candidatejobpostlist')
    return render(request,'applyjob.html',{'user':user,'can':can,'job':job})



######################## Company Views ##################################

def companyIndexPage(request):
    return render(request,'company/index.html')

#### Company Profile
def cprofile(request,pk):
    user = UserMaster.objects.get(pk=pk)
    comp = Company.objects.get(user_id=user)
    if request.method=='POST':
        comp.firstname=request.POST['firstname']
        comp.lastname=request.POST['lastname']
        comp.company=request.POST['company']
        comp.company_description=request.POST['companydescription']
        comp.contact=request.POST['contact']
        comp.state=request.POST['state']
        comp.city=request.POST['city']
        comp.address=request.POST['address']
        comp.save()

    return render(request, 'company/cprofile.html', {'user':user, 'comp':comp}) 



def jobPost(request,pk):
    if request.method =="POST":

        user = UserMaster.objects.get(pk=pk)
        comp = Company.objects.get(user_id=user)

        jobname = request.POST['jobname']
        companyname = request.POST['companyname']
        companyaddress = request.POST['companyaddress']
        qualification = request.POST['qualification']
        responsibilities = request.POST['responsibilities']
        location = request.POST['location']
        companywebsite = request.POST['companywebsite']
        companyemail = request.POST['companyemail']
        companycontact = request.POST['companycontact']
        salary = request.POST['salary']
        experience = request.POST['experience']
        jobdescription = request.POST['jobdescription']

        if jobname and companyname and companycontact and companyemail and companyaddress and qualification:
            post = JobDetails(company_id=comp,job_name=jobname, company_name=companyname, company_address=companyaddress, qualification=qualification, resposibilities=responsibilities, location=location, company_website=companywebsite, company_email=companyemail, company_contact=companycontact, salary =salary,experience=experience, job_description=jobdescription)
            post.save()
            messages.success(request," Job Posted Successfully.")
            return render(request, 'company/jobpost.html')

        else:
            messages.error(request, "Please Fill The Form.")
            return render(request, 'company/jobpost.html')
    return render(request, 'company/jobpost.html')


def jobPostList(request):
    jobposts = JobDetails.objects.all()
    return render(request,'company/jobpostlist.html',{'jobposts':jobposts})


def jobapplylist(request):
    applyjobs = ApplyJob.objects.all()
    return render(request,'company/jobapplylist.html',{'applyjobs':applyjobs})



########################### Page Linking ##############################


def about(request):
    return render(request,'about.html')

def services(request):
    return render(request,'services.html')

def team(request):
    return render(request,'team.html')

def faq(request):
    return render(request,'faq.html')

def pricing(request):
    return render(request,'pricing.html')

def contact(request):
    return render(request,'contact.html')