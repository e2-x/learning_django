from django.shortcuts import render
#from second_app.models import Topic, Webpage, AccessRecord, User
from second_app.forms import NewUserForm

# Create your views here.
def index(request):
    my_dict = {'insert_index':"Go to /users to see the list of user information"}
    return render(request, 'second_app/index.html', context=my_dict)

def users(request):
    form = NewUserForm
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return index(request)
        else:
            print('ERROR FORM INVALID')
    return render(request, 'second_app/users.html', {'form':form})    

def help(request):
    my_dict = {'insert_help':"Help information"}
    return render(request, 'second_app/help.html', context=my_dict)
