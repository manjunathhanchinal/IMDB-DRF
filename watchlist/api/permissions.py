from rest_framework import permissions

class IsAdminOrReadOnly(permissions.IsAdminUser):
    """
    Custom permission to only allow admin users to edit objects.
    """
    def has_permission(self, request, view):
        admin_permission = super().has_permission(request, view)
        if request.method in permissions.SAFE_METHODS:
            return True
        else:
            return request.method == 'GET' or admin_permission  
    
class ReviewUserOrReadOnly(permissions.BasePermission):
    """
    Custom permission to only allow the review user to edit or delete their review.
    """
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        else:
            return obj.review_user == request.user or request.user.is_staff