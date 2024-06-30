from django.db import models
from ai.utils import summarize_text, detect_fake_news

class Article(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    summary = models.TextField(blank=True, null=True)
    is_fake_news = models.BooleanField(default=False)
    published_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if not self.summary:
            self.summary = summarize_text(self.content)
        self.is_fake_news = detect_fake_news(self.content)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title



