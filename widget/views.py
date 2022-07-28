from django.shortcuts import render

def generic(request):
    return render(request, 'widgets/generic.html', {"url": request.GET.get('url')})
