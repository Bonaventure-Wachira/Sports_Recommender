from django.shortcuts import render
from .sports_recommender import attributes, recommend_sport

attribute_descriptions = [
    ("Endurance", "Ability to sustain physical activity over time"),
    ("Strength", "Muscular force exerted to overcome resistance"),
    ("Power", "Combination of strength and speed"),
    ("Speed", "Movement velocity"),
    ("Agility", "Ability to change body position quickly and efficiently"),
    ("Flexibility", "Range of motion around a joint"),
    ("Nerve", "Mental toughness and ability to perform under pressure"),
    ("Durability", "Resistance to injuries and fatigue"),
    ("Hand-Eye Coordination", "Synchronization of vision and hand movement"),
    ("Analytical Aptitude", "Ability to analyze and react to complex situations"),
]

def input_form(request):
    return render(request, "input_form.html", {"attribute_descriptions": attribute_descriptions})

def recommended_sport(request):
    if request.method == "POST":
        inputs = {attr: float(request.POST[attr]) for attr in attributes}
        recommended_sport = recommend_sport(inputs)
        return render(request, "recommended_sport.html", {"recommended_sport": recommended_sport})

