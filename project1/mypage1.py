# my page 1 - Stuti Kandpal
from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request, 'TextAnalyser.html')
    # f = open("project1/Home.html")
    # return HttpResponse(f.read())

def AnalysedText(request):
    djtext = request.POST.get('text','default')
    djRemPunc = request.POST.get('RemPunc', 'off')
    djCountChar = request.POST.get('CharCount', 'off')
    djCap = request.POST.get('Capitalize', 'off')
    djremspace = request.POST.get('Extraspace', 'off')
    Analysed=""
    countoriginal=0
    countnew=0
    #if djRemPunc == 'on':
    punc = '''!@#$%^&*()_-+={[}]:;"'>.<,?/\|'''
    if djRemPunc == "on":
        for char in djtext:
            if char not in punc:
                Analysed= Analysed + char
    else:
        Analysed = Analysed + djtext

    if djCap == "on":
        Analysed2=""
        for ch in Analysed:
            Analysed2= Analysed2+ch.upper()
        Analysed=Analysed2

    if djremspace == "on":
        Analysed2=""
        for cha in Analysed:
            if cha != ' ':
                Analysed2=Analysed2+cha
        Analysed=Analysed2

    if djCountChar == "on":
         countoriginal = countoriginal + len(djtext)
         countnew = countnew + len(Analysed)

    arg = {'Analysedtext': Analysed,'countoriginal':countoriginal,'countnew':countnew}
    return render(request, 'AnalysedText.html', arg)
