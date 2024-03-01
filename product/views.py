from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import status

from product.models import Product

from product.serializer.output import ProductOutSerializer
from product.serializer.input import ProductInSerializer
from product.pagination import BasicPagination, PaginationHandlerMixin

# Create your views here.
class ProductViewSet(ViewSet, PaginationHandlerMixin):
    pagination_class = BasicPagination
    serializer_class= ProductOutSerializer
    serializer_in_class= ProductInSerializer
    
    def get_object(self, pk):
        try:
            product = Product.objects.get(pk=pk)
            return product
        except Product.DoesNotExist:
            data = {
                "status": False,
                "message": "Ce produit n'existe pas."
            }
            return Response(data, status=status.HTTP_404_NOT_FOUND)
    
    def list(self, request):
        products = Product.objects.all().order_by('libelle')

        page = self.paginate_queryset(products)
        if page is not None:
            serializer = self.get_paginated_response(self.serializer_class(page, many=True).data)
        else:
            serializer = self.serializer_class(products, many=True)
        return Response({
            "status": True,
            "message": "Voici la liste de vos produits",
            "detail": serializer.data }, status=status.HTTP_200_OK)
    
    def retrieve(self, request, pk=None):
        instance = self.get_object(pk=pk)
        if type(instance) is Response : return instance
        
        return Response({
            "status": True,
            "message": "Voici les informations sur votre produit",
            "detail": self.serializer_class(instance).data }, status=status.HTTP_200_OK)
    
    def create(self, request):
        booking_in = self.serializer_in_class(data=request.data)
        
        if booking_in.is_valid():
            booking = booking_in.save()
                
            return Response({
                "status": True,
                "message": "Votre produits a bien été enregistr2",
                "detail": self.serializer_class(booking).data }, status=status.HTTP_200_OK)
        return Response({
            "status": False,
            "message": "Données entrées invalides",
            "detail": booking_in.errors }, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, pk=None):
        instance = self.get_object(pk=pk)
        if type(instance) is Response : return instance
        
        serializer = self.serializer_class(instance, data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response({
                "status": True,
                "message": "Votre produit a été mises à jour.",
                "detail": serializer.data
            }, status=status.HTTP_200_OK)
        return Response({
            "status": False,
            "message": "Données entrées invalides" }, status=status.HTTP_400_BAD_REQUEST)
    
    def destroy(self, request, pk=None):
        instance = self.get_object(pk=pk)
        if type(instance) is Response : return instance
        
        instance.delete()
        return Response({
            "status": True,
            "message": "Votre produit a été supprimée" }, status=status.HTTP_200_OK)