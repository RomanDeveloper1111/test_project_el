from rest_framework import serializers
from back.models import Post
from back.scripts import image_size


class PostSerializer(serializers.ModelSerializer):

    class Meta:
        model = Post
        fields = '__all__'

    def validate(self, data):
        image_b = data['image_b']
        image_s = data['image_s']
        check_images = image_size(image_b, image_s)
        if check_images is None:
            raise serializers.ValidationError("Wrong photo size!")
        elif check_images['img_b'] == 'correct' and check_images['img_s'] == 'correct':
            return data


