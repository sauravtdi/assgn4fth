from .models import User
from .serializers import UserSerializer
from rest_framework import viewsets
from rest_framework.response import Response


class UserViewSet(viewsets.ViewSet):
    """
    A simple ViewSet for listing or retrieving users.
    """

    def list(self, request):
        queryset = User.objects.all()
        serializer = UserSerializer(queryset, many=True)
        if len(serializer.data):
            success = True
            found = serializer.data
            status = 200
        else:
            success = False
            found = "Not Found"
            status = 204
        data = {'ok': success, 'members': found}
        return Response(data, status=status)
