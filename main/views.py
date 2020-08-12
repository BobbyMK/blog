from django.shortcuts import render
from .forms import PostForm
from .models import Post

def main(request):
	last = Post.objects.order_by("-id")[0:1]
	latest = Post.objects.order_by("-id")[1:10]
	return render(request, 'main.html', locals())

def post(request):
	return render(request, 'new_post.html', locals())

def publish(request):

	if request.method == "POST":
		form = PostForm(request.POST, request.FILES)
		if form.is_valid():
			post = form.save(commit=False)
			post.image = request.FILES['image']
			post.save()
			print (request.FILES)
			print (request.POST)
	else:
		form = PostForm()


	return render(request, 'main.html', {
		"form": form
    })

def read(request):

	value = request.GET.get('value')
	value = int(value)
	article = Post.objects.filter(id=value)

	return render(request, 'read_post.html', locals())