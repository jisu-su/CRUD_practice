# 1. 자판기 관찰
# 2. input - 현금, 카드를 먼저 투입한다.
print(f"결제 수단을 현금과 카드 중 선택하세요.")
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
    {"id":72, "name": "에이스", "price": 1300}
]

# 고객의 상품 번호 입력
print(f"구매하실 제품을 번호를 선택해주세요")
want_number = int(input())

# 아이템_번호_버튼(아이템_목록)
def product_number_button(products_list):
    # 각 아이템 목록에 대해 
    for product in products_list:
        # 만약에 고객이 원하는 상품 번호가 아이템 목록 id 숫자와 같은게 있다면
        if want_number == product["id"]:
            # 선택한 제품의 이름과 가격 출력하기
            print(f"선택하신 제품은 {product['name']}입니다.")
            print(f"선택하신 제품의 가격은 {product['price']}원입니다.")
            payment_process(pay)

# 4. 카드면 승인 절차, 현금이면 총합 계산 + 5. 거스름돈, 제품 출력
        # 결제 시스템 함수
        def payment_process(pay):
            # 만약 "현금" 결제라면:
            if pay == "현금":
                # 지불한 현금을 정수로 입력받기
                money = int(input())
                # 일단 합계를 0으로 저장
                total = 0 
                # 제품의 가격으로 덮어서 합계 출력
                total = product["price"]
                # 거스름돈
                change = money - total
                # 거스름돈 출력하기
                print(f"거스름돈은 {change}원입니다.")
                # 만약 "카드" 결제라면:
            elif pay == "카드":
                print(f"{product['price']}원 결제되었습니다.")
            # 결제한 제품 받기
            print(f"선택하신 {product['name']}이 나왔습니다. 감사합니다.")
    else:
        print(f"선택하신 번호에 제품이 없습니다.")

# 6. 추가적인 CRUD  - 자판기 건의함
# >> 일단 함수로 만들어 보고 클래스로 묶어보기.
# 건의 사항 게시판 만들기
sugestion_board = []
# 6-1. create
def create_sugestion():
    # 사용자가 건의 내용을 입력한다.
    sugestion = input()
    # 건의함 목록에 추가 된다.
    sugestion_board.append(sugestion)


# 함수 한 번에 호출하기
product_number_button(products)