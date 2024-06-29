from django.db import models

# Create your models here.
class student(models.Model):
    StudentName = models.CharField(max_length = 20)
    RollNumber = models.CharField(max_length = 20)
    Email = models.CharField(max_length = 50)
    Branch = models.CharField(max_length = 20)
    Password = models.CharField(max_length = 20)
class teacher(models.Model):
    Name = models.CharField(max_length = 20)
    Email = models.CharField(max_length = 50)
    Course_code = models.CharField(max_length = 50)
    Course = models.CharField(max_length = 50)
    Password = models.CharField(max_length = 20)
# class adminreg(models.Model):
#     username = models.CharField(max_length = 20)
#     pwd = models.CharField(max_length = 20)


class complaint(models.Model):
    Name = models.CharField(max_length=20)
    email = models.EmailField(max_length=50)
    Complaint = models.CharField(max_length=50)

# class product(models.Model):
#     product_id = models.CharField(max_length = 20)
#     product_name = models.CharField(max_length = 20)
#     description = models.CharField(max_length = 30)
#     category = models.CharField(max_length = 10)
#     quantity = models.IntegerField()
#     price = models.IntegerField()
#     image = models.ImageField()
#     status = models.CharField(max_length = 30)
class hod(models.Model):
    Name = models.CharField(max_length = 20)
    Email = models.CharField(max_length = 50)
    Department = models.CharField(max_length = 50)
    Password = models.CharField(max_length = 20)

class Questions(models.Model):
    student_dtls = models.ForeignKey(student,on_delete=models.CASCADE,null = True)
    question = models.CharField(max_length= 50)
    OPTION_CHOICES=(
        ('good','Good'),
        ('average', 'Average'),
        ('poor','Poor'),
    )
    options = models.CharField(max_length=15, choices=OPTION_CHOICES,null = True)   