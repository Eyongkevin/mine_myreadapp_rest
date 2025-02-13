from django.db import models 
# from django.contrib.auth.models import User


class Reader(models.Model):
    """Reader model"""

    user = models.OneToOneField("auth.User", on_delete=models.CASCADE)
    
    READER_TITLE = {
        "Mr": "Mr",
        "Mrs": "Mrs",
        "Ms": "Ms",
        "Dr": "Dr"
    }
    title = models.CharField(max_length=5, null=True, blank=True, choices=READER_TITLE)
    nic = models.OneToOneField(
        'reader.NIC', 
        related_name='reader', 
        on_delete=models.CASCADE,
        null=True,
        blank=True)

    class Meta:
        # Define some meta data, including constraints
        db_table = 'reader'
        constraints = [
            models.CheckConstraint(
                # reader_Reader_title_check
                name='%(app_label)s_%(class)s_title_check',
                check=models.Q(title__in=['Mr', 'Mrs', 'Ms', 'Dr'])
            )
        ]