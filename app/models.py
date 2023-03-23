from django.db import models

class Files(models.Model):
    filename=models.CharField(max_length=100)
    user=models.CharField(max_length=100,primary_key=True)

    def __str__(self) -> str:
        return f"File : {self.filename} by {self.user}"
