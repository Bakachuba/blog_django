from rest_framework import serializers

from app.models import Post, Creator, Comment, Category, PostViewCount


class CreatorSerializer(serializers.ModelSerializer):
    post_count = serializers.SerializerMethodField()
    username = serializers.CharField(source='user.username', read_only=True)

    class Meta:
        model = Creator
        fields = ['id', 'username', 'created_at', 'post_count']

    def get_post_count(self, obj):
        return obj.posts.count()


class CommentSerializer(serializers.ModelSerializer):
    creator_name = serializers.CharField(source='creator.user.username', read_only=True)

    class Meta:
        model = Comment
        fields = ['id', 'text', 'created_at', 'creator_name']


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name']


class PostSerializer(serializers.ModelSerializer):
    creator_name = serializers.CharField(source='creator.user.username', read_only=True)
    comments = CommentSerializer(many=True, read_only=True)
    categories = CategorySerializer(many=True)
    category_ids = serializers.PrimaryKeyRelatedField(
        queryset=Category.objects.all(), many=True, write_only=True
    )

    class Meta:
        model = Post
        fields = ['id', 'title', 'category_ids', 'content', 'creator_name', 'comments', 'categories', 'created_at']

    def create(self, validated_data):
        category_ids = validated_data.pop('category_ids', [])
        post = Post.objects.create(**validated_data)
        post.categories.set(category_ids)
        return post

    def update(self, instance, validated_data):
        category_ids = validated_data.pop('category_ids', None)
        instance = super().update(instance, validated_data)
        if category_ids is not None:
            instance.categories.set(category_ids)
        return instance


class PostViewCountSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostViewCount
        fields = ['id', 'posts', 'visitor', 'viewed_at']
