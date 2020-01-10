year = int(input("년도 : "))
month = int(input("월 : "))
day = int(input("일 : "))
today_year = 0
today_month = 0
today_day = 0
yunyear = 0
notyunyear = 0

for i in range(1,year):
    if (((i%4 == 0) and (i%100 != 0)) or (i% 400 == 0)):
        yunyear += 1
    else:
        notyunyear += 1
today_year = yunyear*366 + notyunyear*365

for i in range(1,month):
    if i == 1 or i == 3 or i == 5 or i == 7 or i == 8 or i == 10 or i == 12:
        month_day = 31
    elif i == 4 or i == 6 or i == 9 or i == 11:
        month_day = 30
    else:
        if (((i%4 == 0) and (i%100 != 0)) or (i% 400 == 0)):
            month_day = 29
        else:
            month_day = 28

    today_month += month_day
today_day = today_year + today_month + day

if today_day % 7  == 1:
    print("{}년 {}월 {}일은 월요일입니다.".format(year,month,day))
elif today_day % 7 == 2:
    print("{}년 {}월 {}일은 화요일입니다.".format(year,month,day))
elif today_day % 7  == 3:
    print("{}년 {}월 {}일은 수요일입니다.".format(year,month,day))
elif today_day % 7  == 4:
    print("{}년 {}월 {}일은 목요일입니다.".format(year,month,day))
elif today_day % 7  == 5:
    print("{}년 {}월 {}일은 금요일입니다.".format(year,month,day))
elif today_day % 7  == 6:
    print("{}년 {}월 {}일은 토요일입니다.".format(year,month,day))
elif today_day % 7  == 0:
    print("{}년 {}월 {}일은 일요일입니다.".format(year,month,day))