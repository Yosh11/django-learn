import datetime

from django.db import models
from django.utils import timezone

class Article(models.Model):
    article_title = models.CharField(("Title site"), max_length=100)
    article_text = models.TextField(("Site text"))
    pub_date = models.DateTimeField(("publication date"))
    
    def __str__(self):
        return self.article_title
    
    def was_published_recently(self):
        return self.pub_date >= (timezone.now() - datetime.timedelta(days=7))
    
    class Meta:
        """
        Russification
        """
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'

class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    author_name = models.CharField(("Name author"), max_length=50)
    comm_text = models.CharField(("Comment text"), max_length=100)

    def __str__(self):
        """Output format

        Returns:
            Obj: name author
        """
        return self.author_name

    class Meta:
        """
        Russification
        """
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'