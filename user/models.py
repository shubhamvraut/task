from django.contrib.auth.base_user import BaseUserManager, AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.db import models

# Create your models here.
class UserManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, username, password, **extra_fields):
        if not username:
            raise ValueError('The given email must be set')
        user = self.model(username=username, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, username, password=None, **extra_fields):
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(username, password, **extra_fields)

    def create_superuser(self, username, password, **extra_fields):
        extra_fields.setdefault('is_superuser', True)
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')
        return self._create_user(username, password, **extra_fields)

class User(AbstractBaseUser, PermissionsMixin):
    mobile_no = models.CharField(max_length=20, blank=True, null=True,db_column='mobile_no', )
    address = models.CharField(max_length=200,db_column='address', null=True)
    city=models.CharField(max_length=40, blank=True,db_column='city',)
    profile_pic = models.FileField(upload_to='user/',null=True,db_column='profile_pic',)
    username = models.CharField( max_length=100, unique=True,db_column='username')
    secret_code=models.CharField( max_length=20,db_column='secret_code')
    qr_code = models.FileField(upload_to='bin/', blank=True, null=True,db_column='qr_code')
    is_staff = models.BooleanField(default=True)
    created_at = models.DateTimeField(max_length=40,null=False,auto_now=True, blank=False,db_column='created_at',)

    objects = UserManager()
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []

    class Meta:
        db_table = "user"

