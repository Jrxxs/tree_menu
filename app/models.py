from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=200, default="New Category")
    parent = models.ForeignKey('self', related_name='child', on_delete=models.CASCADE, blank=True, null=True)

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'


    def __str__(self) -> str:
        return self.name