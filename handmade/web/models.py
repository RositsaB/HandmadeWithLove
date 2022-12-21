from django.contrib.auth import get_user_model
from django.core.validators import MinLengthValidator
from django.db import models

from handmade.common.validators import photo_max_size_validator_in_mb

UserModel = get_user_model()


class Project(models.Model):
    NAME_MAX_LENGTH = 100
    NAME_MIN_LENGTH = 4

    UPLOAD_TO_DIR = 'project_photos/'

    name = models.CharField(
        max_length=NAME_MAX_LENGTH,
        validators=(
            MinLengthValidator(NAME_MIN_LENGTH),
        ),
    )

    description = models.TextField(
        null=False,
        blank=False,
    )

    date_of_publication = models.DateTimeField(
        auto_now_add=True,
    )

    photo = models.ImageField(
        upload_to=UPLOAD_TO_DIR,
        validators=(
            photo_max_size_validator_in_mb,
        )
    )

    user = models.ForeignKey(
        UserModel,
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return f'{self.name}'


class Favourites(models.Model):
    user = models.ForeignKey(
        UserModel,
        on_delete=models.CASCADE,
    )

    project = models.ForeignKey(
        Project,
        on_delete=models.CASCADE,
        related_name='favourites',
    )

    class Meta:
        unique_together = ('user', 'project')


class Comment(models.Model):
    AUTHOR_NAME_MAX_LEN = 30

    content = models.TextField()

    author_name = models.CharField(
        max_length=AUTHOR_NAME_MAX_LEN,
    )

    date_added = models.DateTimeField(
        auto_now_add=True,
    )

    project = models.ForeignKey(
        Project,
        on_delete=models.CASCADE,
    )

    user = models.ForeignKey(
        UserModel,
        on_delete=models.CASCADE,
        related_name='user_comment',
    )


class News(models.Model):
    TITLE_MAX_LENGTH = 100
    TITLE_MIN_LENGTH = 4

    title = models.CharField(
        max_length=TITLE_MAX_LENGTH,
        unique=True,
        validators=(
            MinLengthValidator(TITLE_MIN_LENGTH),
        ),
    )

    content = models.TextField(
        null=False,
        blank=False,
    )

    picture = models.URLField()