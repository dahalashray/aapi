from django.urls import path
from rest_framework_simplejwt import views as jwt_views
from .views import UserCreateView,UserDetailView,UserListView

urlpatterns = [
    path('api/token/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
    path('list/', UserListView.as_view(), name = 'userlist'),
    path('create/', UserCreateView.as_view(), name = 'usercreate'),
    path('update/<int:pk>/', UserDetailView.as_view(), name = 'userupdate'),
]

