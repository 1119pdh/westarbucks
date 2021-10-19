from django.urls import path
from django.views.generic.base import View

#from Wewecode.Wecode.westarbucks1016.Westar1.owner.models import Owner
#위에코드는 자동으로 생김 모듈에러나면 체크!

from .views import OwnerListView, DogListView


#urlpatterns = [
#    path("",OwnerListView.as_view())
#]

urlpatterns = [
    path("owner", OwnerListView.as_view()),
    path("dog", DogListView.as_view())
]