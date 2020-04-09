from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('my-books/', views.LoanedBooksByUserListView.as_view(), name='my-borrowed'),
    path('all-borrowed-books/', views.AllLoanedBooksByUserListView.as_view(), name='all-borrowed'),
    path('book/<uuid:pk>/renew/', views.renew_book_librarian, name='renew-book-librarian'),
]

urlpatterns +=[
    path('books/', views.BookListView.as_view(), name='books'),
    path('create-books/', views.BookCreateView.as_view(), name='create-book'),
    path('book/<int:pk>', views.BookDetailView.as_view(), name='book-detail'),

    path('create-books-instance/', views.BookInstanceCreateView.as_view(), name='create-book-instance'),

]

urlpatterns += [
    path('authors/', views.AuthorListView.as_view(), name='authors-list'),
    path('author/<int:pk>', views.AuthorDetailView.as_view(), name='author-detail'),
    path('create-authors/', views.AuthorCreateView.as_view(), name='create-author'),
    path('author/<int:pk>/edit/', views.AuthorUpdate.as_view(), name='edit-author'),
]

urlpatterns += [
    path('create-library-user', views.LibraryUserCreateView.as_view(), name='create-library-user'),
    path('library-user-list', views.UserListView.as_view(), name='library-user-list'),
    path('library-user-list/<int:pk>', views.UserDetailView.as_view(), name='library-user-detail'),
]
