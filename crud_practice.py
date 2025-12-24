# update. 'a'랑 'w' 둘 다 사용해보자.
# 'a'는 뒤에 추가하는 방식. append
# 'w'는 덮어쓰기 write

file = open("instructor.txt", "w", encoding="utf-8")
file.write("공미남 너무 잘 어울려요^^")
file.close()