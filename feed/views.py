from django.shortcuts import render
from django.views.generic import TemplateView

from .forms import SubmissionForm

# import feedparser


class HomePage(TemplateView):
    template_name = "feed/home.html"

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        # ctx['feed'] = feedparser.parse("https://simplifiedweb.netlify.app/rss.xml/")
        # print(ctx['feed']['entries'][0].keys())
        return ctx

    def post(self, request, *args, **kwargs):
        form = SubmissionForm(self.request.POST)
        if form.is_valid():
            form.save()
            return render(
                request,
                "feed/home.html",
                {"form": form, "message": "Saved Successfully!"},
            )
        else:
            return render(
                request,
                "feed/home.html",
                {"form": form, "errors": form.errors},
            )
