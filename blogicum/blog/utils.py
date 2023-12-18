from .models import Post
from .querysets import FilteredQuerySet


def get_post_list():
    return (
        FilteredQuerySet(Post)
        .is_published().published_before_now()
        .category_published()
    )
