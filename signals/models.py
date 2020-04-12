from django.db import models
from django.urls import reverse
from django.db.models.signals import post_save,pre_save, post_delete


class Signal(models.Model):
    name = models.CharField(max_length=60)
    age  = models.IntegerField()
    complexion = models.CharField(max_length=10)
    job = models.CharField(max_length=30)

    def __str__(self):
        return self.name
    def get_detail_url(self):
        return reverse('details', kwargs={"id":self.id})
def save_model(sender,instance, **kwargs):
    print('something')

def delete_details(sender,instance, **kwargs):
    print('deleted')
post_delete.connect(delete_details, sender=Signal)
pre_save.connect(save_model,sender=Signal)
post_save.connect(save_model,sender=Signal,weak=True)