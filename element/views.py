from datetime import datetime

import requests
from django.shortcuts import render

from dolphin import settings
from widget.models import ScalarToken, Widget


def view(request):
    scalar_token = request.GET.get('scalar_token')
    room_id = request.GET.get('room_id')
    room_name = request.GET.get('room_name')
    object = ScalarToken.objects.get(scalarToken=scalar_token)
    sysToken = object.sytToken
    widgets = Widget.objects.all()
    for widget in widgets:
        url = f'{settings.env("SYNAPSE_SERVER")}/_matrix/client/r0/rooms/{room_id}/state/im.vector.modular.widgets/widget_{widget.id}'
        check_existed = requests.get(url, headers={"Authorization": f'Bearer {sysToken}'})
        existed = check_existed.json().get('error')
        if (existed is None or existed == "Event not found.") and (check_existed.json().get('type') is None):
            response = requests.put(url, json={
                "type": "m.custom",
                "url": f"http://0.0.0.0:8000/widgets/generic?url={widget.url}",
                "name": f"{widget.title}",
                "data": {
                    "url": f"{widget.url}",
                    "dimension:app:metadata": {
                        "inRoomId": room_id,
                        "wrapperUrlBase": "http://0.0.0.0:8000/widgets/generic?url=",
                        "wrapperId": "generic",
                        "scalarWrapperId": "generic",
                        "integration": {
                            "category": "widget",
                            "type": "custom"
                        },
                        "lastUpdatedTs": int(datetime.now().timestamp() * 1000)
                    }
                }
            }, headers={"Authorization": f'Bearer {sysToken}'})
            print(response.json())
    return render(request, 'element/index.html')
