from django.urls import path
# from watchlist.api.views import movie_list, movie_detail
from watchlist.api.views import ReviewList, ReviewCreate, ReviewDetail, WatchListAV,WatchListDetailAV,StreamPlatformDetailAV,StreamPlatformAV
urlpatterns = [
    path('list/',WatchListAV.as_view(), name='movie'),
    path('<int:pk>/',WatchListDetailAV.as_view(),name='movie-detail'),
    path('stream/',StreamPlatformAV.as_view(), name='stream'),
    path('stream/<int:pk>/',StreamPlatformDetailAV.as_view(),name='stream-detail'),
    # path('review/',ReviewList.as_view(), name='review-list'),
    # path('review/<int:pk>/',ReviewDetail.as_view(), name='review-detail'),
    path('<int:pk>/review-create/',ReviewCreate.as_view(), name='review-create'),
    path('<int:pk>/review/',ReviewList.as_view(), name='review-list'),
    
    path('review/<int:pk>/',ReviewDetail.as_view(), name='review-detail')
]
