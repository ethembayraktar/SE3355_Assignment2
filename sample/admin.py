from django.contrib import admin
from sample.models import Sample
# Register your models here.
class SampleAdmin(admin.ModelAdmin):
    list_display=['title1','category','price']
    list_filter=['title1','category']
    list_display_links= ['title1']

    class Meta:
        model = Sample

admin.site.register(Sample, SampleAdmin)