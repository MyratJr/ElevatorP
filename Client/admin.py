from django.contrib import admin
from unfold.admin import ModelAdmin
from .models import Advertisement, Group, Elevator
from django.utils.safestring import mark_safe
import pathlib
from django.utils.html import format_html
import unfold
from django.utils import timezone


class ElevatorAdmin(unfold.admin.StackedInline):
    model = Elevator
    readonly_fields = ["last_connection", "date_created"]


@admin.register(Advertisement)
class AdvertisementAdmin(ModelAdmin):
    def image_preview(self, obj):
        if obj.media:
            media_format = pathlib.Path(obj.media.url).suffix
            if media_format in [".jpg", ".JPG", ".png", ".PNG", ".gif", ".GIF", ".jpeg", ".JPEG", ".bmp", ".BMP", ".tiff", ".TIFF", ".svg", ".SVG", ".ai", ".AI", ".eps", ".EPS", ".webp", ".WEBP", ".heif", ".HEIF", ".avif", ".AVIF"]:
                return mark_safe('<img src="%s" />' % obj.media.url)
            elif media_format in [".mp4", ".MP4", ".avi", ".AVI", ".mov", ".MOV", ".flv", ".FLV", ".mkv", ".MKV", ".wmv", ".WMV", ".webm", ".WEBM", ".vob", ".VOB", ".3gp", ".3GP", ".hevc", ".HEVC"]:
                return mark_safe('<video style="height:300px;margin: 0 auto;" controls loop><source src="%s" type="video/mp4"> </video>' % obj.media.url)
        return "Медиафайлы не могут быть видны."
    image_preview.short_description = "Предварительный просмотр медиа:"
    readonly_fields = ('image_preview',"date_created")

    def get_fields(self, request, obj=None):
        fields = super().get_fields(request, obj)
        if obj is None:  # If adding a new object
            fields.remove('image_preview')
            fields.remove('date_created')
        return fields
    search_fields = ["parent__name", "title"]
    

@admin.register(Group)
class GroupAdmin(ModelAdmin):
    # inlines = [ElevatorAdmin, AdvertisementAdmin]
    search_fields = ["name"]


@admin.register(Elevator)
class ElevatorAdmin(ModelAdmin):
    list_display = ('name', "colored_status_counter", "time_status")
    ordering = ["last_connection"]
    readonly_fields = ["last_connection", "date_created"]
    search_fields = ["parent__name", "name"]

    def time_status(self, obj):
        now = timezone.now()
        max_value = 60
        percentage = 0
        if obj.last_connection:
            time_diff = now - obj.last_connection
            minutes = int(time_diff.total_seconds() / 60)
            hours = 0
            percentage = min(minutes / max_value, 1)

            if minutes > 60:
                hours = int(minutes / 60)
                minutes = minutes % 60
        else:
            minutes = 0
        
        red = int(255 * percentage)
        green = int(255 * (1 - percentage))
        color = f'rgb({red}, {green}, 0)'

        if hours == 0 and minutes <= 5:
            return format_html(
                '<strong style="color: {};">Все в порядке</strong>',
                color
            )
        return format_html(
            '<strong style="color: {};">Нет связи уже {} часов {} минут.</strong>',
            color, hours, minutes
        )

    time_status.short_description = 'Статус соединения'
   
    def colored_status_counter(self, obj):
        now = timezone.now()
        if obj.last_connection:
            time_diff = now - obj.last_connection
            minutes = int(time_diff.total_seconds() / 60)
        else:
            minutes = 0
        max_value = 60
        percentage = min(minutes / max_value, 1)
        
        red = int(255 * percentage)
        green = int(255 * (1 - percentage))
        color = f'rgb({red}, {green}, 0)'
        return format_html(
            '<div style="width: 20px; height: 20px; border-radius: 50%; background-color: {}; display: inline-block;"></div>',
            color
        )
    
    colored_status_counter.short_description = 'Статус'
    def get_fields(self, request, obj=None):
        fields = super().get_fields(request, obj)
        if obj is None:  # If adding a new object
            fields.remove('last_connection')
            fields.remove('date_created')
        return fields