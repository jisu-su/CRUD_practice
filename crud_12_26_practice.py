# 저번 시간에 적어본 crud 수동을 자동으로 적어보기
# 오늘의 주제는 노래 가사 이어 말하기
# update 부분. "a", "r" 모드로 추가해보기
# 1. "a" 모드로 추가

with open("lyrics.txt", "r", encoding="utf-8") as file:
    lyrics_data = file.read()
    print(lyrics_data)