from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from .forms import *
from django.template import loader

# Create your views here.


def info(request, story_id):
    story = StoryInfo.objects.get(pk=story_id)
    context = {
        'story': story
    }
    return render(request, 'story/detail.html', context)


def index(request):
    story_list = StoryInfo.objects.all()
    context ={
        'story_list': story_list,
    }
    return render(request, 'story/index.html', context)


# ---------- CREATE VIEWS -----------
def pig(request):
    context = {}
    return render(request, 'story/pig-story.html', context)


def rave(request):
    context = {}
    return render(request, 'story/rave-story.html', context)


def egg(request):
    context = {}
    return render(request, 'story/egg-story.html', context)


def sun(request):
    context = {}
    return render(request, 'story/sun-story.html', context)


def haunt(request):
    context = {}
    return render(request, 'story/haunt-story.html', context)


def beach(request):
    context = {}
    return render(request, 'story/beach-story.html', context)


def work(request):
    context = {}
    return render(request, 'story/work-story.html', context)


def cat(request):
    context = {}
    return render(request, 'story/cat-story.html', context)


def breakfast(request):
    context = {}
    return render(request, 'story/breakfast-story.html', context)


def nation(request):
    context = {}
    return render(request, 'story/nation-story.html', context)


def emergency(request):
    context = {}
    return render(request, 'story/emergency-story.html', context)


def skin(request):
    context = {}
    return render(request, 'story/skin-story.html', context)


def baby(request):
    context = {}
    return render(request, 'story/baby-story.html', context)


def extra(request):
    context = {}
    return render(request, 'story/extra-story.html', context)


def closing(request):
    context = {}
    return render(request, 'story/closing-story.html', context)


# ----------- CREATE NEW INSTANCE -------
def raveTo(request):
    form = RaveForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('/story/index')

    return render(request, 'story/rave-form.html', {'form': form})


def pig_story(request):
    form = PigForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('/story/pig')

    return render(request, 'story/pig-form.html', {'form':form})


def eggTo(request):
    form = EggForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('/story/index')

    return render(request, 'story/pig-form.html', {'form': form})


def sunTo(request):
    form = SunForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('/story/index')

    return render(request, 'story/sun-form.html', {'form': form})


def hauntTo(request):
    form = HauntForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('/story/index')

    return render(request, 'story/haunt-form.html', {'form': form})


def beachTo(request):
    form = BeachForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('/story/index')

    return render(request, 'story/beach-form.html', {'form': form})


def workTo(request):
    form = WorkForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('/story/index')

    return render(request, 'story/work-form.html', {'form': form})


def catTo(request):
    form = CatForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('/story/index')

    return render(request, 'story/cat-form.html', {'form': form})


def breakfastTo(request):
    form = BreakfastForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('/story/index')

    return render(request, 'story/breakfast-form.html', {'form': form})


def nationTo(request):
    form = NationForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('/story/index')

    return render(request, 'story/nation-form.html', {'form': form})


def emergencyTo(request):
    form = EmergencyForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('/story/index')

    return render(request, 'story/emergency-form.html', {'form': form})


def skinTo(request):
    form = SkinForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('/story/index')

    return render(request, 'story/skin-form.html', {'form': form})


def babyTo(request):
    form = BabyForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('/story/index')

    return render(request, 'story/baby-form.html', {'form': form})


def extraTo(request):
    form = ExtraForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('/story/index')

    return render(request, 'story/extra-form.html', {'form': form})


def closingTo(request):
    form = ClosingForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('/story/index')

    return render(request, 'story/closing-form.html', {'form': form})


# ---------- EDIT FORMS ----------
def update_item(request, id):
    item = Pig.objects.get(id=id)
    form = PigForm(request.POST or None, instance=item)

    if form.is_valid():
        form.save()
        return redirect('/story/update/3')

    return render(request, 'story/pig-form.html', {'form': form, 'item': item})


def rave_update(request, id):
    item = Rave.objects.get(id=id)
    form = RaveForm(request.POST or None, instance=item)

    if form.is_valid():
        form.save()
        return redirect('/story/rave/1')

    return render(request, 'story/rave-form.html', {'form': form, 'item':item})


def egg_update(request, id):
    item = Eggs.objects.get(id=id)
    form = EggForm(request.POST or None, instance=item)

    if form.is_valid():
        form.save()
        return redirect('/story/egg/1')

    return render(request, 'story/egg-form.html', {'form':form, 'item':item})


def sun_update(request, id):
    item = Sun.objects.get(id=id)
    form = SunForm(request.POST or None, instance=item)

    if form.is_valid():
        form.save()
        return redirect('/story/sun/1')

    return render(request, 'story/sun-form.html', {'form':form, 'item':item})


def haunt_update(request, id):
    item = Haunt.objects.get(id=id)
    form = HauntForm(request.POST or None, instance=item)

    if form.is_valid():
        form.save()
        return redirect('/story/haunt/1')

    return render(request, 'story/haunt-form.html', {'form':form, 'item':item})


def beach_update(request, id):
    item = Beach.objects.get(id=id)
    form = BeachForm(request.POST or None, instance=item)

    if form.is_valid():
        form.save()
        return redirect('/story/beach/1')

    return render(request, 'story/beach-form.html', {'form':form, 'item':item})


