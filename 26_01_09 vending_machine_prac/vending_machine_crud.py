# 6. 추가적인 CRUD  - 자판기 건의함
# >> 일단 함수로 만들어 보고 클래스로 묶어보기.
# 건의 사항 게시판
suggestion_board = []
# 6-1. create
def create_suggestion():
    # 사용자가 건의 내용을 입력한다.
    suggestion = input()
    # 건의함 목록에 추가 된다.
    suggestion_board.append(suggestion)

# 6-2. read
def read_suggestion():
    # 건의 사항 게시판을 글을 확인한다.
    for idx, suggestion in enumerate(suggestion_board):
        print(f"건의사항 {idx}번. {suggestion}")

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
def delete_suggestion(suggestion_board):
    # 일단 게시판에 어떤게 있는지 보기
    read_suggestion()
    # 삭제할 게시물 인덱스 번호 입력하기
    print(f"처리 완료된 건의 사항 삭제를 위한 인덱스 번호 입력")
    delete_idx = int(input())
    # 게시판에서 해당 번호 삭제하기 
    if 0 <= delete_idx < len(suggestion_board):
        suggestion_board.pop(delete_idx)
        print(f"{delete_idx}번 건의 사항이 처리되어 삭제되었습니다.")
    else:
        print("잘못된 번호입니다.")