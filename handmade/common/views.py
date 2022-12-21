from django.shortcuts import render
from django.views import View


class InternalErrorView(View):
    def get(self, request):
        return render(request, 'common/internal_error.html')


class Error404View(View):
    def get(self, request):
        return render(request, 'common/404_page.html')
