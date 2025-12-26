# 저번 시간에 적어본 crud 수동을 자동으로 적어보기
# 오늘의 주제는 노래 가사 이어 말하기
# delete부분. 
# 2. 파일 자체 삭제하기

import os
if os.path.exists("lyrics.txt"):
    os.remove("lyrics.txt")
    print("lyrics.txt 파일이 삭제되었습니다.")
else:
    print("lyrics.txt 파일이 존재하지 않습니다.")


