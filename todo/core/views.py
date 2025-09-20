from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.db import connections
from django.db.utils import OperationalError


@api_view(['GET'])
def health_check(request):
    db_conn = connections['default']
    try:
        db_conn.cursor()
        db_status = 'ok'
    except OperationalError:
        db_status = 'error'

    return Response({
        'status': 'ok',
        'database': db_status
    })