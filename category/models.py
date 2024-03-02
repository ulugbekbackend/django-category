from django.db import models

# Create your models here.

class Category(models.Model):
    paret=models.ForeignKey('self',related_name='children',on_delete=models.CASCADE,blank=True,null=True)
    title=models.CharField(max_length=100)
    created_at=models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title
    
    class Meta:
        def __str__(self):
            full_path=[self.title]
            k=self.paret
            while k is not None:
                full_path.append(k.title)
                k=k.paret
            return '->'.join(full_path[::-1])
