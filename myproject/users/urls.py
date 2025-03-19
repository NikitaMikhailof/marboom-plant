from django.urls import path
from . import views 
from . import utils


urlpatterns = [
    path('', views.PostListView.as_view(), name='home'),
    path('show_posts/<slug:cat_slug>/', views.CategoryListView.as_view(), name='show_category'),
    path('show_tags/<slug:tag_slug>/', views.TagListView.as_view() , name='show_tag'),
    path('autocomplete/', utils.EquipmentAutocomplete.as_view(), name='equipment-autocomplete'),
    path('search/', views.search_equipment, name='search_equipment'),
    path('search_journal/', views.search_journal, name='search_journal'),
    path('search_comment/', views.search_journal, name='search_comment'),
    path('post/<slug:post_slug>/', views.ShowDetailEquipment.as_view(), name='equipment'),
    path('post/journal_equipment/<slug:equipment_slug>/', views.JournalRecordsEquipment.as_view(), name='journal_equipment'),
    path('post/comment_equipment/<slug:comment_slug>/', views.CommentRecordsEquipment.as_view(), name='comment_equipment'),
    path('journal/', views.JournalListView.as_view(), name='journal'),
    path('comment/', views.CommentListView.as_view(), name='comment'),
    path('journal_record/', views.journal_record, name='journal_record'),
    path('comment_record/', views.comment_record, name='comment_record'),
]


