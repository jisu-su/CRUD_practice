# delete 삭제하기
# 1. 특정 줄만 삭제하기
# 2. 파일 전체 삭제하기

# 파일 전체 삭제할 경우 os 도구를 빌려와야 한다.
#1.
import os
os.remove("instructor.txt")