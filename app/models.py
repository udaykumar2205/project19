from django.db import models

# Create your models here.
class Department(models.Model):
   deptno = models.IntegerField(unique=True)  
   deptname = models.CharField(max_length=100) 
   loc = models.CharField(max_length=100) 
    
class Employee(models.Model):
    empno = models.IntegerField(primary_key=True)  
    empname = models.CharField(max_length=100)  
    job = models.CharField(max_length=100)  
    hiredate = models.DateField()  
    sal = models.DecimalField(max_digits=10, decimal_places=3)  
    mgr = models.ForeignKey('self', on_delete=models.SET_NULL, null=True, blank=True)  
    comm = models.DecimalField(max_digits=10, decimal_places=3, null=True, blank=True)  
    deptno = models.ForeignKey(Department, on_delete=models.CASCADE)  