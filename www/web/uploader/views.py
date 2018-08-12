from django.shortcuts import render
from django.views import View

# Create your views here.
class UploaderView(View):
    def get(self, request, *args, **kwargs):
        return render(request, "uploader/get.html", {})

    def post(self, request, *args, **kwargs):
        name = request.POST.get('name')
        value = request.POST.get('value')
        return render(request, "uploader/post.html", {'name': name, 'value': value})

uploader = UploaderView.as_view()
