from django.contrib import admin
from devault.notifications.endpoints import Message




class AdminMixIn(admin.ModelAdmin):
    def save_model(self, request, obj, form, change):
        if not obj.author:
            obj.author = request.user
        obj.editor = request.user
        obj.save()
        obj.name = obj.__str__()
        message = Message("save", request.user.username, (obj, obj.version, obj.environment))
        message.send_message()
        
        
        
class AdminMixInName(admin.ModelAdmin):
    fields = ("name", "comment")
    list_display = ("name", "author", "created", "editor", "modified")
    def save_model(self, request, obj, form, change):
        if not obj.author:
            obj.author = request.user
        obj.editor = request.user
        obj.save()
        message= Message("save", request.user.username, (obj,))    
        message.send_message()
    
