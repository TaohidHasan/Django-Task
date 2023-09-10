from django.shortcuts import render
from website.forms import StockForm  
from website.models import Stock
from django.shortcuts import redirect


def show(request):
    return render(request,"show.html")  

def addnew(request):  
    if request.method == "POST":  
        form = StockForm(request.POST)  
        if form.is_valid():  
            try:  
                form.save()  
                return redirect('/')  
            except:  
                pass
    else:  
        form = StockForm()  
    return render(request,'index.html',{'form':form})  

def index(request):
    stocks = Stock.objects.all()  
    return render(request,"home.html",{'stocks':stocks})   
     
def destroy(request, id):  
    stock = Stock.objects.get(id=id)  
    stock.delete()  
    return redirect("/")

def update(request, id):  
    stock = Stock.objects.get(id=id)  
    return render(request,'update.html', {'stock':stock})  

def uprec(request,id):
    d=request.POST['date']
    t=request.POST['Trade']
    h=request.POST['High']
    l=request.POST['Low']
    o=request.POST['Open']
    c=request.POST['Close']
    v=request.POST['Volume']
    stock=Stock.objects.get(id=id)
    stock.date=d
    stock.Trade=t
    stock.High=h
    stock.Low=l
    stock.Open=o
    stock.Close=c
    stock.Volume=v
    stock.save()
    return redirect("/") 

def bar_chart(request):
    data = Stock.objects.order_by('date')
    chart_data = {
        'labels': [str(item.date) for item in data],
        'close_values': [float(item.Close) for item in data],
    }

    context = {
        'chart_data': chart_data,
        'table_data': data,
    }

    return render(request, 'bar_chart.html', context) 

def pie_chart(request):
    data = Stock.objects.order_by('date')
    chart_data = {
        'labels': [str(item.date) for item in data],
        'close_values': [float(item.Open) for item in data],
    }

    context = {
        'chart_data': chart_data,
        'table_data': data,
    }

    return render(request, 'pie_chart.html', context) 

def line_chart(request):
    data = Stock.objects.order_by('date')
    chart_data = {
        'labels': [str(item.date) for item in data],
        'close_values': [int(item.Volume) for item in data],
    }

    context = {
        'chart_data': chart_data,
        'table_data': data,
    }

    return render(request, 'line_chart.html', context) 




def stock_chart(request):
    stocks = Stock.objects.all().order_by('date')
    trade_codes = Stock.objects.values_list('Trade', flat=True).distinct()
    return render(request, 'stock_chart.html', {'stocks': stocks, 'trade_codes': trade_codes})


def trade_chart(request):
    stocks = Stock.objects.all().order_by('Trade')
    trade_codes = Stock.objects.values_list('date', flat=True).distinct()
    return render(request, 'trade_chart.html', {'stocks': stocks, 'trade_codes': trade_codes})
