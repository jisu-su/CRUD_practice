# 저번 시간에 적어본 crud 수동을 자동으로 적어보기
# 오늘의 주제는 노래 가사 이어 말하기
# update 부분. "a", "r" 모드로 추가해보기
# 1. "a" 모드로 추가

with open("lyrics.txt", "a", encoding="utf-8") as file:
    file.write("\nhands talk won't stop we go to war")
    file.write("\nin the heat of the moment you think that we're broken")
    file.write("\ni could see my whole life with you baby")
