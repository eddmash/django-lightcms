from django.core import checks
from django.db import models
from django.utils.text import slugify


class SlugField(models.SlugField):
    """A slug that takes an attribute to use to generate a slug"""

    def __init__(self, *args, **kwargs):
        self.field = kwargs.pop('field', '')
        super(SlugField, self).__init__(*args, **kwargs)

    def check(self, **kwargs):
        errors = super(SlugField, self).check(**kwargs)
        errors.extend(self._check_field(**kwargs))
        return errors

    def _check_field(self, **kwargs):
        if not self.field:
            return [
                checks.Error(
                    "SlugField must define a 'field' attribute.",
                    obj=self,
                    id='fields.E120',
                )
            ]
        else:
            return []

    def deconstruct(self):
        name, path, args, kwargs = super(SlugField, self).deconstruct()
        if self.field:
            kwargs['field'] = self.field
        return name, path, args, kwargs

    def pre_save(self, model_instance, add):
        # set value only on add
        if not model_instance.id and add:
            value = getattr(model_instance, self.field)

            count = model_instance.__class__.objects.filter(**{self.name:slugify(value)}).count()
            if count:
                value = slugify("{} {}".format(value, count))
            else:
                value = slugify(value)

            setattr(model_instance, self.attname, value)
            return value
        else:
            return super(SlugField, self).pre_save(model_instance, add)