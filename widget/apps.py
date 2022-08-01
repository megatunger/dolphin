from django.apps import AppConfig
from django.db import connections
from dolphin import settings

def pairwise(iterable):
    a = iter(iterable)
    return zip(a, a)

def table_exists(table_name: str, connection_name: str) -> bool:
    return table_name in connections[connection_name].introspection.table_names()

class WidgetConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'widget'

    def ready(self):
        from widget.models import Widget
        if table_exists('widget_widget', 'default'):
            widgets = Widget.objects.all()
            env_widgets = list(eval(settings.WIDGET_URLS))
            for title, url in pairwise(env_widgets):
                widget = Widget.objects.filter(title=title)
                if widget.exists():
                    _widget = widget.get()
                    _widget.url = url
                    _widget.save()
                    print(f'Widget exist, {_widget.title} {_widget.url}')
                else:
                    _widget = Widget.objects.create(title=title, url=url, description="")
                    print(f'Create new widget, {_widget.title} {_widget.url}')