from django.shortcuts import render, redirect
from .models import Post
from django.utils import timezone
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.forms import UserCreationForm

# Create your views here.

def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})
	
def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})

			 
def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            my_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=my_password)
            login(request, user)
            return redirect('/')
    else:
        form = UserCreationForm()
    return render(request, 'blog/signup.html', {'form': form})
	
def registr(request):
    if request.method == 'POST':
        form = UserForm(request.POST)     # create form object
        if form.is_valid():
            email = form.cleaned_data['email']
            user = User(email=email)
            user.save()
            return HttpResponseRedirect('/blog/registr.html')
			
def faq(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/faq.html', {'posts': posts})