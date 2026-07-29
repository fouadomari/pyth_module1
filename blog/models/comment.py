from django.db import models
from .post import Post
from .user import User

class Comment(models.Model):
    # تعديل هذا السطر أيضاً
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments', null=True, blank=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Comment by {self.user.name if self.user else 'Unknown'} on {self.post.title[:20]}"
