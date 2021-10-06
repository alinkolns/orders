import re
def deleteContent(pfile):
    pfile.seek(0)
    pfile.truncate()
    f.write(a)
f=open(r"C:\Users\user\desktop\C.txt", "r+" ,encoding='Utf-8')
data=f.read()
print(data)
words=data.split()
count=0
for i in words:
	if "о" in i or "О" in i or "O" in i or "o" in i:
		count+=1
print("\nКоличество слов с буквой 'o':",count)
my_regex = "\'.*\'|\<.*\>"
a=re.sub(my_regex,"",data)
print(a)
deleteContent(f)

f.close()