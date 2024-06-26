from django.contrib.postgres.fields import JSONField
from django.contrib.auth.models import User
from django.db.models import *


class Dashboard(Model):
    owner = ForeignKey(User, on_delete=CASCADE, default=None)
    name = CharField(max_length=80)
    theme = CharField(max_length=80, default='theme')
    private = BooleanField(default=False)
    description = TextField()
    created_at = DateTimeField('creation timestamp', auto_now_add=True)
    data = JSONField(default={})

    def __str__(self):
        return str(self.name)


class Figure(Model):
    figure_types = [
        ("frequency", "Frequency analysis"),
        ("wordcloud", "Wordcloud"),
        ("correlation", "Correlation heatmap"),
        ("sentiment", "Sentiment analysis"),
    ]
    dashboard = ForeignKey(Dashboard, on_delete=CASCADE)
    type = CharField(choices=figure_types, max_length=40, default="Frequency analysis")
    data = JSONField()
    params = JSONField()
    modify_at = DateTimeField('creation timestamp', auto_now_add=True)

    def __str__(self):
        return str(self.type)
