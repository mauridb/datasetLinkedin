# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import singleton as singleton
from django.shortcuts import render, redirect
import csv
import sys
from unicodecsv import DictReader

reload(sys)
sys.setdefaultencoding('utf-8')


class Counter():
    def __init__(self):
        self.counter = 0

    def plus_one(self):
        self.counter += 1
        return self.counter


c = Counter()


def index(request):
    if request.method == 'POST':
        # print 'sono in post'

        with open('datasetBigDive.csv', 'a') as csvfile:
            fieldnames = ['ID', 'FIRST_NAME', 'LAST_NAME', 'JOB_PLACEMENT', 'COMPANY', 'NATION', 'COUNTRY']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            if c.counter == 0:
                writer.writeheader()

            c.plus_one()
            writer.writerow(
                {'ID': c.counter, 'FIRST_NAME': request.POST.get('name'), 'LAST_NAME': request.POST.get('surname'),
                 'JOB_PLACEMENT': request.POST.get('job'),
                 'COMPANY': request.POST.get('company'), 'NATION': request.POST.get('nationality'),
                 'COUNTRY': request.POST.get('country')})

    return render(request, 'alumniLinkedin/index.html', {})


def reader(request):
    if request.method == 'POST':
        # print 'sono in post'
        # print request.POST.get('src')
        # read csv file
        elem_founded = []

        with open('datasetBigDive.csv') as csvfile:
            dataset = csv.reader(csvfile)
            for row in dataset:
                # print row
                for i in row:
                    # print i
                    if i == request.POST.get('src'):
                        print row
                        elem_founded.append(row)

        print elem_founded
        context = {
            'wanted': elem_founded,
        }
        return render(request, 'alumniLinkedin/reader.html', context)
    return render(request, 'alumniLinkedin/reader.html', {})


def call_api(request):
    return render(request, 'alumniLinkedin/callApi.html', {})
