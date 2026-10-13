from rest_framework import serializers
from watchlist.models import Review, WatchList,StreamPlatform,Review

class ReviewSerializer(serializers.ModelSerializer):
    review_user=serializers.StringRelatedField(read_only=True)
    watchlist=serializers.PrimaryKeyRelatedField(read_only=True)
    class Meta:
        model=Review
        fields='__all__'


class WatchListSerializer(serializers.ModelSerializer):
    # len_name= serializers.SerializerMethodField()
    reviews=ReviewSerializer(many=True, read_only=True)
    class Meta:
        model = WatchList
        fields= '__all__'
    

class StreamPlatformSerializer(serializers.ModelSerializer):
    # len_name= serializers.SerializerMethodField()
    watchlist=WatchListSerializer(many=True, read_only=True)
    # watchlist=serializers.StringRelatedField(many=True, read_only=True)
    class Meta:
        model = StreamPlatform
        fields= '__all__'   
        
        
        
        
        
        
        # fields = ['id', 'name', 'description', ]
        # exclude=['active','name']
    # def get_len_name(self, obj):
    #     return len(obj.name)

   
    # def validate_name(self, value):
    #     """
    #     Check that the blog post is about Django.
    #     """
    #     if len(value) < 2:
    #         raise serializers.ValidationError("Name length should be more then 2 characters")
    #     else:
    #        return value
       
    # def validate(self, data):
    #     """
    #     Check that start is before finish.
    #     """
    #     if data['name'] == data['description']:
    #         raise serializers.ValidationError("Name and description should not be same")
    #     else:
    #         return data

# def name_length(value):
#     if len(value) < 2:
#         raise serializers.ValidationError("Name length should be more then 2 characters")
#     else:
#         return value
  
# class MovieSerializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only=True)
#     name = serializers.CharField(max_length=255,validators=[name_length])
#     description = serializers.CharField(max_length=255)
#     active = serializers.BooleanField(default=True)
    
    # def create(self, validated_data):
    #     """
    #     Create and return a new `Movie` instance, given the validated data.
    #     """
    #     return Movie.objects.create(**validated_data)
        
    # def update(self, instance, validated_data):
    #     """
    #     Update and return an existing `Movie` instance, given the validated data.
    #     """
    #     instance.name = validated_data.get('name', instance.name)
    #     instance.description = validated_data.get('description', instance.description)
    #     instance.active = validated_data.get('active', instance.active)
    #     instance.save()
    #     return instance
    
    
    
 
   
       
   
    
    