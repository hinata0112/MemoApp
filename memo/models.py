from django.db import models

TAG = (
    ('study', '勉強'),
    ('work', '仕事'),
    ('private', 'プライベート'),
    ('other', 'その他'),
)

class Memo(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)  # 作成日時
    tag = models.CharField(
        max_length=100,
        choices = TAG,
        )

    def __str__(self):
        return self.title