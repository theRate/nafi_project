from rest_framework import generics
from .models import Question
from .serializers import QuestionSerializer


class QuestionAPIView(generics.ListCreateAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
