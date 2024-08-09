from rest_framework import permissions


class IsOwnReader(permissions.BasePermission):

    def has_permission(self, request, view):
        # NB: In case we want to make sure this handles
        # Authentication checks as well. Else, it can be 
        # used together with IsAuthenticated
        if request.user.is_authenticated:
            return True
        return False

    def has_object_permission(self, request, view, obj):
        # # NB: If we want the superuser to have control
        # if request.user.is_superuser:
        #    return True
        
        # # NB: If we want methods that don't change the state of
        # # database to pass freely.
        # if request.method in permissions.SAFE_METHODS:
        #    return True 
        
        # TODO: Compare ideas.
        if obj.user.id == request.user.id:
            return True
        
        return False
