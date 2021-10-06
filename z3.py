import random
import numpy as np
from itertools import groupby
random.seed(23)#Зерно
a=[random.randint(100,999) for i in range(50)]
np.array(a)
CHPE=1
#################!!!!!!ЧИСЛО ЗНАЧИТ,ЧТО НУЖНО УДАЛИТЬ СТОБЕЦ В КОТОРОМ ЭЛЕМЕНТ ИМЕЕТ СТОЛЬКО ПРОСТЫХ ДЕЛИТЕЛых!
massive=np.reshape(a,(5,10))
print("двумерный масси\n",massive)
dely=[]
strofcol=[]
for n in range(len(massive)):
    for m in range(len(massive[n])):
        k=massive[n][m]
        st=[]
        print("Делители числа %d:"%k)
        for i in range(k - 1, 1, -1):
            is_simple = 0 # Счётчик
            if (k % i == 0):
                for j in range(i - 1, 1, -1):
                    if (i % j == 0):
                        is_simple = is_simple + 1 # Увеличиваем, если находим делитель
                if (is_simple == 0): # Если делителей не было найдено, выводим
                    st.append(i)
        if len(st)==CHPE: 
            strofcol.append(m)
        print(st)
        print("Число простых делителей = ",len(st))
        print("\n")
   
        st=[]

sc=list(set(strofcol))
print("столбцы для удаления",sc)
massive=np.delete(massive,sc,1)
print(massive)
        








































