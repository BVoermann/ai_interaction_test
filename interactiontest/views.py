from django.shortcuts import render


def slider_view(request):
    return render(request, 'interactiontest/slider.html', {
        'slide_numbers': list(range(1, 10)),
    })
