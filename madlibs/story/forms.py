from django import forms
from .models import *


class PigForm(forms.ModelForm):
    class Meta:
        model = Pig
        fields = ['place', 'object', 'vehicle', 'country',
                  'restaurant', 'porkItem', 'name']


class RaveForm(forms.ModelForm):
    class Meta:
        model = Rave
        fields = ['name', 'action1', 'adjective1', 'action2',
                  'object', 'negativeVerb', 'adjective2', 'liquid']


class EggForm(forms.ModelForm):
    class Meta:
        model = Eggs
        fields = ['adjective', 'maleName', 'eggItem', 'color',
                  'hairstyle', 'place', 'food', 'yesOrNo']


class SunForm(forms.ModelForm):
    class Meta:
        model = Sun
        fields = ['vehicle', 'bodyPart', 'adjective1', 'animal',
                  'verb', 'plant', 'emotion', 'adjective2']


class HauntForm(forms.ModelForm):
    class Meta:
        model = Haunt
        fields = ['noun', 'mythicalCreature', 'adjective1', 'adjective2',
                  'adjective3', 'superlative', 'action']


class BeachForm(forms.ModelForm):
    class Meta:
        model = Beach
        fields = ['adjective1', 'food', 'object', 'verb',
                  'animal', 'plants', 'adjective2']


class WorkForm(forms.ModelForm):
    class Meta:
        model = Work
        fields = ['job', 'verb1', 'adjective1', 'noun',
                  'adjective2', 'emotion', 'verb2']


class CatForm(forms.ModelForm):
    class Meta:
        model = Cat
        fields = ['adjective1', 'food1', 'verb1', 'verb2',
                  'adjective2', 'hobby', 'food2', 'noun', 'emotion']


class BreakfastForm(forms.ModelForm):
    class Meta:
        model = Breakfast
        fields = ['fruit', 'food', 'liquid', 'object',
                  'noun', 'animal', 'adjective1', 'actionVerb', 'adjective2']


class NationForm(forms.ModelForm):
    class Meta:
        model = Nation
        fields = ['adjective1', 'actionVerb1', 'adjective2', 'actionVerb2',
                  'noun1', 'verb', 'noun2']


class EmergencyForm(forms.ModelForm):
    class Meta:
        model = Emergency
        fields = ['actionVerb', 'noun1', 'jobTitle', 'verb',
                  'adjective1', 'noun2', 'adjective2', 'adjective3']


class SkinForm(forms.ModelForm):
    class Meta:
        model = Skin
        fields = ['noun', 'bug', 'adjective1', 'food',
                  'adjective2', 'food', 'adjective2', 'vegetable', 'adjective3']


class BabyForm(forms.ModelForm):
    class Meta:
        model = Baby
        fields = ['LastName', 'color1', 'color2', 'adjective1',
                  'animal', 'color3', 'adjective2', 'verb', 'jobTitle']


class ExtraForm(forms.ModelForm):
    class Meta:
        model = Extra
        fields = ['person', 'animal', 'restaurant', 'adjective1',
                  'adjective2', 'noun', 'number', 'verb', ]


class ClosingForm(forms.ModelForm):
    class Meta:
        model = Closing
        fields = ['number', 'place', 'adjective1', 'adjective2',
                  'object1', 'object2', 'object3', 'verb', ]

