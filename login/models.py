from django.db import models
import re
import bcrypt

# Create your models here.
class UserManager(models.Manager):
    def basic_validator(self, postData):
        errores = {}
        if len(User.objects.filter(username=postData['username'])) > 0:
            errores['existe'] = "Username already registered"
        else:
            if len(postData['name']) == 0:
                errores['name'] = "Name is required"
            if len(postData['username']) == 0:
                errores['username'] = "Username is required"
            if len(postData['password']) < 8:
                errores['password'] = "Password should be at least 8 characters"
            if postData['password'] != postData['password2']:
                errores['password'] = "Password does not match"
            if len(postData['name']) < 3:
                errores['name'] = "Name should be at least 3 characters"
            if len(postData['username']) < 3:
                errores['username'] = "Username should be at least 3 characters"
        return errores

    def encriptar(self, password):
        password = bcrypt.hashpw(password.encode(), bcrypt.gensalt())
        return password

    def validar_login(self, postData, usuario ):
        errores = {}
        if len(usuario) > 0:
            pw_given = postData['password']
            pw_hash = usuario[0].password

            if bcrypt.checkpw(pw_given.encode(), pw_hash.encode()) is False:
                errores['pass_incorrecto'] = "password es incorrecto"
        else:
            errores['usuario_invalido'] = "Usuario no existe"
        return errores

class User(models.Model):
    name = models.CharField(max_length=40)
    username = models.CharField(max_length=40)
    password = models.CharField(max_length=255)
    rol = models.PositiveIntegerField(default=1)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()

