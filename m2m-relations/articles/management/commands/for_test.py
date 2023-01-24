from django.core.management.base import BaseCommand
from articles.models import Article, Tag, Scope


class Command(BaseCommand):
    def add_arguments(self, parser):
        pass


    def handle(self, *args, **options):
        object_list = Article.objects.all()
        for article in object_list:
            print(f'title - {article.title}. text - {article.text}')
            for scope in article.scopes.all():
                print(scope.tag.name)
                print(scope.is_main)
            print('--------------------------')
