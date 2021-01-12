from django.db import models

class Article(models.Model):
    article_title = models.CharField(("Title site"), max_length=100)
    article_text = models.TextField(("Site text"))
    pub_date = models.DateTimeField(("publication date"))

class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    author_name = models.CharField(("Name author"), max_length=50)
    comm_text = models.CharField(("Comment text"), max_length=100)

