from django.http import HttpResponse
from django.template import Context, loader, RequestContext
from django.shortcuts import get_object_or_404, render_to_response,\
redirect

from blog.models import Post
from blog.forms import PostForm

def fix_url(posts):
	for post in posts:
		post.url = post.name.replace(' ', '_')
	return posts

def index(request):
	latest_posts = Post.objects.all().order_by('-created_at')
	popular_posts = Post.objects.order_by('-views')[:5]
	t = loader.get_template('blog/index.html')
	context_dict = {
		'latest_posts': latest_posts,
		'popular_posts': popular_posts,
	 }

	fix_url(latest_posts)
	fix_url(popular_posts)
	c = Context(context_dict)
	return HttpResponse(t.render(c))

def post(request, post_url):
	single_post = get_object_or_404(Post, name=post_url.replace('_', ' '))
	single_post.views += 1
	single_post.save()
	popular_posts = Post.objects.order_by('-views')[:5]
	fix_url(popular_posts)
	t = loader.get_template('blog/post.html')
	context_dict = {
		'single_post' : single_post,
		'popular_posts': popular_posts
		}
	c = Context(context_dict)
	return HttpResponse(t.render(c))

def add_post(request):
	context = RequestContext(request)
	if request.method == 'POST':
		form = PostForm(request.POST, request.FILES)
		if form.is_valid():
			check = form.save(commit=True)
			return redirect('blog.views.post', post_url=check.name.replace(' ', '_'))
		else:
			print form.errors
	else:
		form = PostForm()
	return render_to_response('blog/add_post.html', {'form': form}, context)