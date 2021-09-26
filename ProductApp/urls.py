from django.urls import path
from ProductApp.apis import StoreList

app_name='ProductApp'
urlpatterns = [
    path('api/list',StoreList.as_view(), name='list')
]
