"""
Use this file to write your solution for the Summer Code Jam 2020 Qualifier.

Important notes for submission:

- Do not change the names of the two classes included below. The test suite we
  will use to test your submission relies on existence these two classes.

- You can leave the `ArticleField` class as-is if you do not wish to tackle the
  advanced requirements.

- Do not include "debug"-code in your submission. This means that you should
  remove all debug prints and other debug statements before you submit your
  solution.
"""
import datetime
import typing
import re
import itertools
from collections import Counter


class ArticleField:
    """The `ArticleField` class for the Advanced Requirements."""

    def __init__(self, field_type: typing.Type[typing.Any]):
        pass


class Article:
    """The `Article` class you need to write for the qualifier."""
    newid = itertools.count()
    def __init__(self, title: str, author: str, publication_date: datetime.datetime, content: str):
      self.id = next(Article.newid)
      self.title = title
      self.author = author
      self.publication_date = publication_date
      self.content = content
      self.last_edited = None

    def __repr__(self):
      return f'<Article title={repr(self.title)} author={repr(self.author)} publication_date={repr(self.publication_date.isoformat())}>'

    def __len__(self):
      return len(self.content)

    def  __gt__(self, other):
      return True if self.publication_date > other.publication_date else False

    def short_introduction(self, n_characters: int) ->  str:
      return ' '.join(re.split(r'[ \n]',self.content[:n_characters])[:-1])

    def most_common_words(self, n_words: int) -> dict:
      word_list = re.findall(r'\w+', self.content.lower())
      return dict(Counter(word_list).most_common(n_words))

article_one = Article(title="PEP-8", author="Guide van Rossum", content="Use snake_case", publication_date=datetime.datetime(2001, 7, 5))
print(article_one.id)

article_two = Article(title="Fluent Python", author="Luciano Ramalho", content="Effective Programming", publication_date=datetime.datetime(2015, 8, 20))
print(article_two.id)
article_two.id = 6
print(article_two.id)
