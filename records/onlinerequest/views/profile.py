import json
from django.http import HttpResponse
from django.http import JsonResponse
from django.core.exceptions import ValidationError
from django.shortcuts import render
from ..models import Profile, User
from ..serializers import RecordSerializer
from ..forms import ProfileForm

def index(request):
    # Get authneticated user
    user = request.user
    user_profile = get_if_exists(Profile, user = user)

    if request.method == "GET":
        if user_profile:
            return render(request, 'user/profile.html', { 'profile': user_profile })
        
        return HttpResponse("Profile not yet created. Please consult your administrator")
    
    elif request.method == "POST":
        #  Data
        data = json.loads(request.body)
        contact_no = data.get('contact_no')

        data = {
            'user': user_profile.user,
            'course': user_profile.course,
            'first_name': user_profile.first_name,
            'last_name': user_profile.last_name,
            'middle_name': user_profile.middle_name,
            'contact_no': contact_no,
            'entry_year_from': user_profile.entry_year_from,
            'entry_year_to': user_profile.entry_year_to
        }

        if user_profile:
            profile_form = ProfileForm(data, instance = user_profile)
            
            if profile_form.is_valid():
                profile_form.save()
                return JsonResponse({'message': "Profile saved."})
            else:
                return JsonResponse({'errors': profile_form.errors}, status = 400)
        
    return JsonResponse({'error': 'Only POST and GET requests are allowed'}, status=405)

def get_if_exists(model, **kwargs):
    try:
        obj = model.objects.get(**kwargs)
    except model.DoesNotExist:
        obj = None
    return obj