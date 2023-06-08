from post.models import Post
from django.http import Http404
from post.api.serializers import *
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.pagination import LimitOffsetPagination

"""Retrieve list of posts instance in pagination."""
class PostPaginationList(APIView):
    pagination_class = LimitOffsetPagination
    def get(self, request, limit, offset):
        # update GET value 
        request.GET._mutable = True
        request.GET['limit'] = limit
        request.GET['offset'] = offset
        request.GET._mutable = False


        queryset = Post.objects.all().order_by('-created_date')
        paginator = self.pagination_class()
        paginated_queryset = paginator.paginate_queryset(queryset, request)
        serializer = PostSerializer(paginated_queryset, many=True)
        # return paginator.get_paginated_response(serializer.data)
        return Response(data={'data': serializer.data}, status=status.HTTP_200_OK)
    
"""Retrieve list of posts instance in pagination."""
class PostPaginationListStatus(APIView):
    pagination_class = LimitOffsetPagination
    def get(self, request, limit, offset, flag):
        # update GET value 
        request.GET._mutable = True
        request.GET['limit'] = limit
        request.GET['offset'] = offset
        request.GET._mutable = False

        queryset = Post.objects.filter(status=flag.capitalize()).order_by('-created_date')
        paginator = self.pagination_class()
        paginated_queryset = paginator.paginate_queryset(queryset, request)
        serializer = PostSerializer(paginated_queryset, many=True)
        # return paginator.get_paginated_response(serializer.data)
        return Response(data={'data': serializer.data}, status=status.HTTP_200_OK)
    
"""Create a post instance."""
class PostAdd(APIView):
    def post(self, request):
        serializer = PostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data={'detail': 'Data successfully added', 'a': serializer.data}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=400)

"""Retrieve, update or delete a post instance."""
class PostDetail(APIView):
    """get related post"""
    def get_object(self, id):
        try:
            return Post.objects.get(id=id)
        except Post.DoesNotExist:
            raise Http404
    
    """Retrieve"""
    def get(self, request, id, format=None):
        post = self.get_object(id)
        serializer = PostSerializer(post)
        return Response(data={'data': serializer.data}, status=status.HTTP_200_OK)

    """Update"""
    def put(self, request, id, format=None):
        print(request.data)
        post = self.get_object(id)
        serializer = PostUpdateSerializer(post, data=request.data)
        print(serializer)
        print(serializer.is_valid())
        if serializer.is_valid():
            serializer.save()
            return Response(data={'detail': 'Data successfully updated', 'data': serializer.data}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    """Delete"""
    def delete(self, request, id, format=None):
        post = self.get_object(id)
        post.delete()
        return Response(status=status.HTTP_204_NO_CONTENT, data={'detail': 'Data successfully deleted'})
