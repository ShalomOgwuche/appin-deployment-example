from django.db import models

# Create your models here.
class Topic(models.Model):
    topic_name = models.CharField(max_length=264,unique=True)

    #string representation of Topic model, returning name of topic
    def __str__(self):
        return self.topic_name


class Webpage(models.Model):
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    name = models.CharField(max_length=264,unique=True)
    url = models.URLField(unique=True)

    #string representation of Webpage model
    def __str__(self):
        return self.name

class AccessRecord(models.Model):
    name  = models.ForeignKey(Webpage, on_delete=models.CASCADE)
    date = models.DateField()

#string representation of Webpage model
##As this is a date time object it needs to be casted as a string str(self.date)
    def __str__(self):
        return str(self.date)
