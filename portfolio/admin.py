from pagedown.widgets import AdminPagedownWidget
from django.contrib.flatpages.models import FlatPage
from django.contrib import admin
from sorl.thumbnail.admin import AdminImageMixin

from .models import *


class ImageInline(AdminImageMixin, admin.TabularInline):
    model = Images
    extra = 0
    # verbose_name = 'файл'
    # verbose_name_plural = 'галерея'
    # fields = ('image', 'name', 'description')
    show_change_link = True


# @admin.register(Projects)
class ProjectsAdmin(admin.ModelAdmin):
    actions = ['make_published', ]
    actions_selection_counter = False
    date_hierarchy = 'create_date'
    empty_value_display = '-пусто-'
    # exclude = ('slug',)
    fieldsets = [
        (None,
         {'fields': ['customer', 'name', 'description', 'category', 'tool', 'create_date'],
          # 'description': '<p>Необязательный HTML текст, который будет отображаться над полями</p><hr>'
          }),
        ('ДОПОЛНИТЕЛЬНЫЕ НАСТРОЙКИ',
         {'fields': ['status', 'slider', 'comment', 'slug'], 'classes': ['collapse'],  # extrapretty, wide, collapse
          }),
    ]
    formfield_overrides = {models.TextField: {'widget': AdminPagedownWidget(show_preview=False)}, }
    inlines = (ImageInline, )
    list_filter = ('create_date', 'category')  # admin.RelatedOnlyFieldListFilter
    list_display = ('name', 'category', 'customer', 'create_date', 'status', )
    ordering = ('-create_date',)
    prepopulated_fields = {'slug': ['name']}
    radio_fields = {'category': admin.HORIZONTAL}
    raw_id_fields = ['tool']
    # readonly_fields = ('tool', )

    def make_published(self, request, queryset):
        rows_updated = queryset.update(status=True)
        if rows_updated == 1:
            message_bit = "1 проект был"
        else:
            message_bit = "%s stories were" % rows_updated
        self.message_user(request, "%s успешно  опубликован." % message_bit)

    make_published.short_description = "Опубликовать выбранные проекты"


class FlatPageAdmin(admin.ModelAdmin):
    list_display = ('title', 'url', )
    fieldsets = [
        (None,
         {'fields': ['url', 'title', 'content'], }),
        ('ДОПОЛНИТЕЛЬНЫЕ НАСТРОЙКИ',
         {'fields': ['enable_comments', 'template_name', 'registration_required', 'sites'], 'classes': ['collapse'], }),
    ]
    formfield_overrides = {models.TextField: {'widget': AdminPagedownWidget}, }
    ordering = ('title',)


admin.site.site_header = 'Portfolio Sergart'
admin.site.index_title = 'Управление приложениями'

admin.site.unregister(FlatPage)
admin.site.register(FlatPage, FlatPageAdmin)
admin.site.register(Projects, ProjectsAdmin)
admin.site.register(Customers)
admin.site.register(Tools)
