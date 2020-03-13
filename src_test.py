# 코드를 가지고 오기전 내가 뭘 크롤링 해올지 보자 

# 1. 홈페이지에 접속을 한다 
# 2. 날자 범위를 정한다 
# 3. 속성을 정한다. 
# 4. 조회를 누른다. 
# 5. url 주소를 확인한다. 
order_path = 'https://www.kamis.or.kr/customer/price/retail/period.do'
action_path = ''

# ? 뒤로 액션 
?action=daily&startday=2019-03-01&endday=2019-06-03
&countycode=&itemcategorycode=100&itemcode=111&kindcode=&productrankcode=&convert_kg_yn=N

# 개발자 모드에서 보니까 지역코드 ,
url = order_path + 

url = f"https://www.kamis.or.kr/customer/price/retail/period.do?
action=daily&startday={startday}&endday={endday}
&countycode=&itemcategorycode={itemcategorycode}&itemcode={itemcode}&kindcode={kindcode}&productrankcode=1&convert_kg_yn=N"
