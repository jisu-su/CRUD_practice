# Read 차례. 이제는 메세지를 읽어볼 거다

file = open("instructor.txt", "r", encoding="utf-8")
content = file.read()
print(content)
file.close()