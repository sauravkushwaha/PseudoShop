from django.db import models

class Blogpost(models.Model):
    post_id = models.AutoField(primary_key= True)
    tilte = models.CharField(max_length=60)
    head0 = models.CharField(max_length=600, default="")
    contant0 = models.CharField(max_length=6000, default="")
    head1 = models.CharField(max_length=600, default="")
    contant1 = models.CharField(max_length=6000, default="")
    head2 = models.CharField(max_length=600, default="")
    contant2 = models.CharField(max_length=6000, default="")
    pub_date = models.DateField()
    thumbnail = models.ImageField(upload_to='shop/images', default="")

    def __str__(self):
        return self.tilte