def work_update(request, id):
    item = Work.objects.get(id=id)
    form = WorkForm(request.POST or None, instance=item)

    if form.is_valid():
        form.save()
        return redirect('/story/work/1')

    return render(request, 'story/work-form.html', {'form':form, 'item':item})


def cat_update(request, id):
    item = Cat.objects.get(id=id)
    form = CatForm(request.POST or None, instance=item)

    if form.is_valid():
        form.save()
        return redirect('/story/cat/1')

    return render(request, 'story/cat-form.html', {'form':form, 'item':item})


def breakfast_update(request, id):
    item = Breakfast.objects.get(id=id)
    form = BreakfastForm(request.POST or None, instance=item)

    if form.is_valid():
        form.save()
        return redirect('/story/breakfast/1')

    return render(request, 'story/breakfast-form.html', {'form':form, 'item':item})


def nation_update(request, id):
    item = Nation.objects.get(id=id)
    form = NationForm(request.POST or None, instance=item)

    if form.is_valid():
        form.save()
        return redirect('/story/nation/1')

    return render(request, 'story/nation-form.html', {'form':form, 'item':item})


def emergency_update(request, id):
    item = Emergency.objects.get(id=id)
    form = EmergencyForm(request.POST or None, instance=item)

    if form.is_valid():
        form.save()
        return redirect('/story/emergency/1')

    return render(request, 'story/emergency-form.html', {'form':form, 'item':item})


def skin_update(request, id):
    item = Skin.objects.get(id=id)
    form = SkinForm(request.POST or None, instance=item)

    if form.is_valid():
        form.save()
        return redirect('/story/skin/1')

    return render(request, 'story/skin-form.html', {'form':form, 'item':item})


def baby_update(request, id):
    item = Baby.objects.get(id=id)
    form = BabyForm(request.POST or None, instance=item)

    if form.is_valid():
        form.save()
        return redirect('/story/baby/1')

    return render(request, 'story/baby-form.html', {'form':form, 'item':item})


def extra_update(request, id):
    item = Extra.objects.get(id=id)
    form = ExtraForm(request.POST or None, instance=item)

    if form.is_valid():
        form.save()
        return redirect('/story/extra/1')

    return render(request, 'story/extra-form.html', {'form':form, 'item':item})


def closing_update(request, id):
    item = Closing.objects.get(id=id)
    form = ClosingForm(request.POST or None, instance=item)

    if form.is_valid():
        form.save()
        return redirect('/story/closing/1')

    return render(request, 'story/closing-form.html', {'form':form, 'item':item})


# --------- GENERATE MADLIB --------------
def generate_pig(request, id):
    item = Pig.objects.get(id=id)

    if request.method == 'POST':
        return redirect('/story/pig')

    return render(request, 'story/pig-story.html', {'item':item})


def generate_rave(request, id):
    item = Rave.objects.get(id=id)

    if request.method == 'POST':
        return redirect('/story/rave')

    return render(request, 'story/rave-story.html', {'item':item})


def generate_egg(request, id):
    item = Eggs.objects.get(id=id)

    if request.method == 'POST':
        return redirect('/story/egg')

    return render(request, 'story/egg-story.html', {'item': item})


def generate_sun(request, id):
    item = Sun.objects.get(id=id)

    if request.method == 'POST':
        return redirect('/story/sun')

    return render(request, 'story/sun-story.html', {'item': item})


def generate_haunt(request, id):
    item = Haunt.objects.get(id=id)

    if request.method == 'POST':
        return redirect('/story/haunt')

    return render(request, 'story/haunt-story.html', {'item': item})


def generate_beach(request, id):
    item = Beach.objects.get(id=id)

    if request.method == 'POST':
        return redirect('/story/beach')

    return render(request, 'story/beach-story.html', {'item': item})


def generate_work(request, id):
    item = Work.objects.get(id=id)

    if request.method == 'POST':
        return redirect('/story/work')

    return render(request, 'story/work-story.html', {'item': item})


def generate_cat(request, id):
    item = Cat.objects.get(id=id)

    if request.method == 'POST':
        return redirect('/story/cat')

    return render(request, 'story/cat-story.html', {'item': item})


def generate_breakfast(request, id):
    item = Breakfast.objects.get(id=id)

    if request.method == 'POST':
        return redirect('/story/breakfast')

    return render(request, 'story/breakfast-story.html', {'item': item})


def generate_nation(request, id):
    item = Nation.objects.get(id=id)

    if request.method == 'POST':
        return redirect('/story/nation')

    return render(request, 'story/nation-story.html', {'item': item})


def generate_emergency(request, id):
    item = Emergency.objects.get(id=id)

    if request.method == 'POST':
        return redirect('/story/emergency')

    return render(request, 'story/emergency-story.html', {'item': item})


def generate_skin(request, id):
    item = Skin.objects.get(id=id)

    if request.method == 'POST':
        return redirect('/story/skin')

    return render(request, 'story/skin-story.html', {'item': item})


def generate_baby(request, id):
    item = Baby.objects.get(id=id)

    if request.method == 'POST':
        return redirect('/story/baby')

    return render(request, 'story/baby-story.html', {'item': item})


def generate_extra(request, id):
    item = Extra.objects.get(id=id)

    if request.method == 'POST':
        return redirect('/story/extra')

    return render(request, 'story/extra-story.html', {'item': item})


def generate_closing(request, id):
    item = Closing.objects.get(id=id)

    if request.method == 'POST':
        return redirect('/story/closing')

    return render(request, 'story/closing-story.html', {'item': item})
