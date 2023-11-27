from rest_framework import generics
from rest_framework.response import Response
from rest_framework_simplejwt.authentication import JWTAuthentication 
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework import status

from .models import Vendor, PurchaseOrder
from .serializers import VendorSerializer, PurchaseOrderSerializer


class CustomTokenRefreshView(APIView):
    def post(self, request):
        print('custom token')
        refresh_token = request.data.get("refresh")
        print(refresh_token)
        try:
            refresh = RefreshToken(refresh_token)
            user_id = refresh['vendor_code']
            print(user_id)
        except Exception as e:
            return Response({'detail': str(e)}, status=status.HTTP_400_BAD_REQUEST)

        # Customize the payload of the access token
        vendor = Vendor.objects.get(id=user_id)
       
        token_payload = {
                'user_id': vendor.id,
                'name': vendor.name,
                'vendor_code': vendor.vendor_code,
            }
        print(token_payload)
        access_token = refresh.access_token
        access_token.payload.update(token_payload)

        return Response({'refresh': str(refresh), 'access': str(access_token)},
                status=status.HTTP_200_OK
            )

class VendorListView(generics.ListCreateAPIView):
    authentication_classes=[JWTAuthentication]

    queryset = Vendor.objects.all()
    serializer_class = VendorSerializer

class VendorDetailView(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes=[JWTAuthentication]

    queryset = Vendor.objects.all()
    serializer_class = VendorSerializer

class PurchaseOrderListView(generics.ListCreateAPIView):
    authentication_classes=[JWTAuthentication]

    queryset = PurchaseOrder.objects.all()
    serializer_class = PurchaseOrderSerializer

class PurchaseOrderDetailView(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes=[JWTAuthentication]

    queryset = PurchaseOrder.objects.all()
    serializer_class = PurchaseOrderSerializer

class VendorPerformanceView(generics.RetrieveAPIView):
    authentication_classes=[JWTAuthentication]

    queryset = Vendor.objects.all()
    serializer_class = VendorSerializer

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)
