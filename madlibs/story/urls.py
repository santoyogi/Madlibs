from . import views
from django.urls import path

app_name = 'story'
urlpatterns = [
    path('', views.index, name="index"),
    path('<int:story_id>', views.info, name="info"),
    path('pig', views.pig, name="pig"),
    path('pig_story', views.pig_story, name="pig_story"),
    path('update/<int:id>', views.update_item, name="update_item"),
    path('generate/<int:id>', views.generate_pig, name="generate_pig"),
    path('rave', views.rave, name ="rave"),
    path('rave/<int:id>', views.rave_update, name="rave_update"),
    path('rave_story/<int:id>', views.generate_rave, name="generate_rave"),
    path('egg', views.egg, name="egg"),
    path('egg/<int:id>', views.egg_update, name="egg_update"),
    path('egg_story/<int:id>', views.generate_egg, name="generate_egg"),
    path('sun', views.sun, name="sun"),
    path('sun/<int:id>', views.sun_update, name="sun_update"),
    path('sun_story/<int:id>', views.generate_sun, name="generate_sun"),
    path('haunt', views.haunt, name="haunt"),
    path('haunt/<int:id>', views.haunt_update, name="haunt_update"),
    path('haunt_story/<int:id>', views.generate_haunt, name="generate_haunt"),
    path('beach', views.beach, name="beach"),
    path('beach/<int:id>', views.beach_update, name="beach_update"),
    path('beach_story/<int:id>', views.generate_beach, name="generate_beach"),
    path('work', views.work, name="work"),
    path('work/<int:id>', views.work_update, name="work_update"),
    path('work_story/<int:id>', views.generate_work, name="generate_work"),
    path('cat', views.cat, name="cat"),
    path('cat/<int:id>', views.cat_update, name="cat_update"),
    path('cat_story/<int:id>', views.generate_cat, name="generate_cat"),
    path('breakfast', views.breakfast, name="breakfast"),
    path('breakfast/<int:id>', views.breakfast_update, name="breakfast_update"),
    path('breakfast_story/<int:id>', views.generate_breakfast, name="generate_breakfast"),
    path('nation', views.nation, name="nation"),
    path('nation/<int:id>', views.nation_update, name="nation_update"),
    path('nation_story/<int:id>', views.generate_nation, name="generate_nation"),
    path('emergency', views.emergency, name="emergency"),
    path('emergency/<int:id>', views.emergency_update, name="emergency_update"),
    path('emergency_story/<int:id>', views.generate_emergency, name="generate_emergency"),
    path('skin', views.skin, name="skin"),
    path('skin/<int:id>', views.skin_update, name="skin_update"),
    path('skin_story/<int:id>', views.generate_skin, name="generate_skin"),
    path('baby', views.baby, name="baby"),
    path('baby/<int:id>', views.baby_update, name="baby_update"),
    path('baby_story/<int:id>', views.generate_baby, name="generate_baby"),
    path('extra', views.extra, name="extra"),
    path('extra/<int:id>', views.extra_update, name="extra_update"),
    path('extra_story/<int:id>', views.generate_extra, name="generate_extra"),
    path('closing', views.closing, name="closing"),
    path('closing/<int:id>', views.closing_update, name="closing_update"),
    path('closing_story/<int:id>', views.generate_closing, name="generate_closing"),
]