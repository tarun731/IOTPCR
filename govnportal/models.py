from django.db import models

# Create your models here.
class DCPUlogin(models.Model):
    userid = models.CharField(max_length=200)
    password = models.CharField(max_length=200)

class Organization(models.Model):
    orgname = models.CharField(max_length=200)
    ownername = models.CharField(max_length=200)
    orgid = models.CharField(max_length=200)
    password = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    village = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    state = models.CharField(max_length=200)
    phoneno = models.IntegerField()

class Branches(models.Model):
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE)
    branchname = models.CharField(max_length=200)
    ownername = models.CharField(max_length=200)
    branchid = models.CharField(max_length=200)
    password = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    village = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    state = models.CharField(max_length=200)
    phoneno = models.IntegerField()
    balance = models.IntegerField(null=True)

class Children(models.Model):
    branch = models.ForeignKey(Branches, on_delete=models.CASCADE)
    childid = models.IntegerField()
    childname = models.CharField(max_length=200)
    childdob = models.DateField()
    gender = models.CharField(max_length=200)
    photo = models.ImageField(null=True)

class Attendence(models.Model):
    branch = models.ForeignKey(Branches, on_delete=models.CASCADE, null=True)
    child = models.ForeignKey(Children, on_delete=models.CASCADE, null=True)
    date = models.DateField(null=True)
    morningattendence = models.CharField(max_length=200, null=True)
    nightattendence = models.CharField(max_length=200, null=True)
    guestname = models.CharField(max_length=200, null=True)
    guestmno = models.IntegerField(null=True)
    guestintime = models.TimeField(null=True)
    guestouttime = models.TimeField(null=True)
    schoolouttime = models.TimeField(null=True)
    schoolintime = models.TimeField(null=True)
    personalvisit = models.CharField(max_length=200, null=True)
    pvouttime = models.TimeField(null=True)
    pvintime = models.TimeField(null=True)

class Problem(models.Model):
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE)
    branch = models.ForeignKey(Branches, on_delete=models.CASCADE)
    problemname = models.CharField(max_length=200)
    problemdes = models.CharField(max_length=10000)
    problemid = models.IntegerField()
    photo = models.ImageField(null=True)
    date = models.DateField()
    orgacceptance = models.CharField(max_length=100)
    solved = models.CharField(max_length=100)

class Funds(models.Model):
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE)
    branch = models.ForeignKey(Branches, on_delete=models.CASCADE)
    problem = models.ForeignKey(Problem, on_delete=models.CASCADE, null=True)
    fundid = models.IntegerField()
    fundfor = models.CharField(max_length=200)
    fundraisedby = models.CharField(max_length=200)
    amount = models.IntegerField()
    paymentmode = models.CharField(max_length=200)
    paymentimage = models.ImageField()
    date = models.DateField(null=True)
    balance = models.IntegerField(null=True)
    completestatus = models.CharField(max_length=200, null=True)

class Problemsolution(models.Model):
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE)
    branch = models.ForeignKey(Branches, on_delete=models.CASCADE)
    problem = models.ForeignKey(Problem, on_delete=models.CASCADE)
    fund = models.ForeignKey(Funds, on_delete=models.CASCADE, null=True)
    problemsolution = models.CharField(max_length=1000)

class Donations(models.Model):
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE)
    branch = models.ForeignKey(Branches, on_delete=models.CASCADE)
    donationid = models.IntegerField(null=True)
    donorname = models.CharField(max_length=200)
    phoneno = models.CharField(max_length=200)
    address = models.CharField(max_length=500)
    informof = models.CharField(max_length=100)
    amount = models.IntegerField(null=True)
    foodtime = models.CharField(max_length=100, null=True)
    date = models.DateField(null=True)
    receipt = models.FileField()

class Fundusagebills(models.Model):
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE)
    branch = models.ForeignKey(Branches, on_delete=models.CASCADE)
    fund = models.ForeignKey(Funds, on_delete=models.CASCADE, null=True)
    amount = models.IntegerField(null=True)
    bill = models.ImageField()
    date = models.DateField(null=True)
