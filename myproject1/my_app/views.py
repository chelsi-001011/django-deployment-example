from django.shortcuts import render
# from my_app.models import User
from my_app.forms import NewUserForm

# Create your views here.
def index(request):
    return render(request,'my_app/index.html')

def users(request):

    form = NewUserForm() #someone used form...

    if request.method == 'POST': #to get back information...
        form = NewUserForm(request.POST)

    if form.is_valid(): #and it was valid...
        form.save(commit=True)
        return index(request) #then it will return the index request page
    else:
        print("ERROR FORM INVALID")

    return render(request,'my_app/users.html',{'form':form})