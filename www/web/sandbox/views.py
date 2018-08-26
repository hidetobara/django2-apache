from django.shortcuts import render
from django.views import View

# Create your views here.
class SandboxView(View):
    def get(self, request, *args, **kwargs):
        return render(request, "sandbox/get.html", {})

    def post(self, request, *args, **kwargs):
        name = request.POST.get('name')
        value = request.POST.get('value')
        return render(request, "sandbox/post.html", {'name': name, 'value': value})

index = SandboxView.as_view()
