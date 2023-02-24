from django.contrib import admin

from .models import Post
from .models import Submission

# Register your models here.
admin.site.register(Submission)
admin.site.register(Post)
