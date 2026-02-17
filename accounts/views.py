from rest_framework import generics
from rest_framework.response import Response
from .serializers import CreateUserAccount, LoginUserAccountSerializer
from rest_framework.permissions import AllowAny


class CreatUserVaultAccountAPIView(generics.GenericAPIView):
    serializer_class = CreateUserAccount
    permission_classes=[AllowAny]

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(
            {'message':'Accont Created Successfully'}, status=201
        )
    


class LoginAccountAPIView(generics.GenericAPIView):
    serializer_class = LoginUserAccountSerializer
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = self.serializer_class(
            data=request.data,
            context={'request': request}
        )
        serializer.is_valid(raise_exception=True)
        return Response(serializer.data)
