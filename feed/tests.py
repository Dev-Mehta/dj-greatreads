import datetime

from django.test import TestCase

from .models import Post
from .models import Submission

# Create your tests here.


class SubmissionTestCase(TestCase):
    def setUp(self):
        Submission.objects.create(link="https://simplifiedweb.netlify.app/rss.xml/")

    def test_link(self):
        s = Submission.objects.get(link="https://simplifiedweb.netlify.app/rss.xml/")
        self.assertEqual(s.link, "https://simplifiedweb.netlify.app/rss.xml/")


class PostTestCase(TestCase):
    def setUp(self):
        Post.objects.create(
            title="Hello World",
            author="Dev Mehta",
            summary="Hello World Post",
            link="https://simplifiedweb.netlify.app/hello-world/",
            pub_at=datetime.datetime.now().date(),
        )

    def test_title(self):
        p = Post.objects.get(title="Hello World")
        self.assertEqual(p.title, "Hello World")

    def test_author(self):
        p = Post.objects.get(title="Hello World")
        self.assertEqual(p.author, "Dev Mehta")

    def test_summary(self):
        p = Post.objects.get(title="Hello World")
        self.assertEqual(p.summary, "Hello World Post")

    def test_link(self):
        p = Post.objects.get(title="Hello World")
        self.assertEqual(p.link, "https://simplifiedweb.netlify.app/hello-world/")

    def test_pub_at(self):
        p = Post.objects.get(title="Hello World")
        self.assertEqual(p.pub_at, datetime.datetime.now().date())

    def test_netloc(self):
        p = Post.objects.get(title="Hello World")
        self.assertEqual(p.netloc, "simplifiedweb.netlify.app")
