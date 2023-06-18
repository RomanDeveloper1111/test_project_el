from djchoices import ChoiceItem, DjangoChoices


class PostStatusChoices(DjangoChoices):
    unpublished = ChoiceItem('unpublished', 'unpublished')
    published = ChoiceItem('published', 'published')
    published_and_send = ChoiceItem('published_and_send', 'published_and_send')