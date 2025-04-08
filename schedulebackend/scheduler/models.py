from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify
from django.core.validators import MaxValueValidator, MinValueValidator
from django.utils.translation import gettext_lazy as _

import datetime as dt    

class Term(models.Model):
    code = models.CharField(max_length=20, unique=True)
    name = models.CharField(max_length=256)
    by_month = models.IntegerField(
        default=4,
        validators=[MinValueValidator(1), MaxValueValidator(12)]
    )
    max_hours = models.IntegerField(
        default=192,
        validators=[MinValueValidator(0), MaxValueValidator(4000)]
    )
    
    def __str__(self):
        return self.code

class CourseCode(models.Model):
    """ Create a CourseCode model """
    name = models.CharField(max_length=5, unique=True)
    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name

class CourseNumber(models.Model):
    """ Create a CourseNumber model """
    name = models.CharField(max_length=5, unique=True)
    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name

class CourseSection(models.Model):
    """ Create a CourseSection model """
    name = models.CharField(max_length=12, unique=True)
    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name
    
class CourseName(models.Model):
    name = models.CharField(max_length=50, unique=True)
    
    class Meta:
        ordering = ['name']
        
    def __str__(self):
        return self.name

class Time(models.Model):
    time = models.CharField(max_length=10, unique=True)
    
    class Meta:
        ordering = ['time']
        
    def __str__(self):
        return self.time

class Day(models.Model):
    day = models.CharField(max_length=10, unique=True)
    
    class Meta:
        ordering = ['day']
        
    def __str__(self):
        return self.day



class Course(models.Model):
    term = models.ForeignKey(Term, on_delete=models.DO_NOTHING)
    code = models.ForeignKey(CourseCode, on_delete=models.DO_NOTHING)
    name = models.ForeignKey(CourseName, on_delete=models.DO_NOTHING)
    number = models.ForeignKey(CourseNumber, on_delete=models.DO_NOTHING)
    section = models.ForeignKey(CourseSection, on_delete=models.DO_NOTHING)
    start = models.ForeignKey(Time, on_delete=models.DO_NOTHING, related_name='courses_start')
    end = models.ForeignKey(Time, on_delete=models.DO_NOTHING, related_name='courses_end')
    day = models.ForeignKey(Day, on_delete=models.DO_NOTHING)
    slug = models.SlugField(max_length=256, unique=True)
    
    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.code.name  + ' ' + self.number.name + ' ' + self.section.name + ' ' + self.name + ' ' + self.term.code)
        super(Course, self).save(*args, **kwargs)


class Program(models.Model):
    short_code = models.CharField(max_length=5, unique=True)
    full_name = models.CharField(max_length=50, unique=True)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    
    
    def __str__(self):
        return self.full_name
    



    
    

    
