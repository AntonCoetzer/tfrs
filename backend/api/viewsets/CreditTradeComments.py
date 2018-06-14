from rest_framework import viewsets, permissions, status, mixins, exceptions
from rest_framework.decorators import list_route, detail_route
from rest_framework.response import Response
from rest_framework import filters

from api.permissions.CreditTradeComment import CreditTradeCommentPermissions

from auditable.views import AuditableMixin
from django.db.models import Q
import datetime

from api.models.CreditTradeComment import CreditTradeComment
from api.serializers import CreditTradeCommentSerializer


class CreditTradeCommentsViewSet(AuditableMixin, mixins.RetrieveModelMixin, mixins.CreateModelMixin,
                                 mixins.UpdateModelMixin, viewsets.GenericViewSet):

    permission_classes = (CreditTradeCommentPermissions,)
    http_method_names = ['get', 'put', 'post']
    queryset = CreditTradeComment.objects.all()
    filter_backends = (filters.OrderingFilter,)
    ordering_fields = '__all__'
    ordering = ('create_timestamp',)
    serializer_class = CreditTradeCommentSerializer
