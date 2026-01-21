from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from django.db.models import Count, Q
from .models import Advocate, Case
from .serializers import AdvocateSerializer, CaseSerializer, AdvocateSuccessRateSerializer

# ✅ List & Create Advocates
class AdvocateListCreate(generics.ListCreateAPIView):
    queryset = Advocate.objects.all()
    serializer_class = AdvocateSerializer

# ✅ Retrieve, Update & Delete Advocate
class AdvocateRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Advocate.objects.all()
    serializer_class = AdvocateSerializer

# ✅ List & Create Cases
class CaseListCreate(generics.ListCreateAPIView):
    queryset = Case.objects.all()
    serializer_class = CaseSerializer

# ✅ Retrieve, Update & Delete Case
class CaseRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Case.objects.all()
    serializer_class = CaseSerializer

# ✅ Success Rate API (No authentication for testing)
class AdvocateSuccessRateAPI(APIView):
    """
    Returns success rate for all advocates.
    """
    def get(self, request):
        advocates = Advocate.objects.annotate(
            total_closed_cases=Count('cases', filter=~Q(cases__status='ongoing')),
            won_cases=Count('cases', filter=Q(cases__status='won'))
        )

        data = []
        for adv in advocates:
            total_closed = adv.total_closed_cases
            won = adv.won_cases
            success_rate = (won / total_closed * 100) if total_closed > 0 else 0
            data.append({
                "advocate_id": adv.id,
                "advocate_name": adv.name,
                "total_closed_cases": total_closed,
                "won_cases": won,
                "success_rate": round(success_rate, 2)
            })

        serializer = AdvocateSuccessRateSerializer(data, many=True)
        return Response(serializer.data)

# ✅ Client Dashboard Success Rate API
class ClientDashboardSuccessRateAPI(APIView):
    """
    Returns success rate data formatted for client dashboard display
    """
    def get(self, request):
        # Get all advocates with their success rates
        advocates = Advocate.objects.annotate(
            total_cases=Count('cases'),
            total_closed_cases=Count('cases', filter=~Q(cases__status='ongoing')),
            won_cases=Count('cases', filter=Q(cases__status='won')),
            lost_cases=Count('cases', filter=Q(cases__status='lost')),
            ongoing_cases=Count('cases', filter=Q(cases__status='ongoing'))
        )

        dashboard_data = []
        for adv in advocates:
            total_closed = adv.total_closed_cases
            won = adv.won_cases
            lost = adv.lost_cases
            ongoing = adv.ongoing_cases
            
            # Calculate success rate only for closed cases
            success_rate = (won / total_closed * 100) if total_closed > 0 else 0
            
            dashboard_data.append({
                "advocate_id": adv.id,
                "advocate_name": adv.name,
                "advocate_email": adv.email,
                "specialization": adv.specialization,
                "phone": adv.phone,
                "success_rate": round(success_rate, 2),
                "total_cases": adv.total_cases,
                "closed_cases": total_closed,
                "won_cases": won,
                "lost_cases": lost,
                "ongoing_cases": ongoing,
                "performance_badge": self.get_performance_badge(success_rate),
                "status_breakdown": {
                    "won": won,
                    "lost": lost,
                    "ongoing": ongoing,
                    "win_percentage": round(success_rate, 1)
                }
            })

        # Sort by success rate (highest first)
        dashboard_data.sort(key=lambda x: x['success_rate'], reverse=True)
        
        return Response({
            "success": True,
            "message": "Dashboard data retrieved successfully",
            "data": dashboard_data,
            "summary": {
                "total_advocates": len(dashboard_data),
                "average_success_rate": round(sum(item['success_rate'] for item in dashboard_data) / len(dashboard_data), 2) if dashboard_data else 0,
                "top_performer": dashboard_data[0] if dashboard_data else None
            }
        })

    def get_performance_badge(self, success_rate):
        """Return performance badge based on success rate"""
        if success_rate >= 80:
            return {"text": "Excellent", "color": "#10b981", "icon": "🏆"}
        elif success_rate >= 60:
            return {"text": "Good", "color": "#3b82f6", "icon": "⭐"}
        elif success_rate >= 40:
            return {"text": "Average", "color": "#f59e0b", "icon": "📊"}
        else:
            return {"text": "Needs Improvement", "color": "#ef4444", "icon": "📈"}
