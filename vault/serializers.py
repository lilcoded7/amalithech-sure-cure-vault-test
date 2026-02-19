# serializers.py
from rest_framework import serializers
from vault.models.vaults import Node

class NodeSerializer(serializers.ModelSerializer):
    owner = serializers.HiddenField(default=serializers.CurrentUserDefault())
    type = serializers.CharField(source="node_type")
    content=serializers.CharField(required=False)
    ext = serializers.CharField(source="extension", read_only=True)
    size = serializers.SerializerMethodField()
    children = serializers.SerializerMethodField()
    
    parent = serializers.PrimaryKeyRelatedField(
        queryset=Node.objects.all(), 
        allow_null=True, 
        required=False
    )

    class Meta:
        model = Node
        fields = [
            "id","owner", "name", "type", "content", "ext", "size", 
            "children", "parent", "is_favorite", "is_trashed",
        ]
        read_only_fields = ["id", "ext", "size"]

    def to_internal_value(self, data):
        """
        Intercept the data BEFORE validation.
        If parent is "root" or 0, set it to None.
        """
        if "parent" in data and (data["parent"] == "root" or data["parent"] == "0" or data["parent"] == 0):
            # Create a mutable copy of the data if it's a QueryDict
            if hasattr(data, '_mutable'):
                data._mutable = True
            data["parent"] = None
            
        return super().to_internal_value(data)

    def get_size(self, obj):
        return f"{obj.size_bytes / 1024:.1f}" if obj.size_bytes else "0.0"

    def get_children(self, obj):
        if obj.node_type == "folder":
            # Avoid infinite recursion by checking context depth if needed, 
            # but for basic use, this is fine.
            children = obj.children.filter(is_trashed=False)
            return NodeSerializer(children, many=True).data
        return None