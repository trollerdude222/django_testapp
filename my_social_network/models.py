from django.db import models
from django.contrib.auth.models import User

# Create your models here.
#class UserLink(models.User):
  ##notification.send([to_user], "friends_invite", {"from_user": from_user})
class Author(models.Model):
    name = models.CharField(max_length=50)
class UserLink(models.Model):
    from_user = models.ForeignKey(User, related_name="invitations_from")
    to_user = models.ForeignKey(User, related_name="invitations_to")
    date_added=models.DateField()
    unique_together = ("from_user", "to_user")
    friends = models.ManyToManyField(Friend)
    def save():
      if from_user.name==to_user.name:
        return
      else:
        super(UserLink, self).save(*args, **kwargs)
    users=models.Manager() 

    all_entries = Entry.objects.all()
#userss spelt with 2s because users has been used already
userss = UserLink.objects.get(pk=1)
ussers.friends.add()
userss.save()

