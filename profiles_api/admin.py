from django.contrib import admin

from profiles_api import models


class CapsuleImageAdmin(admin.StackedInline):
    model = models.CapsuleImage




@admin.register(models.Capsule)
class CapsuleAdmin(admin.ModelAdmin):
    inlines = [CapsuleImageAdmin]

    class Meta:
        model = models.Capsule


@admin.register(models.CapsuleImage)
class CapsuleImageAdmin(admin.ModelAdmin):
    pass

@admin.register(models.UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    readonly_fields = ('date_of_creation',)