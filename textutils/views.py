# i have created this file -arun prakasH
from django.http import HttpResponse
from django.shortcuts import render
#

def index(request):
    return render(request,'index.html')
def aboutus(request):
    return render(request,'aboutus.html')

def analyze(request):
    # get the text
    djtext = request.POST.get('text', 'default')
    removepunc=request.POST.get('removepunc','off')
    fullcaps=request.POST.get('fullcaps','off')
    newlineremover=request.POST.get('newlineremover','off')
    spaceremover=request.POST.get('spaceremover','off')
    charcount=request.POST.get('charcount','off')


    if removepunc == "on":
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed=""
        for char in djtext:
            if char not in punctuations:
                analyzed=analyzed+char
        params={'purpose':'Remove Punctuations   ','analyzed_text': analyzed}
        djtext = analyzed
        #return render(request,'analyze.html',params)
    if (fullcaps == "on"):
        analyzed=""
        for char in djtext:
            analyzed=analyzed+char.upper()
        params = {'purpose': 'Change to uppercase   ', 'analyzed_text': analyzed}
        djtext=analyzed
        #return render(request, 'analyze.html', params)

    if (newlineremover=="on"):
        analyzed=""
        for char in djtext:
            if char!=("\n") and char!=("\r"):
                analyzed=analyzed+char
        params = {'purpose': 'remove new lines  ', 'analyzed_text': analyzed}
        djtext=analyzed
        # return render(request, 'analyze.html', params)

    if (spaceremover =="on"):
        analyzed=""
        for index,char in enumerate(djtext):
            if not(djtext[index]==" " and djtext[index+1]==" "):
                analyzed=analyzed+char
        params = {'purpose': 'remove extra spaces ', 'analyzed_text': analyzed}
        djtext=analyzed
        # return render(request, 'analyze.html', params)

    if(charcount == "on"):
        analyzed = ""
        analyzed=len(djtext)

        params = {'purpose': 'char count in values', 'analyzed_text': analyzed}
        djtext=analyzed
        # return render(request, 'analyze.html', params)
    if(removepunc!="on" and fullcaps!="on" and newlineremover!="on" and spaceremover!="on" and charcount!="on"):
        return HttpResponse("please select any operation and try again ")

    return render(request, 'analyze.html', params)
