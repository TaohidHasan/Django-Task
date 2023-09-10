from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('addnew', views.addnew, name='addnew'), 
    path('delete/<int:id>', views.destroy, name='destroy'),
    path('update/<int:id>/',views.update,name="update"),
    path('update/uprec/<int:id>/',views.uprec,name="uprec") ,
    path('bar_chart/', views.bar_chart, name='bar_chart'),
    path('line_chart/', views.line_chart, name='line_chart'),
    path('stock_chart/', views.stock_chart, name='stock_chart'),
    path('trade_chart/', views.trade_chart, name='trade_chart'),
    path('pie_chart/', views.pie_chart, name='pie_chart'),
    
    path('show/', views.show, name='show'),

]


