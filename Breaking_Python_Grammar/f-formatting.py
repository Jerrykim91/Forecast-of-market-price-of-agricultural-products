# 파이썬 문법 

## f-string 기능 
# - 파이썬의 다양한 포멧팅보다 직관적
# - 문자열을 표현하고자하는 대상변수의 type에 대해 자유도가 높음 


tuple = ('hi, i am ', 'song', 123) # tuple형 값 
# %-formatting는 기본적으로 int, string, double형만 지원 => tuple 지원 안함 
# 사용하기위해서는 steing 형을 명시적으로 변환해줘야함 

# %-formatting 사용시 
'tuple : %s %(str(tuple))'
# >>> "tuple : ( 'hi, i am', 'song', 123 )"

# f-formatting 사용시 
f'tuple:{tuple}'
# >>> "tuple: ('hi, i am', 'song', 123 )"


# 날짜 변수를 이용한 예제 
import datetime

date = datetime.datetime.now()
tmp =  f'{date: %Y-%m-%d } is on a {date: %A}'

# print(f'{date: %Y-%m-%d } is on a {date: %A}')
print(tmp)