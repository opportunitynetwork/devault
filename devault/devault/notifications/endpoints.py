from django.conf import settings
from datadog import initialize
options = {
    'api_key':settings.DATADOG_API_KEY,
    'app_key':settings.DATADOG_APP_KEY
}
initialize(**options)
from datadog import api
from hipnotify import Room
from django.conf import settings

class Message(object):
    """Generic Message MixIn.
    """
    systems = []
    
    def __init__(self, action, username, objs, tags=None):
        object_type = objs[0].__class__.__name__.lower()
        operation = "save"

        if tags is None:
            tags = []

        for obj in objs:
            tags.append('object:%s' % obj.name)

        tags.append('object_type:%s' % object_type)
        tags.append('application:devault')

        self.title = '%s performed' % action
        self.text = '%s performed by %s' % (action, username)
        self.tags = tags
        self.objs = objs
        self.username = username
        if settings.DATADOG_API_KEY:
            self.systems.append("send_message_datadog")
        if settings.HIPCHAT_TOKEN:
            self.systems.append("send_message_hipchat")

    def send_message_hipchat(self):
        room = Room(settings.HIPCHAT_TOKEN, 
                    settings.HIPCHAT_ROOM_ID)
        message = '%s %s %s %s' % (self.username, self.title, self.text, ' '.join(self.tags))
        room.notify(message)

    def send_message_datadog(self):
        api.Event.create(title=self.title, 
                         text=self.text, tags=self.tags)

    def send_message(self):
        for system in self.systems:
            getattr(self, system)()



