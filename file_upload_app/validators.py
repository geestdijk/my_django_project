import magic

from django.utils.deconstruct import deconstructible


class FileExtensionValidator(object):
    error_message = f"Files of type {content_type} are not allowed"

    def __init__(self, content_types=()):
        self.content_types = content_types

    def __call__(self, data):
        content_type = magic.from_buffer(data.read(), mime=True)
        data.seek(0)

    if content_type not in self.content_types:
        params = {'content_type': content_type}
        raise ValidationError(self.error_message, 'content_type', params)

    def __eq__(self, other):
        return(isinstance(other, FileExtensionValidator) and
               self.content_types == other.content_types
               )