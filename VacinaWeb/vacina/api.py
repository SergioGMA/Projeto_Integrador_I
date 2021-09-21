from django.http import HttpResponse

from .models import Vacina
from .serializers import VacinaSerializer

from rest_framework import viewsets, mixins
from rest_framework.authentication import SessionAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

import json

class VacinaViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    authentication_classes = [SessionAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Vacina.objects.none()
    serializer_class = VacinaSerializer

    def get_queryset(self,):
        queryset = Vacina.objects.all()
        return queryset


    def post(self, request, *args, **kwargs):
        try:
            print(request.body)
            if len(request.body) > 0:
                data = json.loads(request.body)
                d = Vacina(name=data['name'], desc=data['desc'], qtd_dose=data['qtd_dose'], lote=data['lote'])
                d.save()
                return Response({'status': True, 'msg':'ok'})
            else:
                return Response({'status': False, 'msg':'data invalid'})

        except Exception as error:
            return HttpResponse(error)


