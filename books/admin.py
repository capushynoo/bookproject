from django.contrib import admin

# Register your models here.
from django.core.mail import send_mail

from .models import Customer, Book, Order, Request_Book, UserPrefferedCat

admin.site.register(Customer)
#admin.site.register(Book)
admin.site.register(Order)
admin.site.register(Request_Book)


@admin.register(Book)
class MyAdminView(admin.ModelAdmin):
    def save_model(self, request, obj, form, change):
        print(obj.book_name)
        print(obj.category)
        for pref in UserPrefferedCat.objects.filter(
            category=obj.category
        ):
            print(pref.user)
            send_mail(
                f'BookProject! Book with your favourite genre appeared!',
                f'Book with your favourite genre ({obj.category}) appeared: {obj.book_name}',
                'bookproject.notificaitons@gmail.com',
                [pref.user.email],
                fail_silently=False,
            )
        super(MyAdminView, self).save_model(request, obj, form, change)