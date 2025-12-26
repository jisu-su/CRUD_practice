# 저번 시간에 적어본 crud 수동을 자동으로 적어보기
# 오늘의 주제는 노래 가사 이어 말하기
# update 부분. "a", "r" 모드로 추가해보기
# 1. "w" 모드로 다른 가사 적기

with open("lyrics.txt", "w", encoding="utf-8") as file:
    file.write("아무 일 없던 것처럼 이 모든 게 난 다 꿈일 거리고")
    file.write("눈을 다시 감고 떴을 땐 안심하며 꺨 아침이길 바랬어")
    file.write("어긋나 버린 우리 미래에 시간을 거슬러 갈 수 있다면")
    file.write("거칠기보단 따뜻하게 널 부르며 보내줄 수 없을까")