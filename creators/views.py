from django.shortcuts import render
from django.views.generic import TemplateView
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from rest_framework import viewsets, permissions, filters
from rest_framework.viewsets import ModelViewSet

from creators.models import Content, Creator
from creators.serializers import ContentSerializer, CreatorSerializer, UserSerializer

from django.contrib.auth.models import User


class HomePageView(TemplateView):
    template_name = 'core/base.html'


def content_list(request):
    object_list = Content.objects.all()

    paginator = Paginator(object_list, 30)  # 30 items in each page
    page = request.GET.get('page')

    try:
        creators = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer deliver the first page
        creators = paginator.page(1)
    except EmptyPage:
        # If page is out of range deliver last page of results
        creators = paginator.page(paginator.num_pages)

    return render(request, 'creators/list.html', {'page': page, 'creators': creators})


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.exclude(pk=1)
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    filter_backends = [filters.SearchFilter]
    search_fields = ['creator__platform']
