from django.shortcuts import *
from django.contrib.auth import *
from django.contrib.auth.models import *
from django.urls import reverse_lazy
from django.views.generic import *
from pinterestapp.forms_app.form import SignUp, Login_form, Pin_form
from pinterestapp.models import *


class SignUp_controller(View):
    def get(self,request):
        myform=SignUp()
        return render(
            request,
            template_name='signup_page.html',
            context={
                'signup_details':myform
            }
        )
    def post(self,request):
        myform = SignUp(request.POST)
        if myform.is_valid():
            user=User.objects.create_user(**myform.cleaned_data)
            user=authenticate(
                request,
                username=myform.cleaned_data['username'],
                password=myform.cleaned_data['password']
            )

            if user is not None:
                login(request,user)
                return redirect("/thankyou")

class Login_controller(View):
    def get(self,request):
        if request.user.is_authenticated:
            #return redirect("/thankyou/")
            render(request, 'home.html', {'name': request.user.username})
        myform=Login_form()
        return render(
            request,
            template_name="login_page.html",
            context={
                'login_details':myform
            }
        )
    def post(self,request):
        myform=Login_form(request.POST)
        if myform.is_valid():
            username=myform.cleaned_data['username']
            #email=myform.cleaned_data['email']
            password=myform.cleaned_data['password']
            user=authenticate(request,username=username,password=password)

            if user is not None:
                login(request,user)
                return redirect("home")
            else:
                return redirect("signup")



class Logout_controller(View):
    def get(self,request):
        logout(request)
        return redirect("login")

"""class thankyou(View):
    def get(self,request):
        return render(request,template_name="thankyou.html",context=None)"""

class thankyou(View):
    def get(self,request):
        user = User.objects.get(username=request.user.username)
        pins = Pin.objects.filter(createdby_id=user.id)
        return render(request,template_name="thankyou.html",context={'pins':pins,'user': user})

def get_user_profile(request,username):
    user = User.objects.get(username=username)
    return render(request, 'user_profile.html', {"user": user})

class home(View):
    def get(self,request):
        return render(request,template_name="home.html",context=None)

def following(request):
    return render(request,"following.html")

def topics(request,username):
    user=User.objects.get(username=username)
    return render(request, 'topics.html', {"user": user})



class CreatePin(CreateView):
    model = Pin
    form_class = Pin_form
    template_name = "createpin_form.html"

    def post(self, request, *args, **kwargs):
        post = Pin_form(request.POST,request.FILES)
        if post.is_valid():
            post = post.save(commit=False)
            post.createdby = request.user
            post.save()
            return redirect('/home/')
        else:
            return redirect("createpin")

class ViewPin(DetailView):
    model=Pin
    template_name = "pinview.html"

    """def get_object(self, queryset=None):
        return get_object_or_404(Pin, **self.kwargs)"""

    def get(self, request, *args, **kwargs):
        pin=Pin.objects.get(id=self.kwargs['id'])
        profile=UserProfile.objects.filter(user=request.user)
        return render(request,"pinview.html", context={'pin':pin,'profile':profile})



def ViewAllPins(request,username):
    user=User.objects.get(username=username)
    pins = Pin.objects.filter(createdby_id=user.id)

    return render(request,'viewallpins.html', context={'pins':pins,'user': user})





def selecttopics(request):
    return render(request,"selecttopics.html",None)

class savepin(View):
    pass


"""def CreatePin(request):
    if request.method == 'POST':
        form=Pin_form(request.POST,request.FILES)
        if form.is_valid():
            instance = Pin_form(files=request.FILES['photo'])
            instance.save()
            return HttpResponseRedirect('/home/')
    else:
        form=Pin_form()
    return render(request,'createpin_form.html',{'form':form})"""