from django.core.exceptions import EmptyResultSet, ObjectDoesNotExist
from django.db import IntegrityError
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Card
from .serializers import CardSerializer


class CardView(APIView):
    def get(self, request):
        try:
            query = Card.objects.all()
            serializer = CardSerializer(query, many=True)
            return Response(serializer.data)
        except EmptyResultSet:
            return Response("The card is empty")

    def post(self, request):
        try:
            name = request.data['name']
            query = Card.objects.create(name=name)
            return Response(f"card created : {query.name}")
        except IntegrityError:
            return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def put(self, request, id):
        try:
            name = request.data['name']
            query = Card.objects.filter(id=id).update(name=name)

            return Response(f"card updated :{name}", status=status.HTTP_202_ACCEPTED)
        except ObjectDoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, id):
        try:
            Card.objects.filter(id=id).delete()
            return Response(f"card deleted")
        except ObjectDoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
