# Guidelines
- Find admin token in synapse DB, table `access_tokens`. Token should have prefix as `syt_<xxx>`. Replace in `ADMIN_TOKEN` env variable
- Update environment variables in FILE `run.sh`:
```
export SYNAPSE_SERVER=http://0.0.0.0:8008
export ADMIN_TOKEN=syt_YWRtaW4_VCTyHEmfytfkCxhHlRhD_16ZG4e
export WIDGET_URLS='["uCall","https://google.com","uCall 2","http://localhost:3000"]'
```
- PLEASE FOLLOW these structure for `WIDGET_URLS`:
  - `export WIDGET_URLS = '["NAME", "URL"]'` with `NAME` is your widget name, `URL` is url of your widget
  - If you had more than 1 widget, keep appending like ["NAME", "URL", "NAME", "URL", ...]
  - Everytime startup, app will check existed widget name. If not create a new one. If existed, update with latest url

- Remember to integrate with Element:
```
...
  "integrations_ui_url": "http://localhost:8011/element",
  "integrations_rest_url": "http://localhost:8011/api/v1/scalar",
  "integrations_widgets_urls": [
    "http://localhost:8011/widgets"
  ],
...
```

- FYI, the intergration process should be very similar to Dimension. You can reference here: https://github.com/Automattic/matrix-env/blob/master/dimension.md