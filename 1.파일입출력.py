# file=open("test.txt","w",encoding="utf-8")
# file.write("안녕하세요")
# file.close()

# with open("test.txt","w",encoding="utf-8")as file:
# 	file.write("안녕하세요")

with open("test.txt","r",encoding="utf-8")as file:
	lines=file.readlines()

print(lines)