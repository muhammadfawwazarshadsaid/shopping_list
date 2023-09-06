from django.shortcuts import render

def show_main(request):
    context = {
        'name': 'Muhammad Fawwaz Arshad Said',
        'class': 'PBP A'
    }

    return render(request, "main.html", context)