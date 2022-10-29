from django.contrib import admin

from subscriptions.models import Billing, Category, Plan, Service, Subscription

# Register your models here.
admin.site.register(Category)
admin.site.register(Service)
admin.site.register(Plan)
admin.site.register(Billing)
admin.site.register(Subscription)
