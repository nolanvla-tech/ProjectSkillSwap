from django.contrib import admin

from .models import Skill


@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    """Show the Skill model in the admin area."""
    list_display = ('title', 'owner', 'category', 'is_free', 'availability_status', 'created_at')
    list_filter = ('category', 'is_free', 'availability_status')
    search_fields = ('title', 'description', 'owner__username')
