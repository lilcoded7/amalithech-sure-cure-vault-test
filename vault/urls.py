from django.urls import path
from .views import NodeListCreateView, NodeDetailView

urlpatterns = [
    path("nodes/", NodeListCreateView.as_view(), name="node_list_create"),
    path("nodes/<int:id>/", NodeDetailView.as_view(), name="node_detail"),
]
