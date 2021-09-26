from rest_framework.views import APIView
from ProductApp.models import ModelStore
from ProductApp.serializers import StoreSerializers
from rest_framework.response import Response

class StoreList(APIView):
    def get(self,request,format=None):
        storedata = ModelStore.objects.all()
        serializer = StoreSerializers(storedata,many=True)
        return Response(serializer.data)