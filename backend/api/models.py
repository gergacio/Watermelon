from django.db import models
from django.utils.text import slugify
from userauths.models import User, Profile
from django.utils import timezone
from shortuuid.django_fields import ShortUUIDField

LANGUAGE = (
    ("English", "English"),
    ("Spanish", "Spanish"),
    ("French", "French"),
)

LEVEL = (
    ("Beginner", "Beginner"),
    ("Intemediate", "Intemediate"),
    ("Advanced", "Advanced"),
)

TEACHER_STATUS = (
    ("Draft", "Draft"),
    ("Disabled", "Disabled"),
    ("Published", "Published"),
)

PLATFORM_STATUS = (
    ("Review", "Review"),
    ("Disabled", "Disabled"),
    ("Rejected", "Rejected"),
    ("Draft", "Draft"),
    ("Published", "Published"),
)

RATING = (
    (1, "1 Star"),
    (2, "2 Star"),
    (3, "3 Star"),
    (4, "4 Star"),
    (5, "5 Star"),
)

NOTI_TYPE = (
    ("New Order", "New Order"),
    ("New Review", "New Review"),
    ("New Course Question", "New Course Question"),
    ("Draft", "Draft"),
    ("Course Published", "Course Published"),
    ("Course Enrollment Completed", "Course Enrollment Completed"),
)

# Create your models here.
class Teacher(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.FileField(upload_to="course-file", blank=True, null=True, default="default.jpg")
    full_name = models.CharField(max_length=100)
    bio = models.CharField(max_length=100, null=True, blank=True)
    facebook = models.URLField(null=True, blank=True)
    twitter = models.URLField(null=True, blank=True)
    linkedin = models.URLField(null=True, blank=True)
    about = models.TextField(null=True, blank=True)
    country = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.full_name
    
    def students(self):
        return CartOrderItem.objects.filter(teacher=self)
    
    def courses(self):
        return Course.objects.filter(teacher=self)
    
    def review(self):
        return Course.objects.filter(teacher=self).count()
    
class Category(models.Model):
    title = models.CharField(max_length=100)
    image = models.FileField(upload_to="course-file", default="category.jpg", null=True, blank=True)
    active = models.BooleanField(default=True)
    slug = models.SlugField(unique=True, null=True, blank=True)

    class Meta:
        verbose_name_plural = "Category"
        ordering = ['title']

    def __str__(self):
        return self.title
    
    def course_count(self):
        return Course.objects.filter(category=self).count()
    
    def save(self, *args, **kwargs):
        if self.slug == "" or self.slug == None:
            self.slug = slugify(self.title) 
        super(Category, self).save(*args, **kwargs)    

class Course(models.Model):
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)
    teacher = models.ForeignKey(Teacher, on_delete=models.SET_NULL, blank=True, null=True)
    file = models.CharField(max_length=200, blank=True, null=True)
    image = models.CharField(max_length=200, blank=True, null=True)
    title = models.CharField(max_length=200, blank=True, null=True)
    description = models.TextField(null=True, blank=True)
    price = models.DecimalField(max_digits=12, decimal_places=2, default=0.00, blank=True, null=True)
    language = models.CharField(choices=LANGUAGE, default="English", max_length=100, blank=True, null=True)
    level = models.CharField(choices=LEVEL, default="Beginner", max_length=100, blank=True, null=True)
    platform_status = models.CharField(choices=PLATFORM_STATUS, default="Published", max_length=100, blank=True, null=True)
    teacher_course_status = models.CharField(choices=TEACHER_STATUS, default="Published", max_length=100)
    featured = models.BooleanField(default=False)
    course_id = ShortUUIDField(unique=True, length=6, max_length=20, alphabet="1234567890")
    slug = models.SlugField(unique=True, null=True, blank=True)
    date = models.DateTimeField(default=timezone.now)


    def __str__(self):
        return self.title
    
    def save(self, *args, **kwargs):
        if self.slug == "" or self.slug == None:
            self.slug = slugify(self.title) + str(self.pk)
        super(Course, self).save(*args, **kwargs)


