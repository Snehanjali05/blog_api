from rest_framework.permissions import BasePermission

class IsAuthorOrReadOnly(BasePermission):

  def has_permission(self, request, view):
    allowed_methods = ['GET','HEAD', 'OPTIONS']
    
    # Allow these specific methods for everyone
    if request.method in allowed_methods:
      return True 

    if request.method in ['POST']:
      return request.user.is_authenticated

    # Check if user is authenticated and accessing their own post
    return request.user.is_authenticated and request.user.username == view.get_object().author
