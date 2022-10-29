from django.db import models
from subscriptions.models import Subscription

from users.models import Baseclass

# Create your models here.
class Alarm(Baseclass):
    subscription = models.OneToOneField(Subscription, verbose_name='구독정보', on_delete=models.CASCADE, related_name='alarm_subscription')
    d_day = models.PositiveSmallIntegerField(verbose_name='알람 발송일', help_text='5 입력시 결제 5일전 발송')
    is_active = models.BooleanField(verbose_name="메일 발송 여부", default=False)

    def __str__(self):
        return f"({self.alarm})의 히스토리"
    
    class Meta:
        verbose_name = '알림 정보'
        verbose_name_plural = "알림 정보 목록"

class AlarmHistory(Baseclass):
    alarm = models.ForeignKey(Alarm, verbose_name='알람', on_delete=models.SET_NULL, null=True, blank=True)
    content = models.TextField(verbose_name='히스토리 내역', default='', blank=True, help_text='발송시 메일 내용을 그대로 넣어줍니다.')
    is_success = models.BooleanField(verbose_name='발송 성공 여부', default=False)
    traceback = models.TextField(verbose_name='발송 실패 원인', default='', blank=True)

    def __str__(self):
        return f"({self.alarm})의 히스토리"

    class Meta:
        verbose_name = '알림 히스토리'
        verbose_name_plural = "알림 히스토리 목록"