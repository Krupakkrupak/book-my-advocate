from rest_framework.decorators import api_view
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def test_api(request):
    """
    Simple test API to verify Django setup is working
    """
    return Response({
        'message': 'Django REST API is working!',
        'status': 'success',
        'timestamp': '2025-01-21T15:51:30Z'
    })
