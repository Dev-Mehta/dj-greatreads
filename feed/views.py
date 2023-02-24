from django.views.generic import ListView

from .models import Post


class HomePage(ListView):
    template_name = "feed/home.html"
    model = Post
    paginate_by = 5
    context_object_name = "posts"
    ordering = ["-pub_at"]
