# permissions module has all of base permission classes for DRF
from rest_framework import permissions

class UpdateOwnProfile(permissions.BasePermission):
    """Allow users to edit their own profile"""

    # hasObject Permission : every time request is made by API,
    # it resolve and determine whether it has permission or not
    # return true or false
    def has_object_permission(self, request, view, obj):
        """Check user is trying to edit their own profile."""
        # allow to view any files on the system
        # Only allows GET, HEAD, OPTIONS request
        if request.method in permissions.SAFE_METHODS:
            return True
            # Safe methods : HTTP methods which is classified SAFE_METHODS
        else:
            return obj.id == request.user.id
