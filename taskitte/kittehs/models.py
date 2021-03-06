from django.db import models
import string

# Create your models here.

class List(models.Model):
    name = models.CharField(max_length="30")
    def __unicode__(self):
        return self.name
    
    
class Task(models.Model):
    list = models.ForeignKey('List')
    name = models.CharField(max_length="50")
    description = models.TextField(max_length="280", blank=True, null=True)
    even_more_info = models.URLField(blank=True, null=True)
    contact_name = models.CharField(max_length="30")
    contact_email = models.EmailField()
    is_claimed = models.BooleanField(default=False)
    accepts_mult_claimants = models.BooleanField(default=False)
    # if is_claimed and !accepts_mult_claimants, this is inherently true
    is_closed = models.BooleanField(default=False)
    claimants = models.ManyToManyField('Person', blank=True, null=True)
    email_list = models.OneToOneField('TinyMailingList', blank=True, null=True)
    def __unicode__(self):
        return u'%s%s%s' % (self.list, " task #", self.pk)
    
class Person(models.Model):
    name = models.CharField(max_length="30")
    email = models.EmailField()
    def __unicode__(self):
        return self.name
    
class TinyMailingList(models.Model):
    name = models.CharField(max_length="30")
    members = models.ManyToManyField('Person')
    def name_generator(self):
        part_one = truncate(strip(self.task.list.name,string.punctuation),10)
        part_two = truncate(strip(self.task.name,string.punctuation),15)
        pk = self.pk
        return part_one + '-' + part_two + '-' + str(pk)
    def __unicode__(self):
        return u'%s%s' % (self.name, "@taskitte.com")
        
def truncate(string, n):
    '''shortens a string to length n, then cuts off further at the next available space, if any'''
    if string.length > n:
        string = string[0:n-1]
    reversed_string = string[::-1]
    # looks for the first space in the reversed string 
    # (that is, the space closed to the end of the original string)
    for index in range(0, reversed_string.length - 1):
        if reversed_string[index] == ' ':
            # chops string off at the space
            reversed_string = reversed_string[index+1:]
            break
    # let's put our string back in order!
    string = reversed_string[::-1]
    return string
    