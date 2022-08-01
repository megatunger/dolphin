from django.apps import AppConfig

from dolphin import settings

def pairwise(iterable):
    a = iter(iterable)
    return zip(a, a)

class WidgetConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'widget'

    def ready(self):
        from widget.models import Widget
        if 'widget_widget' in connection.introspection.table_names():
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
            # print(widget)