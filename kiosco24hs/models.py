from django.db import models

# Create your models here.
class stores(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name  

class products(models.Model):
    title = models.CharField(max_length=100)
    price = models.FloatField()
    store = models.ForeignKey(stores,on_delete=models.CASCADE)
    vendido = models.BooleanField(default=False)

    def __str__(self):
        return self.title
    
class Comment(models.Model):
    product = models.ForeignKey(
        products,
        on_delete=models.CASCADE,
        related_name="comments"
    )
    author = models.CharField(max_length=100)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Comentario de {self.author} en {self.product.title}"
