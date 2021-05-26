from django.core.validators import FileExtensionValidator
from django.db import models
from profiles.models import Profile

TAG_CHOICES = (
    ('adventure', 'adventure'),
    ('arcade', 'arcade'),
    ('battleroyale', 'battleroyale'),
    ('fps', 'fps'),
    ('mmorpg', 'mmorpg'),
    ('moba', 'moba'),
    ('rpg', 'rpg'),
    ('racing', 'racing'),
    ('sandbox', 'sandbox'),
    ('shooter', 'shooter'),
    ('simulator', 'simulator'),
    ('sport', 'sport'),
    ('survival', 'survival'),
    ('tactical', 'tactical'),
    ('other', 'other'),
)


# Create your models here.
class Post(models.Model):
    content = models.TextField()
    image = models.ImageField(upload_to='posts', validators=[FileExtensionValidator(['png', 'jpg', 'jpeg'])],
                              blank=True)
    upvoted = models.ManyToManyField(Profile, blank=True, related_name='upvotes')
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='posts')
    tags = models.CharField(max_length=20, choices=TAG_CHOICES, default='adventure')

    def __str__(self):
        return str(self.content[:20])

    def num_upvote(self):
        return self.upvoted.all().count()

    def num_comments(self):
        return self.comment_set.all().count()

    class Meta:
        ordering = ('-created',)


class Comment(models.Model):
    user = models.ForeignKey(Profile, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    body = models.TextField(max_length=300)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.pk)


UPVOTE_CHOICES = (
    ('Upvote', 'Upvote'),
    ('Downvote', 'Downvote'),
)


class Upvote(models.Model):
    user = models.ForeignKey(Profile, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    value = models.CharField(choices=UPVOTE_CHOICES, max_length=8)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user}-{self.post}-{self.value}"
