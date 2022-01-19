from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from .models import Card
from .serializers import CardSerializer


class CardView(APIView):
    def get(self, request):
        query = Card.objects.all()
        serializer = CardSerializer(query, many=True)
        return Response(serializer.data)

    def post(self, request):
        name = request.data['name']
        query = Card.objects.create(name=name)
        return Response(f"card created : {query.name}")

    def put(self, request, id):
        name = request.data['name']
        query = Card.objects.filter(id=id).update(name=name)

        return Response(f"card updated :{name}", status=status.HTTP_202_ACCEPTED)

    def delete(self, request, id):
        query = Card.objects.filter(id=id).delete()
        return Response(f"card deleted")
