from django.contrib import admin
from subscriptions.models import Company, Type, Billing, Category, Service, Plan, Subscription

from django.utils import timezone
from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta


# Register your models here.

admin.site.register(Type)
""" 최선우 : Type Model을 Admin Site에 등록 """


admin.site.register(Company)
""" 최선우 : Company Model을 Admin Site에 등록 """


@admin.register(Billing)
class BillingAdmin(admin.ModelAdmin):
    """
    최선우 : Billing Model을 Admin Site에 등록
    """
    list_display = ["user", "type", "company"]
  
    
admin.site.register(Category)
""" 최선우 : Category Model을 Admin Site에 등록 """


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    """
    최선우 : Service Model을 Admin Site에 등록
    """
    list_display = ["name", "category"]
   
    
@admin.register(Plan)
class PlanAdmin(admin.ModelAdmin):
    """
    최선우 : Plan Model을 Admin Site에 등록
    """
    list_display = ["name", "service", "price"]
  
    
@admin.register(Subscription)
class subscriptionAdmin(admin.ModelAdmin):
    """
    최선우 : Subscription Model을 Admin Site에 등록
    """
    list_display = ["user", "get_category", "plan", "billing", "started_at", "get_billing_at", "expire_at", "is_active"]
    
    @admin.display(description="카테고리")
    def get_category(self, obj):
        return obj.plan.service.category
    
    @admin.display(description="다음 결제 예정일")
    def get_billing_at(self, obj):
        """
        결제 예정일 : 구독 시작일로부터 갱신일자를 추출 후, 현재 날짜와 비교하여 계산
        """
        renewal_day = obj.started_at.day
        today = datetime.now() + relativedelta(hours=9)
        pay_year, pay_month, pay_day = today.year, today.month, renewal_day
        
        if renewal_day < today.day:
            if today.month == 12:
                pay_year += 1
                pay_month = 1
            else:
                pay_month += 1    
                
        next_billing_at = datetime(pay_year, pay_month, pay_day).date()
        return 