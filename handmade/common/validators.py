from django.core.exceptions import ValidationError


def only_letters_validator(value):
    for ch in value:
        if not ch.isalpha():
            raise ValidationError('Value must contain only letters')


def photo_max_size_validator_in_mb(photo):
    max_size_mb = 100
    if photo.file.size > max_size_mb * 1024 * 1034:
        raise ValidationError("Max file size is %sMB" % str(max_size_mb))