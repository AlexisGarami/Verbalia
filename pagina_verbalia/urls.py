"""
URL configuration for pagina_verbalia project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from boletas import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('prueba/', views.prueba),
    path('signup/', views.signup, name='signup'),
    path('tasks/', views.tasks, name='tasks'),
    path('tasks/<int:task_id>/', views.task_detail, name='task_detail'),
    path('tasks/<int:task_id>/complete', views.complete_task, name='complete_task'),
    path('tasks/<int:task_id>/delete', views.delete_task, name='delete_task'),
    path('signout/', views.signout, name='signout'),
    path('signin/', views.signin, name='signin'),
    path('create_task/', views.create_task, name='create_task'),
    path('create_grade/', views.create_grade, name='create_grade'),
    path('create_grade_adults/', views.create_grade_adults, name='create_grade_adults'),
    path('inicio_plan/', views.inicio_plan, name='inicio_plan'),
    path('create_plan/<int:group_id>/', views.create_plan, name='create_plan'),
    path('inicio_performance/', views.inicio_performance, name='inicio_performance'),
    path('create_performance/<int:group_id>/<int:student_count>/', views.create_performance, name='create_performance'),
    path('select_student_count/<int:group_id>/', views.select_student_count, name='select_student_count'),
    path('inicio_attendance/', views.inicio_attendance, name='inicio_attendance'),
    path('select_attendance_count/<int:group_id>/', views.select_attendance_count, name='select_attendance_count'),
    path('create_attendance/<int:group_id>/<int:student_count>/', views.create_attendance, name='create_attendance'),
    path('edit_plan/<int:week_plan_id>/', views.edit_plan, name= 'edit_plan'),
    path('edit_performance/<int:performance_id>/', views.edit_performance, name='edit_performance'),
    path('view_performances', views.view_performances, name='view_performances'),
    path('performance_detail/<int:performance_id>/', views.performance_detail, name='performance_detail'),
    path('edit_attendance/<int:attendance_id>/', views.edit_attendance, name='edit_attendance'),
    path('view_attendances', views.view_attendances, name='view_attendances'),
    path('attendance_detail/<int:attendance_id>/', views.attendance_detail, name='attendance_detail'),
    path('view_plans', views.view_plans, name='view_plans'),
    path('plan_detail/<int:plan_id>/', views.plan_detail, name='plan_detail'),
    path('performances_for_week/<str:week>/', views.performances_for_week, name='performances_for_week'),
    path('attendances_for_week/<str:week>/', views.attendances_for_week, name='attendances_for_week'),
    path('plans_for_week/<str:week>/', views.plans_for_week, name='plans_for_week'),

]
