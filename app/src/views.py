#from django.http import HttpResponse
from django.shortcuts import render
from io import StringIO

import matplotlib.pyplot as plt
import csv
import os
import numpy as np
import datetime



def index(request):
    """Placeholder index view"""
    # return HttpResponse(return_graph())
    return render(request, 'dashboard.html', {"form": return_graph()})


def return_graph():
    # x = np.arange(0, np.pi*3, .1)
    # y = np.sin(x)
    dirname = os.path.dirname(__file__)
    filename = os.path.join(dirname, 'csv/python_exercise_trades.csv')
    
    x = []
    y = []
    # arr = list()
    stockDataObj = []
    tQuantity = []
    qtyData = 0
    with open(filename, 'r') as csvfile:
        plots = csv.reader(csvfile, delimiter=',')
        next(plots)
        
        for row in plots:
            d = datetime.datetime.strptime(row[2], "%d/%M/%Y")
            if d.year not in x:
                x.append(d.year)

            qtyData = round(int(row[4]) * float(row[5]))
            stockDataObj.append({
                'year': d.year,
                'price': float(row[5]),
                'quantity': int(row[4]),
                'date': row[2],
                'item_price': qtyData
            })

        price_added = 0
        price_lose = 0
        maped_stock_data_add = []
        maped_stock_data_lose = []
        maped_qnty = []
        #print(stockDataObj)
        for dataObj in stockDataObj:
            if (dataObj.get('quantity') < 0):
                price_lose += dataObj.get('item_price')
                maped_stock_data_add.append({dataObj.get('year'): price_lose})
            elif (dataObj.get('quantity') > 0):
                maped_qnty.append(dataObj.get('quantity'))
                price_added += dataObj.get('item_price')
                maped_stock_data_lose.append({dataObj.get('year'): price_added})

            # fig, ax = plt.subplots(1,1)
            # a = np.array(temp)
            # ax.hist(a, bins=x)
            # ax.set_title("Essentia Analytics Recruitment Exercise")
            # ax.set_xticks(x)
            # ax.set_xlabel('Year')
        
    # fig = plt.figure()
    # plt.plot(maped_qnty, maped_qnty)
    reduced = np.array(maped_qnty)
    getArr = np.partition(-reduced, 2)
    result = -getArr[:5]
    lengths = result.__len__
    colors = ['green']
    fig, ax = plt.subplots(1, 1)
    a = np.array(result)

    ax.hist(a, bins=[0, 25, 50, 75, 100],
            histtype='bar',
            color=colors)
    ax.set_title("histogram of result")
    ax.set_xticks([0, 25, 50, 75, 100])
    ax.set_xlabel('Qty')
    ax.set_ylabel('no.')

    imgdata = StringIO()
    fig.savefig(imgdata, format='svg')
    imgdata.seek(0)
    data = imgdata.getvalue()
    return data
