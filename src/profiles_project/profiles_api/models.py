# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

#Abstract UserModel: Built-in UserModel
from django.contrib.auth.models import AbstractBaseUser

#UserModel Permission
from django.contrib.auth.models import PermissionsMixin

# Built in BaseUserManager... we're gonna customize it
from django.contrib.auth.models import BaseUserManager

class UserProfileManager(BaseUserManager):
    """Helps Django work with our custom user model."""

    def create_user(self, email, name, password=None):
        """create a new user profile object."""
        if not email:
            raise ValueError('Users must have an email address')

        # normalize_email is funcion which normalize as lower case characters
        email = self.normalize_email(email)
        user = self.model(email=email, name=name)

        # set the password
        # it's encrypt the password for us. Hash function
        user.set_password(password)

        user.save(using=self._db)
        return user

    def create_superuser(self, email, name, password):
        """Create and saves a new superuser with given details."""
        user = self.create_user(email, name, password)
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)
        return user


# Create your models here.
class UserProfile(AbstractBaseUser, PermissionsMixin):
    """ User Profile """
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    # is_active is required
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    # ObjectManager is to manage the UserProfile... it's required!
    objects = UserProfileManager()

    # When we set sth as USERNAME_FIELD, it goes to REQUIRED_FIELDS
    USERNAME_FIELD = 'email'
    # So you don't need to specify email into the REQUIRED_FIELDS
    REQUIRED_FIELDS = ['name']

    # since it's class function, we put self in the parameter
    def get_full_name(self):
        """Used to get a users full name"""
        return self.name

    def get_short_name(self):
        return self.name

    def __str__(self):
        """Django uses this when it needs to convert the object to a string"""
        return self.email

class ProfileFeedItem(models.Model):
    """Profile Status Update"""

    # Points to the user profile
    # if userProfile is deleted, feed is also deleted
    user_profile = models.ForeignKey('UserProfile', on_delete=models.CASCADE)
    status_text = models.CharField(max_length=255)
    # set current time
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.status_text
