from django.urls import path
from . import views

app_name = "login"
urlpatterns = [
    path('', views.index, name="my_index"),

    path('register', views.register_page, name="my_register_page"),

    path('register_submit', views.register, name="my_register"),

    path('login_submit', views.log_in, name="my_log_in"),

    path('dashboard', views.successful_log_in, name="my_successful_log_in"),

    path('admin_controls', views.admin_controls, name="my_admin_controls"),

    path('user/edit_user/<int:user_id>', views.edit_user, name="my_edit_user"),

    path('admin_controls/post_edit_user/<int:user_id>',
         views.post_edit_user, name="my_admin_post_edit_user"),

    path('user/delete_user/<int:user_id>',
         views.delete_user, name="my_delete_user"),

    path('admin_controls/post_new_cat',
         views.post_new_cat, name="my_admin_post_new_cat"),

    path('admin_controls/edit_category/<int:category_id>',
         views.edit_category, name="my_admin_edit_category"),

    path('admin_controls/post_edit_cat/<int:category_id>',
         views.post_edit_category, name="my_admin_post_edit_category"),

    path('admin_controls/delete_category/<int:category_id>',
         views.delete_category, name="my_admin_delete_category"),

    path('category/delete_category/<int:category_id>',
         views.delete_category, name="my_delete_category"),

    path('direct_message', views.direct_message, name="my_direct_message"),

    path('logout', views.log_out, name="my_log_out"),

]
