from django.http import JsonResponse
from django.views.decorators.http import require_POST

from .models import App, Log, LogField
from .utils import app_login_required


@require_POST
@app_login_required
def create_log(request):
    key = request.POST.get('key')
    level = request.POST.get('level')
    params: dict = request.POST.get('params')

    app = App.objects.get(key=key, active=True)
    log = Log.objects.create(level=level, app=app)
    for param, value in params.items():
        LogField.objects.create(log_name=param, log_value=log)

    return JsonResponse({"success": True, "message": "Log created successfully"}, status=200)
