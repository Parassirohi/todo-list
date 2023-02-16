from rest_framework.routers import SimpleRouter
from . import views

router = SimpleRouter()
router.register('todos', views.TodoViewSet)

urlpatterns = router.urls
