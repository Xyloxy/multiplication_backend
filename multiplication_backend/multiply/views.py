from rest_framework.views import APIView
from rest_framework.response import Response

# Create your views here.
class MultiplyView(APIView):
    def post(self, request):
        # Validate data
        data = request.data
        number1 = data.get("number1", None)
        number2 = data.get("number2", None)
        
        if number1 is None or number2 is None:
            return Response({"error": "number1 and number2 are required"}, status=400)
        
        # Parse data
        try:
            number1 = float(number1)
            number2 = float(number2)
        except (ValueError, TypeError):
            return Response({"error": "number1 and number2 must be integers or floats"}, status=400)
        
        result = number1 * number2
        
        return Response({"result": result})
