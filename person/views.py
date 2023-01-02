from .models import Person
from person.serializers import PersonSerializer
from rest_framework.response import Response
from rest_framework.views import APIView
from reportlab.pdfgen import canvas
from django.http import HttpResponse
class PersonsIdentity(APIView):
    def get(self, request):
        persons = Person.objects.all()
        serializer = PersonSerializer(persons, many = True)
        return Response(serializer.data)

class getpdf(APIView):
    def get(self, request):
        persons = Person.objects.all()
        serializer = PersonSerializer(persons, many = True)
        response = HttpResponse(content_type='application/pdf')
        response['Content-Disposition'] = 'attachment; filename = "file.pdf"'
        p = canvas.Canvas(response)
        p.drawString(100,700, serializer)
        p.showPage()
        p.save()
        return response

