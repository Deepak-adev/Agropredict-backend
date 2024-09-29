from django.urls import path
from .views import generate_report,get_wordpress_posts,capture_image
from crop_app import views
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('generate_pdf/', views.generate_pdf, name='generate_pdf'),
    path('generate_report/', generate_report, name='generate_report'),
    path('home/', views.home, name='home'),
    path('wordpress-posts/', get_wordpress_posts, name='wordpress-posts'),
    path('capture_image/', capture_image, name='capture_image'),
]

from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from rest_framework.routers import DefaultRouter
from .views import MyModelViewSet

router = DefaultRouter()
router.register(r'ImageModel', MyModelViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('generate_pdf/', views.generate_pdf, name='generate_pdf'),
    path('generate_report/', generate_report, name='generate_report'),
    path('home/', views.home, name='home'),
    path('wordpress-posts/', get_wordpress_posts, name='wordpress-posts'),
    path('capture_image/', capture_image, name='capture_image'),
]


