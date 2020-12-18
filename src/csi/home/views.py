from django.shortcuts import render
from tournament.models import Tournament
from news.models import Newse
from .models import Sponser
from datetime import datetime
# Create your views here.

def index(request):
    tour = Tournament.objects.all().order_by("tournament_startdate")
    # news_featured = Newse.objects.filter(news_category='Featured').order_by('-id')[0],

    news_featured = {
        'news1' : Newse.objects.filter(news_category='Featured').order_by('-id')[0],
        # 'news2' : Newse.objects.filter(news_category='Featured').order_by('-id')[1],
        # 'news3' : Newse.objects.filter(news_category='Featured').order_by('-id')[2]
    }
    news_latest = Newse.objects.filter(news_category='Latest').order_by("-timestamp")[0:4]
    spons1 = Sponser.objects.all()[0:5]
    spons2 = Sponser.objects.all()[5:]
    today = datetime.now()
    params = {'spons1':spons1,'spons2':spons2,'tour': tour,'today':today,'news_featured':news_featured,'news_latest':news_latest}
    return render(request,"home/index.html",params)

def tournaments(request, myid):
    tourview = Tournament.objects.filter(id=myid)
    params = {'tourview': tourview[0]}
    return render(request, "tounament/tournaments.html", params)

def events(request):
    event = Tournament.objects.values('id','tournament_name','tournament_startdate').order_by("tournament_startdate")
    params = {'event': event}
    return render(request,"home/events.html",params)

# def news(request):
#     pass



