from django.db import models

from users.models import Baseclass

# Create your models here.
class Category(Baseclass):
    # OTT = 1
    # MUSIC = 2
    # BOOK = 3
    # ECOMMERCE = 4
    # SOFTWARE = 5
    # DELIEVERY = 6
    # RENTAL = 7

    SERVICE_TYPE = [
        (1, 'OTT'), (2, '음악'),
        (3, '도서'), (4, '이커머스'),
        (5, '소프트웨어'), (6, '정기배송'),
        (7, '렌탈'),
    ]
    type = models.PositiveSmallIntegerField(verbose_name='카테고리 종류', choices=SERVICE_TYPE)
		
    def __str__(self):
        return self.get_type_display()
    
    class Meta:
        verbose_name = '카테고리'
        verbose_name_plural = "카테고리 목록"

class Service(Baseclass):
    name = models.CharField(verbose_name='서비스명', max_length=50, unique=True)
    category = models.ForeignKey(Category, verbose_name='카테고리', on_delete=models.CASCADE, related_name='service_category')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '서비스'
        verbose_name_plural = "서비스 목록"

class Plan(Baseclass):
    service = models.ForeignKey(Service, verbose_name='서비스', on_delete=models.CASCADE, related_name='plan_service')
    name = models.CharField(verbose_name='구독플랜', max_length=50)
    price = models.PositiveIntegerField(verbose_name='가격')
    
    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '구독 플랜'
        verbose_name_plural = "구독 플랜 목록"

class Billing(Baseclass):
    method = models.CharField(verbose_name='결제수단', max_length=50)
    user = models.ForeignKey('users.User', verbose_name='유저', on_delete=models.CASCADE, related_name="billing_user")

    def __str__(self):
        return self.method

    class Meta:
        verbose_name = '결제 정보'
        verbose_name_plural = "결제 정보 목록"

class Subscription(Baseclass):
    user = models.ForeignKey('users.User', verbose_name='유저', on_delete=models.CASCADE, related_name='subscription_user')
    plan = models.ForeignKey(Plan, verbose_name='구독플랜', on_delete=models.CASCADE)
    billing = models.ForeignKey(Billing, verbose_name='결제 정보', on_delete=models.CASCADE, related_name='subscription_billing')
    started_at = models.DateField(verbose_name='최초 구독일')
    expire_at = models.PositiveSmallIntegerField(verbose_name='구독 만료일', null=True)

    def __str__(self):
        return str(self.user)

    class Meta:
        verbose_name = '사용자 구독 정보'
        verbose_name_plural = "사용자 구독 정보 목록"