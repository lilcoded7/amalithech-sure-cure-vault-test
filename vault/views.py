from rest_framework import generics, mixins, permissions
from vault.models.vaults import Node
from .serializers import NodeSerializer


class NodeListCreateView(generics.ListCreateAPIView):
    serializer_class = NodeSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        queryset = Node.objects.filter(is_trashed=False, owner=self.request.user)
        parent_id = self.request.query_params.get("parent")

        if parent_id:
            return queryset.filter(parent_id=parent_id)
        return queryset.filter(parent__isnull=True)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class NodeDetailView(
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    generics.GenericAPIView,
):
    """
    Handles retrieving, updating (rename/move), and deleting a specific node.
    """

    serializer_class = NodeSerializer
    permission_classes = [permissions.IsAuthenticated]
    lookup_field = "id"

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        # You might want to implement "Soft Delete" here instead of hard delete
        return self.destroy(request, *args, **kwargs)

    def get_queryset(self):
        return Node.objects.filter(is_trashed=False, owner=self.request.user)
