from django.views.generic import ListView
from note.models import Note, Tag
from note.views import getDistinctUserTags
from django.http import JsonResponse

class HomePage(ListView):
    template_name = "base/home_page.html"
    model = Note
    
    def get_queryset(self):
        queryset = super(HomePage, self).get_queryset()
        if self.request.user.is_authenticated:
            user = self.request.user
            queryset = Note.objects.filter(user_id=user.id)
        else:
            queryset = Note.objects.none()
        return queryset
    
    def get_context_data(self, **kwargs):
        context = super(HomePage, self).get_context_data(**kwargs)
        # json_serializer = serializers.get_serializer("json")()
        if self.request.user.is_authenticated:
            tagList = ""
            tags = getDistinctUserTags(self.request)
            for q in tags:
                tagList+=q.name+","
            context['tagList']=tagList[:len(tagList)-1]
            context['tags'] = tags
        return context
