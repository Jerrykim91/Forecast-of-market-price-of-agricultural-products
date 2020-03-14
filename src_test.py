
# 코드를 가지고 오기전 내가 뭘 크롤링 해올지 보자 
# 1년치 배추 상품 데이터 크롤링 
# - 100 일이 넘어 가면 안된다 

# 1. 홈페이지에 접속을 한다 
# 2. 날자 범위를 정한다 
# 3. 속성을 정한다. 
# 4. 조회를 누른다. 
# 5. url 주소를 확인한다. 
order_path = 'https://www.kamis.or.kr/customer/price/retail/period.do'
action_path = ''

# ? 뒤로 액션 
action = f'?action=daily&startday={startday}&endday={endday}&countycode=&itemcategorycode=100&itemcode=111&kindcode=&productrankcode=&convert_kg_yn=N
'
# startday
startday = '2019-06-03'
# endday
endday = '2019-06-03'

# itemcategorycode 
itemcategorycode = 200   # 채소류 : 200, 과일류 : 400

# itemcode : 품목
itemcode = 211   # 무 : 231, 배추 : 211, 사과 : 411, 파 : 246, 배 : 412

# kindcode : 품종, 없으면 ''
# 사과-후지 : 05, 배-신고 : 01
kindcode = '01'

# 개발자 모드에서 보니까 지역코드 ,
url = order_path + action
