from django.shortcuts import render
def show_main(request):
    context = {
        'npm' : '2406360722',
        'name': 'A. Sheriqa Dewina Ihsan',
        'class': 'PBP B'
    }

    return render(request, "main.html", context)
# Create your views here.
