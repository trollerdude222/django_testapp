from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from my_social_networkm.models import UserLink

def viewusers(request):
  something = get_object_or_404(UserLink,un=username)
  return HttpResponse("You're looking at all users ")
def viewfriends(request, username):
  something = get_object_or_404(UserLink,un=username)
  return HttpResponse("You're looking at user %s." % username)
def viewfollowers(request, username):
  something = get_object_or_404(UserLink,un=username)
  return HttpResponse("You're looking at user %s." % username)
def viewfollowing(request,username):
  something = get_object_or_404(UserLink,un=username)
  return HttpResponse("You're looking at user %s." % username)
