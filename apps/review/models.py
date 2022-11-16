from django.db import models
from django.contrib.auth import get_user_model

from apps.product.models import Product


User = get_user_model()

class Comment(models.Model):
    user = models.ForeignKey(
        to=User,
        on_delete=models.CASCADE,
        related_name='comments'
    )
    text = models.TextField()
    product = models.ForeignKey(
        to=Product, # 'apps.product.models.Product',
        on_delete=models.CASCADE,
        related_name='comments'
    )
    created_at = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(
        upload_to='comments_images', 
        blank=True, 
        null=True
        )

    def __str___(self):
        return f'Comment from {self.user.username} to {self.product.title}'
    