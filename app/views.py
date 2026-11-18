from django.shortcuts import render
from .models import Book
from .serializer import BookSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.generics import GenericAPIView
from rest_framework import generics, mixins
from .paginator import BookPaginator
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
from app.mixins import ProMixinsGenricsAPI, ProMixinsDetailGenricsAPI
from rest_framework.viewsets import ViewSet, ModelViewSet
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from app.permissions import ReadAndAdminUpdate

class BookViewSets(ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [ReadAndAdminUpdate]

    @action(detail=True, methods=["get"])
    def info(self, request, pk):
        book = self.get_object()
        return Response({
            'name': book.title,
            'about': book.description,
            'author': book.author
        })

    @action(detail=False, methods=['get'])
    def expensive(self, request):
        book = Book.objects.order_by('-price').first()
        serializer = self.get_serializer(book)
        return Response(serializer.data)

    @action(detail=False, methods=['get'])
    def chip(self, request):
        book = Book.objects.order_by('price').first()
        serializer = self.get_serializer(book)
        return Response(serializer.data)


    @action(detail=True, methods=['post'])
    def change_rating(self, request, pk=None):
        book = self.get_object()

        book.rating = request.data.get('rating')
        book.save()

        return Response({
            'rating': book.rating
        })
    


# class BookViewSets(ViewSet):

#     def list(self, request):
#         book = Book.objects.all()
#         serializer = BookSerializer(book, many=True)

#         return Response(serializer.data)

#     def create(self, request):
#         serializer = BookSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()

#         return Response(serializer.data)

#     def retrieve(self, request, pk):
#         book = Book.objects.get(pk=pk)
#         serializer = BookSerializer(book)

#         return Response(serializer.data)

#     def update(self, request, pk):
#         book = Book.objects.get(pk=pk)
#         serializer = BookSerializer(book, data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()

#         return Response(serializer.data)

#     def partial_update(self, request, pk):
#         book = Book.objects.get(pk=pk)
#         serializer = BookSerializer(book, data=request.data, partial=True)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()

#         return Response(serializer.data)

#     def destroy(self, request, pk):
#         book = Book.objects.get(pk=pk)
#         book.delete()

#         return Response({'message': 'Your product was deleted'})


# class BookCreateAPI(ProMixinsGenricsAPI):
#     queryset = Book.objects.all()
#     serializer_class = BookSerializer

#     def get(self, request, *args, **kwargs):
#         return self.list(request, *args, **kwargs)

#     def post(self, request, *args, **kwargs):
#         return self.create(request, *args, **kwargs)

# class BookDetailGenericsAPIView(ProMixinsDetailGenricsAPI):
#     queryset = Book.objects.all()
#     serializer_class = BookSerializer
#     lookup_field = 'id'

#     def get(self, request, *args, **kwargs):
#         return self.retrieve(request, *args, **kwargs)

#     def put(self, request, *args, **kwargs):
#         return self.update(request, *args, **kwargs)

#     def patch(self, request, *args, **kwargs):
#         return self.partial_update(request, *args, **kwargs)

#     def delete(self, request, *args, **kwargs):
#         return self.destroy(request, *args, **kwargs)
    
        


# class BookCreateAPI(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Book.objects.all()
#     serializer_class = BookSerializer
#     lookup_field = 'id'

#     pagination_class = BookPaginator
#     filter_backends = [
#         DjangoFilterBackend,
#         SearchFilter,
#         OrderingFilter
#     ]

#     filterset_fields = ['category', 'rating']
#     search_fields = ['title', 'description', 'author']
#     ordering_fields = ['price', 'rating', 'title']
#     ordering = ['title']
    


# class BookGenericsAPIView(GenericAPIView):
#     queryset = Book.objects.all()
#     serializer_class = BookSerializer
#     pagination_class = BookPaginator
#     filter_backends = [
#         DjangoFilterBackend,
#         SearchFilter,
#         OrderingFilter
#     ]

#     filterset_fields = ['category', 'rating']
#     search_fields = ['title', 'description', 'author']
#     ordering_fields = ['price', 'rating', 'title']
#     ordering = ['title']

#     def get(self, request):
#         products = self.filter_queryset(self.get_queryset())
#         page = self.paginate_queryset(products)
#         serializer = self.get_serializer(page, many=True)
        
#         return self.get_paginated_response(serializer.data)

#     def post(self, request):
#         serializer = self.get_serializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.data, status=status.HTTP_201_CREATED)


# class BookDetailGenericsAPIView(GenericAPIView):
#     queryset = Book.objects.all()
#     serializer_class = BookSerializer
#     lookup_field = 'id'

#     def get(self, request, id):
#         product = self.get_object()
#         serializer = self.get_serializer(product)
#         return Response(serializer.data, status=status.HTTP_200_OK)

#     def put(self, request, id):
#         product = self.get_object()
#         serializer = self.get_serializer(product, data=request.data)

#         if serializer.is_valid():
#             serializer.save()

#             return Response(serializer.data, status=status.HTTP_201_CREATED)
            
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     def patch(self, request, id):
#         product = self.get_object()
#         serializer = self.get_serializer(product, data=request.data, partial=True)

#         if serializer.is_valid():
#             serializer.save()

#             return Response(serializer.data, status=status.HTTP_201_CREATED)
            
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     def delete(self, request, id):
#         product = self.get_object()
#         product.delete()

#         return Response({'message': 'Успешно удалено'}, status=status.HTTP_200_OK)




# class BookAPIView(APIView):
#     def get(self, request):
        # products = Book.objects.all()
        # serializer = BookSerializer(products, many=True)
        
        # return Response(serializer.data, status=status.HTTP_200_OK)

    # def post(self, request):
    #     serializer = BookSerializer(data=request.data)
    #     serializer.is_valid(raise_exception=True)
    #     serializer.save()
    #     return Response(serializer.data, status=status.HTTP_201_CREATED)


# class BookDetailAPIView(APIView):
    # def get(self, request, id):
    #     product = Book.objects.get(id=id)
    #     serializer = BookSerializer(product)
    #     return Response(serializer.data, status=status.HTTP_200_OK)

    # def put(self, request, id):
    #     product = Book.objects.get(id=id)
    #     serializer = BookSerializer(product, data=request.data)

    #     if serializer.is_valid():
    #         serializer.save()

    #         return Response(serializer.data, status=status.HTTP_201_CREATED)
            
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # def patch(self, request, id):
    #     product = Book.objects.get(id=id)
    #     serializer = BookSerializer(product, data=request.data, partial=True)

    #     if serializer.is_valid():
    #         serializer.save()

    #         return Response(serializer.data, status=status.HTTP_201_CREATED)
            
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # def delete(self, request, id):
    #     product = Book.objects.get(id=id)
    #     product.delete()

    #     return Response({'message': 'Успешно удалено'}, status=status.HTTP_200_OK)







# @api_view(['GET', 'POST'])
# def product_list(request):
#     if request.method == 'GET':
        # products = Book.objects.all()
        # serializer = BookSerializer(products, many=True)

        # return Response(serializer.data, status=status.HTTP_200_OK)

#     elif request.method == 'POST':
        # serializer = BookSerializer(data=request.data)
        # serializer.is_valid(raise_exception=True)
        # serializer.save()
        # return Response(serializer.data, status=status.HTTP_201_CREATED)



# @api_view(['GET', 'PUT', 'PATCH', 'DELETE'])
# def detail_product(request, id):
#     product = Book.objects.get(id=id)

#     if request.method == 'GET':
        # serializer = BookSerializer(product)
        # return Response(serializer.data, status=status.HTTP_200_OK)

#     elif request.method == 'PUT':
        # serializer = BookSerializer(product, data=request.data)

        # if serializer.is_valid():
        #     serializer.save()

        #     return Response(serializer.data, status=status.HTTP_201_CREATED)
            
        # return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     elif request.method == 'PATCH':
#             serializer = BookSerializer(product, data=request.data, partial=True)
    
#             if serializer.is_valid():
#                 serializer.save()
    
#                 return Response(serializer.data, status=status.HTTP_201_CREATED)
                
#             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     elif request.method == 'DELETE':
        # product.delete()

        # return Response({'message': 'Успешно удалено'}, status=status.HTTP_200_OK)



