# 저번 시간에 적어본 crud 수동을 자동으로 적어보기
# 오늘의 주제는 노래 가사 이어 말하기
# delete부분. 
# 1. 특정 줄 삭제하기

with open("lyrics.txt", "r", encoding="utf-8") as file:
    lines = file.readlines()

if len(lines) > 2: # 혹시 줄이 없을 때를 대비한 안전장치
    del lines[2] 

with open("lyrics.txt", "w", encoding="utf-8") as file:
    file.writelines(lines)  