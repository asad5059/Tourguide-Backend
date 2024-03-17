from rest_framework import permissions

class IsPermittedForAction(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method=='GET':
            return True
        if obj.owner == request.user:
            return True
        return False