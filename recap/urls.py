from django.conf import settings
from django.urls import path
from django.conf.urls.static import static
from . import views

urlpatterns=[
    path('',views.student_list,name='student'),

    path('add_student/',views.add_student,name='add'),

    path('update_student/<int:student_id>',views.update_student,name='update'),

    path('delete/<int:student_id>',views.delete_student,name='delete')

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)