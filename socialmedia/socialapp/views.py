from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Profile,Post,Like_post
# Create your views here.
def home(request):
    return render(request,'socialapp/home.html')

def signup(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        if username!='' and password!='':
            
                user_object=User.objects.create_user(username=username,password=password)
                user_profile=Profile.objects.create(user=user_object,id_user=user_object.id)
                user_profile.save()
                #messages.info(request,'This user name has already taken')
                return redirect('/')

        else:
            messages.info(request,'fill up')
            return redirect('signup')
   
    return render(request,'socialapp/signup.html')

@login_required
def show(request):
    return render(request,'socialapp/home.html')   

@login_required
def logout(request):
    return render(request,'socialapp/new_out.html')

@login_required
def profile(request):
    user_profile=Profile.objects.get(user=request.user)
    if request.method=='POST':
        if request.FILES.get('image')==None:
            image=user_profile.profileimg
            bio=request.POST['bio']
            location=request.POST['location']
            user_profile.profileimg=image
            user_profile.bio=bio
            user_profile.location=location
            user_profile.save()
        if request.FILES.get('image')!=None:
            image=request.FILES.get('image')
            bio=request.POST['bio']
            location=request.POST['location']
            user_profile.profileimg=image
            user_profile.bio=bio
            user_profile.location=location
            user_profile.save()
        return redirect('/')   
    
    return render(request,'socialapp/profile.html',{'user_profile':user_profile})    
@login_required
def post(request):
    if request.method=="POST":
        if request.FILES.get("post_img")==None:
            messages.info(request,'please give a picture')
        if request.FILES.get("post_img")!=None:
            img=request.FILES.get("post_img")
            name=request.POST['name']    
            caption=request.POST['caption']
            post=Post.objects.create(user=name,img=img,caption=caption)
            post.save()
            return redirect('/')

    
    return render(request,'socialapp/post.html')

@login_required
def allpic(request):
    pics=Post.objects.all()        
    return render(request,'socialapp/allpic.html',{'pics':pics})
@login_required
def like(request):
    id=request.GET.get('post_id')
    username=request.user.username
    post=Post.objects.get(id=id)
    like_filter=Like_post.objects.filter(user=username,post_id=id).first()
    if like_filter:
        like_filter.delete()
        post.no_of_likes-=1
        post.save()
    else:
        like=Like_post.objects.create(user=username,post_id=id)    
        like.save()
        post.no_of_likes+=1
        post.save()
    return redirect('/allpic')
