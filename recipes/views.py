from django.http import HttpResponse
from django.template import Context, loader, RequestContext
from django.shortcuts import get_object_or_404, render_to_response,\
redirect

from recipes.models import Recipe
from recipes.forms import RecipeForm

def fix_url(recipes):
	for recipe in recipes:
		recipe.url = recipe.name.replace(' ', '_')
	return recipes

def index(request):
	latest_posts = Recipe.objects.all().order_by('-created_at')
	popular_posts = Recipe.objects.order_by('-views')[:5]
	t = loader.get_template('recipes/index.html')
	context_dict = {
		'latest_posts': latest_posts,
		'popular_posts': popular_posts,
	 }

	fix_url(latest_posts)
	fix_url(popular_posts)
	c = Context(context_dict)
	return HttpResponse(t.render(c))

def post(request, post_url):
	single_post = get_object_or_404(Recipe, name=post_url.replace('_', ' '))
	single_post.views += 1
	single_post.save()
	popular_posts = Recipe.objects.order_by('-views')[:5]
	fix_url(popular_posts)
	t = loader.get_template('recipes/post.html')
	context_dict = {
		'single_post' : single_post,
		'popular_posts': popular_posts
		}
	c = Context(context_dict)
	return HttpResponse(t.render(c))

def add_post(request):
	context = RequestContext(request)
	if request.method == 'POST':
		form = RecipeForm(request.POST, request.FILES)
		if form.is_valid():
			check = form.save(commit=True)
			return redirect('recipes.views.post', post_url=check.name.replace(' ', '_'))
		else:
			print form.errors
	else:
		form = RecipeForm()
	return render_to_response('recipes/add_post.html', {'form': form}, context)