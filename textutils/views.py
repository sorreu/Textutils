
from django.http import HttpResponse
from django.shortcuts import render




def index(request):
    return render(request, 'index.html')



def analyze(request):
    djtext = request.POST.get('text', 'default')


    removepunc = request.POST.get('removepunc', 'off')
    fullcaps = request.POST.get('fullcaps', 'off')
    newlineremov = request.POST.get('newlineremover', 'off')
    spaceremov = request.POST.get('spaceremover', 'off')


    if removepunc == 'on':

        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed = ""
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char

        params = {'purpose': 'Removed Punctuations', 'analyzed_text': analyzed}
        djtext = analyzed


    if fullcaps == "on":
        analyzed = ""
        for cha in djtext:
            analyzed = analyzed + cha.upper()
        params = {'purpose': 'Capitalization', 'analyzed_text': analyzed}
        djtext = analyzed


    elif newlineremov == 'on':
        analyzed = ""
        for cha in djtext:
            if cha != "\n" and cha != "\r":
                analyzed = analyzed + cha
        params = {'purpose': 'Removed newlines', 'analyzed_text': analyzed}
        djtext = analyzed


    if spaceremov == 'on':
        analyzed = ""
        for index, cha in enumerate(djtext):

            if not (djtext[index] == " " and djtext[index + 1] == " "):
                analyzed = analyzed + cha
        params = {'purpose': 'space remove', 'analyzed_text': analyzed}


    if (removepunc != "on" and newlineremov != "on" and spaceremov != "on" and fullcaps != "on"):
        return HttpResponse("please select any operation and try again")
    return render(request, 'analyze.html', params)
