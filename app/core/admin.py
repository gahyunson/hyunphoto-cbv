from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.utils.translation import gettext_lazy as _
from django.shortcuts import render
from django.urls import path
import tempfile

from django.http import JsonResponse

from photos.views import PhotoView
from core import models


class UserAdmin(BaseUserAdmin):
    ordering = ['id']
    list_display = ['email', 'name', 'is_active']
    # list_editable = ('is_active',)
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        (_('Permissions'), {
            'fields': (
             'is_active',
             'is_staff',
             'is_superuser',
            )
        }),
        (_('Important dates'),
         {'fields': ('last_login',)}),
    )
    readonly_fields = ['last_login']
    add_fieldsets = (
        (None, {
            'classes': ('wide', ),
            'fields': (
                'email',
                'password1',
                'password2',
                'name',
                'is_active',
                'is_staff',
                'is_superuser',
            )
        })
    )

class PhotosAdmin(admin.ModelAdmin):
    def get_urls(self):
        urls = super().get_urls()
        # print('urls is', urls)
        custom_urls = [
            path('create_photo/', self.create_photo_view),
        ]
        return custom_urls + urls

    def create_photo_view(self, request):
        if request.method == 'GET':
            return render(request, 'admin/create_photo_form.html')

        elif request.method == 'POST':
            view = PhotoView.as_view()
            return view(request)
        return JsonResponse({'error': 'Failed to create photo'}, status=405)
            # url = 'http://127.0.0.1:8000/api/photos/'
            # title = request.POST.get('title')  # 'POST' 데이터 접근 방식 수정
            # image = request.FILES.get('image')  # 이미지 파일을 받습니다.
            # description = request.POST.get('description')
            # data = {'title': title,
            #         'description': description,
            #         'image': image
            #         }
            # response = request.POST(url, data)
            # if response.status_code == 201:
            #     return JsonResponse(response.json(), status=201)
            # else:
            #     return JsonResponse({'error': 'Failed to create photo'}, status=400)


    class Media:
        js = ('admin/js/create_photo.js',)


admin.site.register(models.User, UserAdmin)
admin.site.register(models.Photos, PhotosAdmin)
admin.site.register(models.Prices)
admin.site.register(models.Cart)
