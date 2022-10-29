from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

# Create your models here.
class Baseclass(models.Model):
    created_at = models.DateTimeField(verbose_name="생성일", auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name="갱신일", auto_now=True)
    
    class Meta:
        abstract = True


class UserManager(BaseUserManager):
    def create_user(self, email, fullname, password=None):
        if not email:
            raise ValueError("Users must have an email address")
        if not password:
            raise ValueError("Users must have a password")
        email = self.normalize_email(email)
        user = self.model(
            email=email,
            fullname=fullname,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, fullname, password=None):
        user = self.create_user(email=email, fullname=fullname, password=password)
        user.is_admin = True
        user.save(using=self._db)
        return user

     
class User(Baseclass, AbstractBaseUser):
    email = models.EmailField(verbose_name="이메일", max_length=100, unique=True)
    fullname = models.CharField(verbose_name="이름", max_length=20)
    password = models.CharField(verbose_name="비밀번호", max_length=255)
    phone = models.CharField(verbose_name="휴대폰", max_length=15, null=True)
    picture = models.ImageField(verbose_name="프로필 사진", null=True, blank=True, upload_to="profile/image/")
    is_active = models.BooleanField(verbose_name="활성 여부", default=True)
    is_admin = models.BooleanField(verbose_name="관리자 여부", default=False)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["fullname", "password"]

    objects = UserManager()
    
    def __str__(self):
        return self.email
 
    # True를 반환하여 권한이 있음을 알림.
    def has_perm(self, perm, obj=None):
           return self.is_admin
    # True를 반환하여 주어진 앱의 모델에 접근이 가능하도록 함.
    def has_module_perms(self, app_label):
       return self.is_admin
   
    # True가 반환되면 Django의 관리자 화면에 로그인 가능.
    @property
    def is_staff(self):
        return self.is_admin
    
