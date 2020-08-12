from django.urls import path
from . import views

app_name = "item"
urlpatterns = [
    path('', views.index, name="my_index"),

    path('new_item', views.new_item, name="my_new_item"),

    path('item/<int:item_id>', views.item_info, name="my_item_info"),

    path('category/<int:category_id>',
         views.category_page, name="my_category_page"),

    path('user/<int:user_id>', views.user_page, name="my_user_page"),

    path('create_item', views.create_item, name="my_create_item"),

    path('item/<int:item_id>/edit', views.edit, name="my_edit_item"),

    path('post_edit/<int:item_id>', views.post_edit, name="my_post_edit_item"),

    path('item/<int:item_id>/delete', views.delete, name="my_delete_item"),

    path('new_review', views.new_review, name="my_new_review"),

    path('post_message', views.post_message, name="my_post_message"),

    path('post_comment', views.post_comment, name="my_post_comment"),

    path('all_listings', views.all_listings, name="my_all_listings"),

    path('flag_item/<int:item_id>', views.flag_item, name="my_flag_item"),

    path('admin_flag_control/<int:item_id>',
         views.admin_flag_control, name="my_admin_flag_control"),

    path('all_categories', views.all_categories, name="my_all_categories"),
]
