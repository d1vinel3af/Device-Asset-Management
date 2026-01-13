from django.shortcuts import render


def test(request):
    
    return render(
        request=request,
        template_name="base.html"
    )