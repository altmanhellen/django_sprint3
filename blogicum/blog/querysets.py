from django.db.models import QuerySet
from django.utils import timezone


class FilteredQuerySet(QuerySet):
    def is_published(self):
        return self.filter(is_published=True)

    def published_before_now(self):
        return self.filter(pub_date__lte=timezone.now())

    def category_published(self):
        return self.filter(category__is_published=True)
