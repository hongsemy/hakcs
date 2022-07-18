from django.db import models

# Create your models here.
class CommonInfo(models.Model):
    title = models.CharField(max_length=20)
    description = models.CharField(max_length=500)
    class Meta:
        abstract = True


class Mission(CommonInfo):
    icon = models.CharField(max_length=30)


class PastEvents(CommonInfo):
    time = models.CharField(max_length=60)


class Executive(models.Model):
    name = models.CharField(max_length=20)
    role = models.CharField(max_length=100)
    programs_of_study = models.CharField(max_length=300)
    instagram_id = models.CharField(max_length=50)
    linked_in_address = models.CharField(max_length=200)
    github_address = models.CharField(max_length=200)
    image = models.CharField(max_length=500)


class SectionTitle(CommonInfo):
    section_name = models.CharField(max_length=20)
    title = models.CharField(max_length=50)
