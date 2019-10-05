from django.db import models

# Create your models here.
class bhayander_kinderGarten_english(models.Model):
    image=models.FileField()
    date=models.CharField(max_length=20)
    time=models.CharField(max_length=15)
    name=models.CharField(max_length=50)
    discription=models.TextField()
    url=models.CharField(max_length=1500)

class bhayander_kinderGarten_english_teacher(models.Model):
    image=models.FileField()
    name=models.CharField(max_length=50)
    discription=models.TextField()
    designation=models.CharField(max_length=50)
    url=models.CharField(max_length=1500)

class bhayander_kinderGarten_hindi(models.Model):
    image=models.FileField()
    date=models.CharField(max_length=20)
    time=models.CharField(max_length=15)
    name=models.CharField(max_length=50)
    discription=models.TextField()
    url=models.CharField(max_length=1500)

class bhayander_kinderGarten_hindi_teacher(models.Model):
    image=models.FileField()
    name=models.CharField(max_length=50)
    discription=models.TextField()
    designation=models.CharField(max_length=50)
    url=models.CharField(max_length=1500)

class bhayander_primary_english(models.Model):
    image=models.FileField()
    date=models.CharField(max_length=20)
    time=models.CharField(max_length=15)
    name=models.CharField(max_length=50)
    discription=models.TextField()
    url=models.CharField(max_length=1500)

class bhayander_primary_english_teacher(models.Model):
    image=models.FileField()
    name=models.CharField(max_length=50)
    discription=models.TextField()
    designation=models.CharField(max_length=50)
    url=models.CharField(max_length=1500)

class bhayander_secondary_english(models.Model):
    image=models.FileField()
    date=models.CharField(max_length=20)
    time=models.CharField(max_length=15)
    name=models.CharField(max_length=50)
    discription=models.TextField()
    url=models.CharField(max_length=1500)

class bhayander_secondary_english_teacher(models.Model):
    image=models.FileField()
    name=models.CharField(max_length=50)
    discription=models.TextField()
    designation=models.CharField(max_length=50)
    url=models.CharField(max_length=1500)

class bhayander_primary_hindi(models.Model):
    image=models.FileField()
    date=models.CharField(max_length=20)
    time=models.CharField(max_length=15)
    name=models.CharField(max_length=50)
    discription=models.TextField()
    url=models.CharField(max_length=1500)

class bhayander_primary_hindi_teacher(models.Model):
    image=models.FileField()
    name=models.CharField(max_length=50)
    discription=models.TextField()
    designation=models.CharField(max_length=50)
    url=models.CharField(max_length=1500)

class bhayander_secondary_hindi(models.Model):
    image=models.FileField()
    date=models.CharField(max_length=20)
    time=models.CharField(max_length=15)
    name=models.CharField(max_length=50)
    discription=models.TextField()
    url=models.CharField(max_length=1500)

class bhayander_secondary_hindi_teacher(models.Model):
    image=models.FileField()
    name=models.CharField(max_length=50)
    discription=models.TextField()
    designation=models.CharField(max_length=50)
    url=models.CharField(max_length=1500)

class bhayander_juniorCollege(models.Model):
    image=models.FileField()
    date=models.CharField(max_length=20)
    time=models.CharField(max_length=15)
    name=models.CharField(max_length=50)
    discription=models.TextField()
    url=models.CharField(max_length=1500)

class bhayander_juniorCollege_teacher(models.Model):
    image=models.FileField()
    name=models.CharField(max_length=50)
    discription=models.TextField()
    designation=models.CharField(max_length=50)
    url=models.CharField(max_length=1500)

class nalasopara_kinderGarten(models.Model):
    image=models.FileField()
    date=models.CharField(max_length=20)
    time=models.CharField(max_length=15)
    name=models.CharField(max_length=50)
    discription=models.TextField()
    url=models.CharField(max_length=1500)

class nalasopara_kinderGarten_teacher(models.Model):
    image=models.FileField()
    name=models.CharField(max_length=50)
    discription=models.TextField()
    designation=models.CharField(max_length=50)
    url=models.CharField(max_length=1500)

class nalasopara_primary_hindi(models.Model):
    image=models.FileField()
    date=models.CharField(max_length=20)
    time=models.CharField(max_length=15)
    name=models.CharField(max_length=50)
    discription=models.TextField()
    url=models.CharField(max_length=1500)

class nalasopara_primary_hindi_teacher(models.Model):
    image=models.FileField()
    name=models.CharField(max_length=50)
    discription=models.TextField()
    designation=models.CharField(max_length=50)
    url=models.CharField(max_length=1500)

