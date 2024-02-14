import hashlib
from functools import wraps

from django.http import JsonResponse

from .models import App


def password_encryption(password):
    hash_algorithm = hashlib.sha256()
    hash_algorithm.update(password.encode('utf-8'))
    hashed_password = hash_algorithm.hexdigest()
    return hashed_password


def password_verification(entered_password, stored_hashed_password):
    hashed_entered_password = password_encryption(entered_password)
    return hashed_entered_password == stored_hashed_password


def app_login_required(func):
    @wraps(func)
    def wrapper(request, *args, **kwargs):
        app = App.objects.get(active=True)
        if app.exists() and password_verification(request.POST.get('password'), app.key):
            return func(request, *args, **kwargs)
        else:
            return JsonResponse({"success": False, "message": "Invalid password"}, status=401)

    return wrapper
