# 6. 추가적인 CRUD  - 자판기 건의함
# >> 일단 함수로 만들어 보고 클래스로 묶어보기.
# 건의 사항 게시판
sugestion_board = []
# 6-1. create
def create_sugestion():
    # 사용자가 건의 내용을 입력한다.
    sugestion = input()
    # 건의함 목록에 추가 된다.
    sugestion_board.append(sugestion)

# 6-2. read
def read_sugestion():
    # 건의 사항 게시판을 글을 확인한다.
    for idx, sugestion in enumerate(sugestion_board):
        print(f"건의사항 {idx}번. {sugestion}")

# 6-3. update
# 판매자가 건의 사항을 확인해서 직접 제품을 추가한다.
def add_product(products):
    # 새로운 제품을 직접 입력해서
    print("추가할 제품 번호를 입력하세요:")
    new_product_id = int(input())
    print("추가할 제품 이름을 입력하세요:")
    new_product_name = input()
    print("추가할 제품 가격을 입력하세요:")
    new_product_price = int(input())
    new_product = {
        "id": new_product_id,
        "name": new_product_name,
        "price": new_product_price
    }
# products 목록에 추가한다.
    products.append(new_product)
    print("제품이 추가되었습니다!")

# 6-4. delete
def delete_sugestion(sugestion_box):
    # 제품이 추가된 건의 사항은 게시판에서 삭제하기
        for idx, sugestion in enumerate(sugestion_board):
            # 삭제할 번호를 입력한다
            delete_sugestion_idx = int(input())
            sugestion.pop(delete_sugestion_idx)
            break