# delete 삭제하기
# 1. 특정 줄만 삭제하기
# 2. 파일 전체 삭제하기

# 파일 전체 삭제할 경우 os 도구를 빌려와야 한다.
#2.
import os
if os.path.exists("instructor.txt"):
    os.remove("instructor.txt")
    print("파일이 완전히 삭제되었습니다")
else:
    print("삭제할 파일이 없습니다")