# update. 'a'랑 'w' 둘 다 사용해보자.
# 'a'는 뒤에 추가하는 방식. append
# 'w'는 덮어쓰기 write

file = open("instructor.txt", "r", encoding="utf-8")
content = file.read()
file.close()
print(content)