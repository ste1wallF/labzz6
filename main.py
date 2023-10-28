import numpy as np
while True:

    try:
        numcra = int(input("Введите кол-во критериев: "))
        break
    except ValueError:
        print('Неверное значение')

matri_s = np.eye(numcra)
        #Этап создания первой матрицы
        #после, заполнение коэфф. сравнения
a = 1   
        #считаем пропуски заполненных значений
for i in range(a, numcra+1):
    for j in range(a+1, numcra+1):
        
        while True:
            try:
                        #каждый элемент строки матрицы заполняется
                matri_s[i-1][j-1] = round(float(input('Введите сравнение К{0}-К{1}:'.format(i, j))), 3)
                break
            except ValueError:
                print('Неверное значение')
                        # ячейки обратного отношения (К1-К2 -> К2-К1)
        matri_s[j-1][i-1] = round(matri_s[i-1][j-1]**(-1), 2)
    a += 1
                        # список сумм строки
sum_list = [round(sum(j),2) for j in matri_s]
list_back = [round(n/sum(sum_list), 2) for n in sum_list]

if (sum(list_back)) != 1.0:
    index = list_back.index(max(list_back))
    k = (sum(list_back)) - 1.0
    list_back[index] -= k

print('Весовые коэффициенты')

for ind in list_back:
    print(ind, end=' ')
