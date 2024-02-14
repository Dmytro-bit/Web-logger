from django.db import models

LOG_LEVELS = [
    ("DEBUG", "DEBUG"),
    ("INFO", "INFO"),
    ("WARNING", "WARNING"),
    ("ERROR", "ERROR"),
    ("CRITICAL", "CRITICAL"),
]


class App(models.Model):
    name = models.CharField(max_length=100, unique=True)
    key = models.CharField(max_length=200, unique=True)
    active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Log(models.Model):
    level = models.CharField(max_length=10, choices=LOG_LEVELS)
    app = models.ForeignKey(App, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-timestamp']

    def __str__(self):
        return self.level


class LogField(models.Model):
    log_name = models.CharField(max_length=100)
    log_value = models.TextField()
    log = models.ForeignKey(Log, on_delete=models.CASCADE)

    def __str__(self):
        return self.log_name
