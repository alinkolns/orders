import random
import numpy as np

random.seed(23)#Зерно

m, n = 5, 10
a = [[random.randint(100, 999) for j in range(m)] for i in range(n)]
a=np.array(a)

print(a)


def delit(a):
    res = []
    i = 2
    # цикл до квадратного корня из "а"
    # больше этого без остатка не делится, если только ...
    # (об этом ниже)
    while i * i < a + 1:
        # если при делении остаток = 0, то добавляем "i" в список
        if a % i == 0:
            res.append(i)
            # теперь делим исходное число на "i", пока не появится остаток
            while a % i == 0:
                a //= i
        # берем следующее "i"
        i += 1
    # если в конце "а" не равно единице, то значит остался один(!)
    # делитель, больший кв. корня из исходного "а"
    # добавляем в список
    if a != 1:
        res.append(a)
    return res


print(delit(int(input())))