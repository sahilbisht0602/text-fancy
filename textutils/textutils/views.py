
# views.py
# I have created this file - Harry
from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request, 'index.html')


def analyze(request):
    #Get the text
    djtext = request.POST.get('text', 'default')
    removepunc=request.POST.get('removepunc','off')
    extraspaceremover=request.POST.get('extraspaceremover','off')
    charcount=request.POST.get('charcount','off')
    fullcaps=request.POST.get('fullcaps','off')
    newlineremover=request.POST.get('newlineremover','off')
    #Analyze the text
    if removepunc == 'on':
        analyzed = ""
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char
            params = {'purpose':'Analyzed text', 'analyzed_text': analyzed}
            djtext=analyzed
        #return render(request,'analyze.html', params)
    if extraspaceremover=='on':
        analyzed = ""
        for char in djtext:
            if not(char =="  "):
                analyzed = analyzed + char
        params = {'purpose': 'Extra space remover', 'analyzed_text': analyzed}
        djtext = analyzed
        #return render(request, 'analyze.html', params)
    if charcount=='on':
        analyzed = ""
        l=0
        for char in djtext:
            if char!=" ":
                l+=1
        print(l)
        params = {'purpose': 'Character count', 'analyzed_text': l}
        djtext = analyzed
        #return render(request, 'analyze.html', params)
    if fullcaps=='on':
        analyzed = ""
        for char in djtext:
            analyzed=analyzed+char.upper()
        params = {'purpose': 'full caps', 'analyzed_text': analyzed}
        djtext = analyzed
        #return render(request, 'analyze.html', params)
    if newlineremover == ' on ':
        analyzed = ""
        for char in djtext:
            if char!='\n' and char!='\r':
                analyzed = analyzed + char
        params = {'purpose': 'newlineremover', 'analyzed_text': analyzed}
        djtext=analyzed
        #return render(request, 'analyze.html', params)

    return render(request,'analyze.html',params)


