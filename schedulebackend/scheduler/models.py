from django.db import models

class departments(models.Model):
    department_id = models.AutoField(primary_key=True)
    department_name = models.CharField(max_length=50, unique=True)
    
    class Meta:
        db_table_comment = "Departments Table"
    
    def __str__(self):
        return self.department_name
    
class courses(models.Model):
    course_code = models.CharField(max_length=20, primary_key=True, null=False)
    instructor = models.CharField(max_length=100, null=False)
    time = models.JSONField(defualt=dict, null=False) 
    # example: {"Monday": [10:00, 1], "Wednesday": [18:00, 2]}
    # first index is the time, second index is the duration in hours
    days = models.CharField(max_length=10, null=False)
    
    
    class Meta:
        db_table_comment = "Courses Table"
    
    def __str__(self):
        return f"{self.course_code} - {self.instructor}"
    # TODO: add a method to get the time in a more readable format
    # TODO: add more fields to the course model

class department_courses(models.Model):
    department = models.ForeignKey(departments, on_delete=models.CASCADE)
    course = models.ForeignKey(courses, on_delete=models.CASCADE)
    
    class Meta:
        db_table_comment = "Department Courses Table"
        unique_together = ("department", "course")
    
    def __str__(self):
        return f"{self.department} requires {self.course}"
    
