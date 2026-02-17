import os
from django.db import models
from django.core.validators import FileExtensionValidator
from django.contrib.auth import get_user_model

User = get_user_model()


class Node(models.Model):
    NODE_TYPES = (
        ('folder', 'Folder'),
        ('file', 'File'),
    )

    owner = models.ForeignKey(
        User, 
        on_delete=models.CASCADE, 
        related_name="nodes"
    )
    parent = models.ForeignKey(
        'self', 
        on_delete=models.CASCADE, 
        null=True, 
        blank=True, 
        related_name='children'
    )

    name = models.CharField(max_length=255)
    node_type = models.CharField(max_length=10, choices=NODE_TYPES, default='file')
    

    file_obj = models.FileField(
        upload_to='vault/%Y/%m/%d/', 
        null=True, 
        blank=True
    )
    
    extension = models.CharField(max_length=10, editable=False, null=True, blank=True)
    size_bytes = models.BigIntegerField(default=0, editable=False) 
    
    is_favorite = models.BooleanField(default=False)
    is_trashed = models.BooleanField(default=False)
    last_accessed_at = models.DateTimeField(auto_now_add=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-node_type', 'name']
        unique_together = ('name', 'parent', 'owner')

        indexes = [
            models.Index(fields=['owner', 'parent']),
            models.Index(fields=['is_trashed']),
        ]

    def save(self, *args, **kwargs):
        if self.file_obj and self.node_type == 'file':
            self.size_bytes = self.file_obj.size
            self.extension = os.path.splitext(self.file_obj.name)[1].lower().replace('.', '')
        super().save(*args, **kwargs)

    @property
    def size_display(self):
        """Converts bytes to readable KB/MB for the Next.js frontend"""
        return f"{self.size_bytes / 1024:.1f}"