# delete 삭제하기
# 1. 특정 줄만 삭제하기
# 2. 파일 전체 삭제하기

file = open("instructor.txt","a",encoding="utf-8")
file.write("\n 특정 줄 삭제를 위한 줄 추가 \n 메리크리스마스")
file.close()
