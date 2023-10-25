from rest_framework import serializers
from apptest.models import Brand


class BrandSerializers(serializers.ModelSerializer):

    class Meta:
        model = Brand
        fields = "__all__"