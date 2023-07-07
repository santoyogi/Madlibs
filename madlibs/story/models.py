from django.db import models

# Create your models here.


class StoryInfo(models.Model):
    def __str__(self):
        return self.title

    title = models.CharField(max_length=200)
    description = models.CharField(max_length=250)
    story_img = models.CharField(max_length=500, default="https://cdn-icons-png.flaticon.com/512/4545/4545027.png")


class Pig(models.Model):
    place = models.CharField(max_length=50)
    object = models.CharField(max_length=50)
    vehicle = models.CharField(max_length=50)
    country = models.CharField(max_length=50)
    restaurant = models.CharField(max_length=50)
    porkItem = models.CharField(max_length=50)
    name = models.CharField(max_length=50)


class Rave(models.Model):
    name = models.CharField(max_length=50)
    action1 = models.CharField(max_length=50)
    adjective1 = models.CharField(max_length=50)
    action2 = models.CharField(max_length=50)
    object = models.CharField(max_length=50)
    negativeVerb = models.CharField(max_length=50)
    adjective2 = models.CharField(max_length=50)
    liquid = models.CharField(max_length=50)


class Eggs(models.Model):
    adjective = models.CharField(max_length=50)
    maleName = models.CharField(max_length=50)
    eggItem = models.CharField(max_length=50)
    color = models.CharField(max_length=50)
    hairstyle = models.CharField(max_length=50)
    place = models.CharField(max_length=50)
    food = models.CharField(max_length=50)
    yesOrNo = models.CharField(max_length=50)


class Sun(models.Model):
    vehicle = models.CharField(max_length=50)
    bodyPart = models.CharField(max_length=50)
    adjective1 = models.CharField(max_length=50)
    animal = models.CharField(max_length=50)
    verb = models.CharField(max_length=50)
    plant = models.CharField(max_length=50)
    emotion = models.CharField(max_length=50)
    adjective2 = models.CharField(max_length=50)


class Haunt(models.Model):
    noun = models.CharField(max_length=50)
    mythicalCreature = models.CharField(max_length=50)
    adjective1 = models.CharField(max_length=50)
    adjective2 = models.CharField(max_length=50)
    adjective3 = models.CharField(max_length=50)
    superlative = models.CharField(max_length=50)
    action = models.CharField(max_length=50)


class Beach(models.Model):
    adjective1 = models.CharField(max_length=50)
    food = models.CharField(max_length=50)
    object = models.CharField(max_length=50)
    verb = models.CharField(max_length=50)
    animal = models.CharField(max_length=50)
    plants = models.CharField(max_length=50)
    adjective2 = models.CharField(max_length=50)

class Work(models.Model):
    job = models.CharField(max_length=50)
    verb1 = models.CharField(max_length=50)
    adjective1 = models.CharField(max_length=50)
    noun = models.CharField(max_length=50)
    adjective2 = models.CharField(max_length=50)
    emotion = models.CharField(max_length=50)
    verb2 = models.CharField(max_length=50)


class Cat(models.Model):
    adjective1 = models.CharField(max_length=50)
    food1 = models.CharField(max_length=50)
    verb1 = models.CharField(max_length=50)
    verb2 = models.CharField(max_length=50)
    adjective2 = models.CharField(max_length=50)
    hobby = models.CharField(max_length=50)
    food2 = models.CharField(max_length=50)
    noun = models.CharField(max_length=50)
    emotion = models.CharField(max_length=50)


class Breakfast(models.Model):
    fruit = models.CharField(max_length=50)
    food = models.CharField(max_length=50)
    liquid = models.CharField(max_length=50)
    object = models.CharField(max_length=50)
    noun = models.CharField(max_length=50)
    animal = models.CharField(max_length=50)
    adjective1 = models.CharField(max_length=50)
    actionVerb = models.CharField(max_length=50)
    adjective2 = models.CharField(max_length=50)


class Nation(models.Model):
    adjective1 = models.CharField(max_length=50)
    actionVerb1 = models.CharField(max_length=50)
    adjective2 = models.CharField(max_length=50)
    actionVerb2 = models.CharField(max_length=50)
    noun1 = models.CharField(max_length=50)
    verb = models.CharField(max_length=50)
    noun2 = models.CharField(max_length=50)


class Emergency(models.Model):
    actionVerb = models.CharField(max_length=50)
    noun1 = models.CharField(max_length=50)
    jobTitle = models.CharField(max_length=50)
    verb = models.CharField(max_length=50)
    adjective1 = models.CharField(max_length=50)
    noun2 = models.CharField(max_length=50)
    adjective2 = models.CharField(max_length=50)
    adjective3 = models.CharField(max_length=50)


class Skin(models.Model):
    noun = models.CharField(max_length=50)
    bug = models.CharField(max_length=50)
    adjective1 = models.CharField(max_length=50)
    food = models.CharField(max_length=50)
    adjective2 = models.CharField(max_length=50)
    vegetable = models.CharField(max_length=50)
    adjective3 = models.CharField(max_length=50)


class Baby(models.Model):
    LastName = models.CharField(max_length=50)
    color1 = models.CharField(max_length=50)
    color2 = models.CharField(max_length=50)
    adjective1 = models.CharField(max_length=50)
    animal = models.CharField(max_length=50)
    color3 = models.CharField(max_length=50)
    adjective2 = models.CharField(max_length=50)
    verb = models.CharField(max_length=50)
    jobTitle = models.CharField(max_length=50)


class Extra(models.Model):
    person = models.CharField(max_length=50)
    animal = models.CharField(max_length=50)
    restaurant = models.CharField(max_length=50)
    adjective1 = models.CharField(max_length=50)
    adjective2 = models.CharField(max_length=50)
    noun = models.CharField(max_length=50)
    number = models.CharField(max_length=50)
    verb = models.CharField(max_length=50)


class Closing(models.Model):
    number = models.CharField(max_length=50)
    place = models.CharField(max_length=50)
    adjective1 = models.CharField(max_length=50)
    adjective2 = models.CharField(max_length=50)
    object1 = models.CharField(max_length=50)
    object2 = models.CharField(max_length=50)
    object3 = models.CharField(max_length=50)
    verb = models.CharField(max_length=50)