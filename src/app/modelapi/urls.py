from rest_framework_nested import routers
from django.urls import (
    include,
    path,
)
from .views import (
    SchoolViewSet,
    StudentViewSet,
)

router = routers.SimpleRouter()
router.register(r'schools', SchoolViewSet)

student_router = routers.SimpleRouter()  # to satisfies condition in step 2
student_router.register(r'students', StudentViewSet)

school_router = routers.NestedSimpleRouter(router, r'schools', lookup='schools')
school_router.register(r'students', StudentViewSet, basename='schools-students')
# 'basename' is optional. Needed only if the same viewset is registered more than once
# Official DRF docs on this option: http://www.django-rest-framework.org/api-guide/routers/

urlpatterns = [
    path(r'', include(student_router.urls)),  # to satisfies condition in step 2
    path(r'', include(router.urls)),
    path(r'', include(school_router.urls)),
]
