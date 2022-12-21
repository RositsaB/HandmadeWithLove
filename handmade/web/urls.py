from django.urls import path

from handmade.web.views import index, ProjectsView, ProjectDetailsView, ProjectAddView, ProjectEditView, \
    ProjectDeleteView, CommentAddView, CommentEditView, CommentDeleteView, FavouritesView, FavouritesAddView, \
    FavouritesRemoveView, HandmadeNewsView, HandmadeNewsAddView

urlpatterns = (
    path('', index, name='index'),

    path('projects/', ProjectsView.as_view(), name='projects'),
    path('details/<int:pk>', ProjectDetailsView.as_view(), name='project details'),
    path('add/', ProjectAddView.as_view(), name='project add'),
    path('edit/<int:pk>', ProjectEditView.as_view(), name='project edit'),
    path('delete/<int:pk>', ProjectDeleteView.as_view(), name='project delete'),

    path('<int:pk>/comment/', CommentAddView.as_view(), name='comment'),
    path('<int:pk>/comment/edit', CommentEditView.as_view(), name='comment edit'),
    path('<int:pk>/comment/delete', CommentDeleteView.as_view(), name='comment delete'),

    path('favourites/', FavouritesView.as_view(), name='favourites'),
    path('project/favourite/<int:pk>', FavouritesAddView.as_view(), name='favourites add'),
    path('project/favourite/remove/<int:pk>', FavouritesRemoveView.as_view(), name='favourites remove'),

    path('news/', HandmadeNewsView.as_view(), name='news'),
    path('news/add/', HandmadeNewsAddView.as_view(), name='news add'),
)
