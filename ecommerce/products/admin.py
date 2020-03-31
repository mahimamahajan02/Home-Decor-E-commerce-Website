




from django.contrib import admin

from .models import Product

from import_export.admin import ImportExportModelAdmin

class ProductAdmin(ImportExportModelAdmin):
	list_display = ['__str__','slug']
	class Meta:
		model = Product

admin.site.register(Product,ProductAdmin)
# Register your models here.
