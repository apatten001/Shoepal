from django.shortcuts import render
from django.views.generic import TemplateView,DetailView, ListView, CreateView
from django.shortcuts import get_object_or_404,Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Shoe
from .serializers import ShoeSerializer
from .forms import CreateShoeForm
from django.urls import reverse


# Create your views here.


class ShoeListView(ListView):

    model = Shoe

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class ShoeCreateView(CreateView):

    form_class = CreateShoeForm
    template_name = 'sell/shoe_create.html'


class HomeView(DetailView):

    model = Shoe

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['latest_shoes'] = Shoe.objects.all()[:5]
        return context


#List all stocks or create a new one
# url shoes/
class ShoeList(APIView):

    def get(self,request):
        shoes = Shoe.objects.all()
        serializer = ShoeSerializer(shoes, many=True)
        return Response(serializer.data)

    def post(self,request):
        serializer = ShoeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ShoeDetail(APIView):

    def get_object(self, pk):
        try:
            return Shoe.objects.get(pk=pk)
        except Shoe.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        snippet = self.get_object(pk)
        serializer = ShoeSerializer(snippet)
        return Response(serializer.data)

    def put(self, request, pk):
        snippet = self.get_object(pk)
        serializer = ShoeSerializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        snippet = self.get_object(pk)
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class WelcomeTemplateView(TemplateView):
    template_name = "base.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
