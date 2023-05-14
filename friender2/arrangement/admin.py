from django.contrib import admin
from .models import *
from django.utils.html import format_html

class UserRatingInline(admin.TabularInline):
    model = UserRating
    extra = 2
class HobbiesInline(admin.StackedInline):
    model = Hobbies.user.through

@admin.action(description="Change city")
def change_city(modeladmin, request, queryset):
    queryset.update(city="Baranovichi")

color_code = 'ffd700'

# @admin.display(description='ФИО')
# def upper_case_name(obj):
#     return f'{obj.name} {obj.surname}'.upper()

@admin.register(Users)
class UserAdmin(admin.ModelAdmin):

    @admin.display
    def colored_name(self):
        return format_html(
            '<span style="color: #{};">{} {}</span>',
            color_code,
            self.name,
            self.surname,
        )
    fields = ["name", 'surname', 'age', 'email', 'sex', 'city']
    list_display = [colored_name, 'name', 'surname', 'age', 'sex', 'city']
    list_display_links = [colored_name, 'name', 'surname']
    list_editable = ['age', 'city']
    search_fields = ['sex', 'city', 'age']
    list_filter = ['sex', 'city', 'age']
    inlines = [
        UserRatingInline,
        HobbiesInline,
    ]
    actions = [change_city]
# admin.site.register(Users, UserAdmin)
admin.site.register(UserRating)
admin.site.register(Hobbies)
admin.site.register(User_establishment)
admin.site.register(EstablishmentsRating)
admin.site.register(Passport)
admin.site.register(Arrangements)
admin.site.register(Host)
admin.site.register(Guest)

# Register your models here.
