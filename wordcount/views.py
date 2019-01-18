from django.shortcuts import render
import operator

def home(request):
    return render(request, 'home.html', {'text':'hey'})

def count(request):
    ft = request.GET['text']
    c = ft.split()
    wordict = {}
    for word in c :
        if word in wordict:
            wordict[word] +=1
        else:
            wordict[word]=1
    #sortedwords = sorted(wordict.items(), key=operator.itemgetter(1), reverse=True)

    return render(request, 'count.html', {'yourtext':ft, 'length':len(c), 'sortedwords':wordict.items()})

def about(request):
    return render(request, 'about.html')