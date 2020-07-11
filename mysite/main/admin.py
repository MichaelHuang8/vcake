from django.contrib import admin
from .models import Basic, Customized

class BasicAdmin(admin.ModelAdmin):
	fields = ["name",
              "price",
              "image",
              ]

class CustomizedAdmin(admin.ModelAdmin):
	fields = ["name",
              "price",
              "image",
              ]


# Register your models here.
admin.site.register(Basic, BasicAdmin)
admin.site.register(Customized, CustomizedAdmin)