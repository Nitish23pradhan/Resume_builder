from rest_framework import viewsets
from .models import Resume
from .serializers import ResumeSerializer
from django.utils.timezone import now
from datetime import timedelta
from rest_framework.response import Response
from rest_framework.decorators import action
from reportlab.pdfgen import canvas
from django.http import HttpResponse
from django.core.mail import EmailMessage
class ResumeViewSet(viewsets.ModelViewSet):
    queryset = Resume.objects.all()
    serializer_class = ResumeSerializer

    @action(detail=False, methods=['get'])
    def check_time(self, request):
        deploy_time = now() - timedelta(minutes=20)

        if now() > deploy_time:
            return Response({"msg": "Submission expired"})
        return Response({"msg": "Allowed"})
    def generate_pdf(request, pk):
          resume = Resume.objects.get(id=pk)

          response = HttpResponse(content_type='application/pdf')
          response['Content-Disposition'] = 'attachment; filename="resume.pdf"'

          p = canvas.Canvas(response)
          p.drawString(100, 800, resume.name)
          p.drawString(100, 780, resume.email)
          p.drawString(100, 760, resume.content)
          p.save()

          resume.downloads += 1
          resume.save()

          return response
    from django.core.mail import EmailMessage

    def send_resume_email(request, pk):
      resume = Resume.objects.get(id=pk)

      email = EmailMessage(
        'Resume',
        'Password: Name-DOB',
        to=[resume.email]
       )

      email.send()