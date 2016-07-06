from django.conf import settings
from devault.notifications.endpoints import GenericMessageMixIn, HipchatMessageMixIn, DatadogMessageMixIn

def get_message_class():
    mixins = []
    class MessageTemplate(mixins):
        pass    

    return MessageTemplate

Message = get_message_class()
