import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'class.settings')

import django
django.setup()

from instrument.models import numOfYear, numOfMonth, numOfDay, numOfTime


def populate():
    #ADD YEAR
    python_year = add_year(2015)

    #ADD MONTH
    nameOfMonths = ["January","February","March","April","May","June","July","August","September","October","November","December"]
    numberOfDates = [31,      28,        31,     30,   31,    30,    31,     31,        30,        31,        30   ,    31];
    output = [0]*12
    for x in range(0,12):
        output[x] = add_month(python_year, nameOfMonths[x], x, numberOfDates[x])

    #ADD DAYS
    for x in range(0,12):
        count = 1
        for y in range(0,numberOfDates[x]):
            add_day(output[x], count)
            count = count + 1

    # Print out what we have added to the user.
    for c in numOfMonth.objects.all():
        print "- {0} ".format(str(c))

def add_year(number):
    y = numOfYear.objects.get_or_create(number=number)[0]
    y.save()
    return y


def add_month(numofyear, name, number, numberOfDays):
    m = numOfMonth.objects.get_or_create(numofyear=numofyear, name=name)[0]
    m.number=number
    m.numberOfDays=numberOfDays
    m.save()
    return m

def add_day(numofmonth, number):
    d = numOfDay.objects.get_or_create(numofmonth=numofmonth,number=number)[0]
    d.save()
    return d

def add_time(numofday, startHour, startMinute):
    t = numOfTime.objects.get_or_create(numofday=numofday, startHour=startHour)[0]
    t.startMinute=startMinute
    t.save()
    return t


# Start execution here!
if __name__ == '__main__':
    print "Starting Rango population script..."
    populate()