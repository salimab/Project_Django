from django.db import models
from django.urls import reverse_lazy
# Create your models here.
from django.template.defaultfilters import slugify


class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, max_length=256)
    slug = models.SlugField(unique=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Mate:
        ordering = ('name',)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse_lazy('product_list_by_category', args=[self.slug])


class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    description = models.TextField(blank=True)
    slug = models.SlugField(unique=True, blank=True)
    category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE)

    class Mate:
        ordering = ('name',)

    def __str__(self):
        return self.name

    def save(self, *args, **Kwargs):
        if not self.id:
            self.slug = slugify(self.name)

        super().save(*args, **Kwargs)

    def get_absolute_url(self):
        return reverse_lazy('product_detail', args=[self.slug])