import random
from collections import Counter
random.seed(23)#Зерно
list_data=[]
data = [random.randint(pow(10,4),pow(10,5)) for i in range(0, 5)]
print("Cформированные 5 чисел:", data,"\n")
print("Числа, имеющие 2 одинаковых цифры:")
for i in range(len(data)):
	c=Counter(str(data[i]))
	c=dict(c)
	#print(c)
	if 2 in c.values():
		print(data[i])
	
		
	
#print(data)














# Symbol = ["о", "О","o", "O" ]
# with open ("C.txt", "r") as myfile:
#     data = myfile.read().replace('\n', '')
#     print(data)
#     freq = 0
#     for char in data:
#         if char == Symbol:
#             freq = freq + 1
#     print(freq)
