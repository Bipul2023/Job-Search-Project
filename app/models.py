from django.db import models

# Create your models here.

class UserMaster(models.Model):
    email = models.EmailField(max_length = 50)
    password = models.CharField(max_length = 100)
    otp = models.IntegerField()
    role = models.CharField(max_length = 30)
    is_active = models.BooleanField(default = True)
    is_verifired = models.BooleanField(default = False)
    is_updated = models.DateTimeField(auto_now_add= True)
    is_created = models.DateTimeField(auto_now_add=True)

class Candidate(models.Model):
    user_id = models.ForeignKey(UserMaster , on_delete=models.CASCADE)
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    contact = models.CharField(max_length=20)
    state = models.CharField(max_length= 50)
    city = models.CharField(max_length=100)
    jobtype = models.CharField(max_length=100,default='000000')
    job_category = models.CharField(max_length=100,default='000000')
    min_salary = models.BigIntegerField(default='000000')
    max_salary = models.BigIntegerField(default='000000')
    education = models.CharField(max_length=150,default='000000')
    experience = models.CharField(max_length=100,default='000000')
    job_description = models.TextField(default='000000')
    gender = models.CharField(max_length=50)
    profile_pic = models.ImageField(upload_to = "app/img/candidate")
    

class Company(models.Model):
    user_id = models.ForeignKey(UserMaster , on_delete=models.CASCADE)
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    company = models.CharField(max_length=100)
    company_description = models.TextField(default="0000")
    contact = models.CharField(max_length=20)
    state = models.CharField(max_length= 50)
    city = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    

class JobDetails(models.Model):
    company_id = models.ForeignKey(Company , on_delete=models.CASCADE,default='0')
    job_name = models.CharField(max_length=250)
    company_name = models.CharField(max_length=250)
    company_address = models.CharField(max_length=250)
    job_description = models.CharField(max_length=550)
    qualification = models.CharField(max_length=250)
    resposibilities = models.CharField(max_length=250)
    location = models.CharField(max_length=250)
    company_website = models.CharField(max_length=250)
    company_email = models.CharField(max_length=250)
    company_contact = models.CharField(max_length=250)
    salary = models.CharField(max_length=250)
    experience = models.CharField(max_length=250)


class ApplyJob(models.Model):
    candidate = models.ForeignKey(Candidate, on_delete=models.CASCADE)
    job = models.ForeignKey(JobDetails, on_delete=models.CASCADE)
    education = models.CharField(max_length=150)
    city = models.CharField(max_length=150)
    state = models.CharField(max_length=150)
    experience = models.CharField(max_length=150)
    gender = models.CharField(max_length=150)
    email = models.CharField(max_length=150,default='0')
    resume = models.FileField(upload_to="app/resume")