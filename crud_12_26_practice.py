# 저번 시간에 적어본 crud 수동을 자동으로 적어보기
# 오늘의 주제는 노래 가사 이어 말하기
# create 부분. file = open 이 아닌 with -as - 사용해보기

with open("lyrics.txt", "w", encoding="utf-8") as file:
    file.write("late night your eyes fell to tme floor\n")
    file.write("i'm trying to make sense but you're losing your patience")
