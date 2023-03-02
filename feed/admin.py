from django.contrib import admin
from django.contrib.admin.filters import SimpleListFilter

from .models import Post
from .models import Submission


class SourceFilter(SimpleListFilter):
    title = "source"
    parameter_name = "source"

    def lookups(self, request, model_admin):
        return (
            ("hackernoon", "hackernoon"),
            ("testdriven", "testdriven"),
            ("simplifiedweb", "simplifiedweb"),
        )

    def queryset(self, request, queryset):
        val = self.value()
        if val:
            hn = queryset.filter(link__startswith=f"https://{val}")
            return hn
        else:
            return queryset


class TagFilter(SimpleListFilter):
    title = "tag"
    parameter_name = "tag"

    def lookups(self, request, model_admin):
        return (
            ("django", "django"),
            ("python", "python"),
            ("chatgpt", "chatgpt"),
            ("how to", "how to..."),
        )

    def queryset(self, request, queryset):
        val = self.value()
        if val:
            return queryset.filter(title__icontains=val)
        else:
            return queryset


class PostAdmin(admin.ModelAdmin):
    list_filter = (SourceFilter, TagFilter)


# Register your models here.
admin.site.register(Submission)
admin.site.register(Post, PostAdmin)
