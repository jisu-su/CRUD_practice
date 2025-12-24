# update. 'a'랑 'w' 둘 다 사용해보자.
# 'a'는 뒤에 추가하는 방식. append
# 'w'는 덮어쓰기 write

file = open("instructor.txt", "a", encoding="utf-8")
file.write("\n영어학습어플에서도 미남이라서 신기했습니다")
file.close()