from rest_framework import permissions


class IsOwner(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        if request.user and request.user.is_staff:
            return True

        return obj.owner == request.user


class IsShared(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        if request.user and request.user.is_staff:
            return True

        return obj.shared_to == request.user

