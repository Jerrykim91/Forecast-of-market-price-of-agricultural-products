
# 보류 

# def date_list_t(year):
#     # 이게 1년분 -> 총 4개 근데 반복 
#     # 1-3(1분기) , 10-12(4분기) => 31 
#     # 4-6(2분기) , 7-9(3분기)   => 30 

#     # date_list = [('2019-01-01', '2019-03-31'), ('2019-04-01', '2019-06-30'), ('2019-07-01', '2019-09-30'), ('2019-10-01', '2019-12-31')] 
#     # 만약에 1년이상이라면 
#     # 만약에 1년미만이라면 
#     year = year # 년도는 고정 

#     month_start = month 
#     month_end   = month + 2

#     # test_date = [(f'{str(year)}-'+ str(month_start)+'-01'), f'{str(year)}-'+ str(month_end)+'-31')] 
#     if month == 1 or 10:
#         day = '31'
#         test_date = [(year+'-' + str(month_start)+'-'+ '01'), (year+'-' + str(month_start)+'-'+ day)]
#         print('31')
        
#     elif month == 4 or 7:
#         day = '30'
#         test_date = [(year+'-' + str(month_start)+'-'+ '01'), (year+'-' + str(month_start)+'-'+ day)]
#         print('30')

#     print(test_date)

# pass

# -------------- # 

# for i in range(1,5): # 1부터 4분기 
#     # 1분기가 들어오면 -> 월 = 1 , 1+2 =3 -? 1분기 생성 이거를 담아야해 

#     print(i) 

# # 리턴 값은 리스트 형태로 -> [(),()]
# return 



# -------------- # 

x= 10 
year = 2001
month = 0

# -------------- # 

if  1 <= month <= 9 :
    month = '0'+ month
    print('1자리')

elif 1 <= month <= 12:
    print('10자리')

else:
    month == 0 or month <= 13 
    print('error')


# date_list = [(year+'-01-01', year+'-03-31'), (year+'-04-01', year+'-06-30'), (year+'-07-01', year+'-09-30'), (year+'-10-01', year+'-12-31')] 

# -------------- # 

date_list = [] 
for i in range(1, x+1):
    # print(year + i)
    year = year + 1
    # date_list = [(year+'-01-01', year+'-03-31'), (year+'-04-01', year+'-06-30'), (year+'-07-01', year+'-09-30'), (year+'-10-01', year+'-12-31')] 
    date_year = [(str(year)+'-01-01', str(year)+'-03-31'), (str(year)+'-04-01', str(year)+'-06-30'), (str(year)+'-07-01', str(year)+'-09-30'), (str(year)+'-10-01', str(year)+'-12-31')] 
    # print(date_list)
    date_list.append(date_year)

# print(date_list, len(date_list))

for idx in range(x):  
    for start_date , end_date in date_list[idx]:
        print('start_date', start_date, 'end_date', end_date)

# -------------- # 
tmp = [] 
for i in range(1,100):
    print([i])
    tmp.append([i])
# -------------- # 
