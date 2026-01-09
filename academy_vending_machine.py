# 1. 자판기 관찰
# 2. input - 현금, 카드를 먼저 투입한다.
pay = input()
# 3. 입력 창 만들기 - 상품 번호 입력하고 결정 버튼을 누른다. > 버튼화 
# 아이템 목록 만들기
products = [
    {"id":10, "name": "미에로 화이바", "price": 900},
    {"id":11, "name": "하늘보리", "price": 1500},
    {"id":12, "name": "헛개차", "price": 1500},
    {"id":13, "name": "보성홍차 아이스티", "price": 1600},
    {"id":14, "name": "알로에 농장", "price": 1600},
    {"id":15, "name": "포도 봉봉", "price": 1300},
    {"id":16, "name": "토레타", "price": 1600},
    {"id":17, "name": "아몬드 초콜렛", "price": 2000},
    {"id":20, "name": "코코팜", "price": 1300},
    {"id":21, "name": "T.O.P 라떼", "price": 1500},
    {"id":22, "name": "T.O.P 블랙", "price": 1500},
    {"id":23, "name": "멘토스 민트", "price": 2200},
    {"id":24, "name": "몬스터 핑크", "price": 2200},
    {"id":25, "name": "콘트라베이스 라떼", "price": 2000},
    {"id":26, "name": "몬스터 화이트", "price": 2200},
    {"id":27, "name": "애플망고", "price": 1200},
    {"id":28, "name": "콘트라베이스 블랙", "price": 2000},
    {"id":30, "name": "포카리 스웨트", "price": 1300},
    {"id":31, "name": "갈아만든 배", "price": 1300},
    {"id":32, "name": "고려은단 비타민C", "price": 800},
    {"id":33, "name": "코카콜라", "price": 1400},
    {"id":34, "name": "델몬트 망고", "price": 1000},
    {"id":35, "name": "초코송이", "price": 1300},
    {"id":36, "name": "다이제 씬", "price": 1500},
    {"id":37, "name": "코카콜라 제로", "price": 1400},
    {"id":40, "name": "불닭볶음면", "price": 1500},
    {"id":41, "name": "신라면", "price": 1300},
    {"id":42, "name": "참깨라면", "price": 1300},
    {"id":43, "name": "농심 육개장", "price": 1300},
    {"id":44, "name": "농심 육개장", "price": 1300},
    {"id":45, "name": "환타 오렌지", "price": 1300},
    {"id":50, "name": "예감", "price": 1600},
    {"id":51, "name": "닥터유 에너지바", "price": 1300},
    {"id":52, "name": "불닭볶음면", "price": 1500},
    {"id":53, "name": "신라면", "price": 1300},
    {"id":54, "name": "빠다코코낫", "price": 1600},
    {"id":60, "name": "화이트하임", "price": 1500},
    {"id":61, "name": "프링글스", "price": 1600},
    {"id":62, "name": "초코에몽", "price": 1300},
    {"id":63, "name": "오레오", "price": 1600},
    {"id":64, "name": "ABC 초코쿠키", "price": 1300},
    {"id":70, "name": "통크", "price": 1300},
    {"id":71, "name": "마켓오 브라우니", "price": 3000},
    {"id":70, "name": "에이스", "price": 1300}
]

# 고객의 상품 번호 입력
want_number = int(input())

# 아이템_번호_버튼(아이템_목록)
def product_number_button(products_list):
    for product in products:
        if want_number == products

# 4. 카드면 승인 절차, 현금이면 총합 계산 후 거스름돈
# 5. 출력 - 사용자가 선택한 제품, 거스름돈
# 6. 추가적인 CRUD  - 자판기 건의함
# - 이미 정해져 있는 제품들
# - 사용자가 원하는 물건을 적는다.
# - 판매자가 확인하다.
# - 가능한 것들을 추가하고, 뺄 것들은 뺀다.