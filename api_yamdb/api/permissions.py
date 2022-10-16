from rest_framework.permissions import BasePermission, SAFE_METHODS


class IsAdminOrReadOnly(BasePermission):
    """
    Редактирование возможно только для admin.
    Для чтения доступно всем.
    """
    def has_permission(self, request, view):
        return (request.method in SAFE_METHODS
                or (request.user.is_authenticated and (
                    request.user.is_admin or request.user.is_superuser)))


class IsAdmin(BasePermission):
    """
    Для редактирования объекта нужны права admin.
    """
    def has_permission(self, request, view):
        return (request.user.is_authenticated and request.user.is_admin)

    def has_object_permission(self, request, view, obj):
        return (request.user.is_authenticated and request.user.is_admin)


class IsModerator(BasePermission):
    """
    Для редактирования объекта нужен статус moderator.
    """
    def has_permission(self, request, view):
        return (request.user.is_authenticated and request.user.is_moderator)

    def has_object_permission(self, request, view, obj):
        return (request.user.is_authenticated and request.user.is_moderator)


class IsSuperuser(BasePermission):
    """
    Для редактирования объекта нужен статус superuser.
    """
    def has_permission(self, request, view):
        return (request.user.is_authenticated and request.user.is_superuser)

    def has_object_permission(self, request, view, obj):
        return (request.user.is_authenticated and request.user.is_superuser)


class IsAuthor(BasePermission):

    def has_object_permission(self, request, view, obj):
        return request.method in SAFE_METHODS or obj.author == request.user
