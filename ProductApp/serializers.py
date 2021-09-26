from rest_framework import serializers
from ProductApp.models import ModelStore


class StoreSerializers(serializers.ModelSerializer):
    class Meta:
        model = ModelStore
        fields = ['id','user','name','description','price','old_price','solde','category','h_img']