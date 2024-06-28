from django.shortcuts import render

# Create your views here.

def show_member_info(request):
    return render(request, "member_page.html" , {
        'member_name': 'jun',
        'member_age': '21吧'
    })