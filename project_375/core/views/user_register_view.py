from rest_framework.exceptions import ValidationError
from rest_framework.views import APIView
from rest_framework.response import Response
from ..models import User
from ..serializers import UserSerializer


class UserRegisterView(APIView):
    """
    Регистрация нового пользователя
    """
    def post(self, request, *args, **kwargs):
        validation = UserValidate(request.data)
        validation.validate()
        validation.user().save()
        return Response({'status': 'OK'}, status=200)


class UserValidate(ValidationError):
    def __init__(self, data):
        self.login = data.get('login')
        self.last_name = data.get('last_name')
        self.first_name = data.get('first_name')
        self.email = data.get('email')
        self.password = data.get('password')
        self.password_confirmation = data.get('password_confirmation')

    def validate(self):
        try:
            User.objects.get(login=self.login)
            raise ValidationError({
               'login': 'Такой пользователь уже существует',
            })
        except User.DoesNotExist:
            pass
        if self.password != self.password_confirmation:
            raise ValidationError({
                'password': 'Пароли не совпадают',
                'password_confirmation': 'Пароли не совпадают',
            })

    def user(self):
        user = User(
            login=self.login,
            email=self.email,
            last_name=self.last_name,
            first_name=self.first_name,
            #password=self.password,
        )
        user.set_password(self.password)
        return user
