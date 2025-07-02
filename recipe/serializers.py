from rest_framework.serializers import ModelSerializer
from .models import Recipe

class RecipeSerializer(ModelSerializer):
    
    class Meta:
        model = Recipe
        fields = ['title', 'description', 'time_minutes', 'price', 'link']
        read_only_fields = ['id']
    
    def create(self, validated_data):
        request = self.context.get('request')
        return Recipe.objects.create(user=request.user, **validated_data)

class RecipeDetailSerializer(RecipeSerializer):
    """Serializer for recipe datail view"""

    class Meta(RecipeSerializer.Meta):
        fields = RecipeSerializer.Meta.fields + ['description']