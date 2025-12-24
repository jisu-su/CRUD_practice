# delete 삭제하기
# 1. 특정 줄만 삭제하기
# 2. 파일 전체 삭제하기

# 수동일 경우에는 읽기 - 삭제 - 다시쓰기

file = open("instructor.txt","r",encoding="utf-8")
lines = file.readlines()
file.close()

del (lines[1])

file = open("instructor.txt","w",encoding="utf-8")
file.writelines(lines)
file.close()