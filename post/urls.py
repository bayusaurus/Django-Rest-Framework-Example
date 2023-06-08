from django.urls import path
from post.api.views import *
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from django.conf.urls import url
from rest_framework import permissions

schema_view = get_schema_view(
    openapi.Info(
        title="Test API",
        default_version='v1',
        description="Test description",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="testing@api.com"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)

app_name = 'post'
urlpatterns = [
    #swaggerapi documentation
    url('playground/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    url('docs/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    
    # Article
    path('article/', PostAdd.as_view(), name = 'article_create'),
    path('article/<int:id>/', PostDetail.as_view(), name = 'article_detail'),
    path('article/<int:limit>/<int:offset>/', PostPaginationList.as_view(), name = 'article_list'),
    path('article/<int:limit>/<int:offset>/<str:flag>/', PostPaginationListStatus.as_view(), name = 'article_list'),
]