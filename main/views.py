from django.shortcuts import render

def show_main(request):
    context = {
        'name': 'Apple iPad 9th Gen',
        'amount': '10',
        'description':'The iPad (9th generation) also referred as iPad 9, is a tablet computer developed and marketed by Apple Inc.',
        'price':'4.999.000',
        'date_added': '2023-09-13',
    }

    return render(request, "main.html", context)
