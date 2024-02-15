from django.urls import path
from django.contrib.auth import views as auth_views
from .views import (user_login, user_signup, jobs_list, job_detail, job_apply,
                    create_job, update_job, job_delete, search_results, job_search)

app_name = 'jobs'

urlpatterns = [
    path("", jobs_list, name='jobs_list'),
    path("login/", user_login, name='login'),
    path("signup/", user_signup, name='signup'),
    path("<int:job_id>/detail/", job_detail, name='job_detail'),
    path("<int:job_id>/apply/", job_apply, name='job_apply'),
    path('create/', create_job, name='create_job'),
    path('<int:job_id>/update/', update_job, name='job_update'),
    path("<int:job_id>/delete/", job_delete, name='job_delete'),
    path('search/', job_search, name='job_search'),

]