class nalasopara_secondary_hindi(models.Model):
    image=models.FileField()
    date=models.CharField(max_length=20)
    time=models.CharField(max_length=15)
    name=models.CharField(max_length=50)
    discription=models.TextField()
    url=models.CharField(max_length=1500)

class nalasopara_secondary_hindi_teacher(models.Model):
    image=models.FileField()
    name=models.CharField(max_length=50)
    discription=models.TextField()
    designation=models.CharField(max_length=50)
    url=models.CharField(max_length=1500)
    
class nalasopara_primary_english(models.Model):
    image=models.FileField()
    date=models.CharField(max_length=20)
    time=models.CharField(max_length=15)
    name=models.CharField(max_length=50)
    discription=models.TextField()
    url=models.CharField(max_length=1500)

class nalasopara_primary_english_teacher(models.Model):
    image=models.FileField()
    name=models.CharField(max_length=50)
    discription=models.TextField()
    designation=models.CharField(max_length=50)
    url=models.CharField(max_length=1500)
    
    
class virar_primary_hindi(models.Model):
    image=models.FileField()
    date=models.CharField(max_length=20)
    time=models.CharField(max_length=15)
    name=models.CharField(max_length=50)
    discription=models.TextField()
    url=models.CharField(max_length=1500)

class virar_primary_hindi_teacher(models.Model):
    image=models.FileField()
    name=models.CharField(max_length=50)
    discription=models.TextField()
    designation=models.CharField(max_length=50)
    url=models.CharField(max_length=1500)

class virar_secondary_hindi(models.Model):
    image=models.FileField()
    date=models.CharField(max_length=20)
    time=models.CharField(max_length=15)
    name=models.CharField(max_length=50)
    discription=models.TextField()
    url=models.CharField(max_length=1500)

class virar_secondary_hindi_teacher(models.Model):
    image=models.FileField()
    name=models.CharField(max_length=50)
    discription=models.TextField()
    designation=models.CharField(max_length=50)
    url=models.CharField(max_length=1500)

class bhayander_achivement(models.Model):
    name=models.CharField(max_length=50)
    achive=models.CharField(max_length=50)
    discription=models.TextField()
    image=models.FileField()
    url=models.CharField(max_length=1500)

class bhayander_management(models.Model):
    image=models.FileField()
    name=models.CharField(max_length=50)
    discription=models.TextField()
    designation=models.CharField(max_length=50)
    url=models.CharField(max_length=1500)

class bhayander_event(models.Model):
    image=models.FileField()
    date=models.CharField(max_length=20)
    time=models.CharField(max_length=15)
    name=models.CharField(max_length=50)
    discription=models.TextField()
    url=models.CharField(max_length=1500)

class bhayander_facility(models.Model):
    image=models.FileField()
    name=models.CharField(max_length=50)
    discription=models.TextField()
    url=models.CharField(max_length=1500)

class nalasopara_achivement(models.Model):
    name=models.CharField(max_length=50)
    achive=models.CharField(max_length=50)
    discription=models.TextField()
    image=models.FileField()
    url=models.CharField(max_length=1500)

class nalasopara_management(models.Model):
    image=models.FileField()
    name=models.CharField(max_length=50)
    discription=models.TextField()
    designation=models.CharField(max_length=50)
    url=models.CharField(max_length=1500)

class nalasopara_event(models.Model):
    image=models.FileField()
    date=models.CharField(max_length=20)
    time=models.CharField(max_length=15)
    name=models.CharField(max_length=50)
    discription=models.TextField()
    url=models.CharField(max_length=1500)

class nalasopara_facility(models.Model):
    image=models.FileField()
    name=models.CharField(max_length=50)
    discription=models.TextField()
    url=models.CharField(max_length=1500)

class virar_achivement(models.Model):
    name=models.CharField(max_length=50)
    achive=models.CharField(max_length=50)
    discription=models.TextField()
    image=models.FileField()
    url=models.CharField(max_length=1500)

class virar_management(models.Model):
    image=models.FileField()
    name=models.CharField(max_length=50)
    discription=models.TextField()
    designation=models.CharField(max_length=50)
    url=models.CharField(max_length=1500)

class virar_event(models.Model):
    image=models.FileField()
    date=models.CharField(max_length=20)
    time=models.CharField(max_length=15)
    name=models.CharField(max_length=50)
    discription=models.TextField()
    url=models.CharField(max_length=1500)

class virar_facility(models.Model):
    image=models.FileField()
    name=models.CharField(max_length=50)
    discription=models.TextField()
    url=models.CharField(max_length=1500)
