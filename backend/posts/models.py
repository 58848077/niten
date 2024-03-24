import uuid
from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()

class Comment(models.Model):
    id = models.CharField(max_length=36, primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.CharField(max_length=100)
    create_time = models.DateTimeField(auto_now_add=True)
    edit_time = models.DateTimeField(auto_now=True)
    
    @property
    def on(self):
        post = Post.objects.get()
    
    def __str__(self):
        return f"{self.user.name}"
    
class Post(models.Model):
    """
    no likes, likes is poison.
    """
    id = models.CharField(max_length=36, primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    pic_url = models.TextField()
    image = models.ForeignKey("PostImage", on_delete=models.SET_NULL, null=True)
    desc = models.TextField(blank=False)
    comment = models.ManyToManyField(Comment, through='PostComment', through_fields=('post', 'comment'))
    is_archived = models.BooleanField(default=False)
    create_time = models.DateTimeField(auto_now_add=True)
    edit_time = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"{self.user.name}, {self.name} {'(已封存)' if self.is_archived else ''}"
    
    def belongs_to(self):
        return self.user.name
    
class PostComment(models.Model):
    id = models.CharField(max_length=36, primary_key=True, default=uuid.uuid4, editable=False)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE)
    
    create_time = models.DateTimeField(auto_now_add=True)
    edit_time = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"{self.comment.user.name} 於 {self.post.name}的評論, 建立於{self.create_time.strftime('%Y-%m-%d %H:%M:%S')}"
    
class PostImage(models.Model):
    """
    定時檢查：刪除在Post中找不到對應貼文的圖片
    """
    type_choices = (
        ("none", "none"),
        ("item", "item"),
        ("people", "people"),
        ("landscope", "landscope"),
    )
    id = models.CharField(max_length=36, primary_key=True, default=uuid.uuid4, editable=False)
    image_id = models.CharField(max_length=100)
    link = models.TextField()   # image url
    type = models.CharField(max_length=50, choices=type_choices, default=type_choices[0][0])
    
    create_time = models.DateTimeField(auto_now_add=True)
    edit_time = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        post = Post.objects.filter(image=self.id).first()
        return f"{post.name}" if post else "對應貼文已被刪除"
