from django.conf.urls import url, include
from django.contrib import admin
from DjangoUeditor import urls as djud_urls
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'', include('blog.urls')),
    url(r'', include('comments.urls')),
    url(r'^ueditor/',include(djud_urls)),
    url(r'^search/', include('haystack.urls')),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
#仅解决测试环境中(debug=True),解决静态文件404，部署环境，nginx配置会自动访问

    