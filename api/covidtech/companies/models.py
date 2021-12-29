from django.db import models

# Create your models here.


class Company(models.Model):
    class CompanyStatus(models.TextChoices):
        LAYOFFS = "layoffs"
        HIRING_FREEZE = "hiring_freeze"
        HIRING = "hiring"

    name = models.CharField(max_length=30, unique=True)
    status = models.CharField(
        choices=CompanyStatus.choices, default=CompanyStatus.HIRING, max_length=30
    )
    last_update = models.DateTimeField(auto_now=True, editable=True)
    application_link = models.URLField(blank=True, null=True)

    def __str__(self):
        return f"{self.name}"
