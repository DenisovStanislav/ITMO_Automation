"""
2. Функция на вход получает два произвольных числа.
Вывести в консоль наибольшее из чисел.
"""
def comparator(num_1:int=0, num_2:int=0):
    num_1=(int(input('\n Введите первое произвольное целое число:')))
    num_2 = (int(input('\n Введите второе произвольное целое число:')))
    if num_1>num_2:
        print('\n ', num_1, ' это наибольшее число из двух введенных')
    elif num_1<num_2:
        print('\n ', num_2, ' это наибольшее число из двух введенных')
    else:
        print('\n Введены одинаковые числа')
comparator()

"""
3. Функция на вход получает два произвольных числа. 
Вывести в консоль “yes”, если они отличаются друг от друга на 135, 
иначе вывести на экран “No”
"""
def delta_135(num_1:int=0, num_2:int=0):
    num_1=(int(input('\n Введите первое произвольное целое число:')))
    num_2 = (int(input('\n Введите второе произвольное целое число:')))
    if num_1-num_2==135 or num_2-num_1==135:
        print('\n YES')
    else:
        print('\n NO')
delta_135()
"""
4. Функция на вход получает произвольное число от 1 до 12 (номер месяца). 
Вывести название сезона года в консоль (зима, весна, лето, осень)

"""
def sezon(num_2:int=0):
    num_2=(int(input('\n Введите номер месяца:')))
    if num_2==1 or num_2==2 or num_2==12:
        print('\n ЗИМА')
    elif 2<num_2<6:
        print('\n ВЕСНА')
    elif 6<=num_2<=8:
        print('\n ЛЕТО')
    elif 9<=num_2<=11:
        print('\n ОСЕНЬ')
    else:
        print('\n Введен некорректный номер месяца')
sezon()


"""

5. Функция на вход получает три произвольных числа. 
Если все числа больше 10, то вывести на экран “yes”, иначе “no”;

"""
def trio_compare(num_1:int=0,num_2:int=0,num_3:int=0):
    num_1=(int(input('\n Введите первое произвольное целое число:')))
    num_2 = (int(input('\n Введите второе произвольное целое число:')))
    num_3 = (int(input('\n Введите третье произвольное целое число:')))

    if num_1>10 and num_2>10 and num_3>10:
        print('\n YES')
    else:
        print('\n NO')
trio_compare()

"""

6. Функция на вход получает список, состоящий из 5 произвольных чисел. 
Найти количество положительных чисел среди них.

"""
def count_positiv(lst_1:list=[0,0,0,0,0]):
    lst_1[0]=(int(input('\n Введите первое произвольное целое число:')))
    lst_1[1]= (int(input('\n Введите второе произвольное целое число:')))
    lst_1[2]= (int(input('\n Введите третье произвольное целое число:')))
    lst_1[3]= (int(input('\n Введите четвертое произвольное целое число:')))
    lst_1[4]= (int(input('\n Введите пятое произвольное целое число:')))
    print('Вы ввели список: ',lst_1)
    count = 0
    count = sum(True for elem in lst_1 if elem > 0)
    return print('Количество положительных элементов списка равно: ', count)
count_positiv()
"""
    for elem in lst_1:
        if elem>0:
            count+=1
"""

                 #len([elem for elem in lst_1 if elem > 0]))





"""

7. Функция на вход получает 2 переменные.
a. Кол-во лет (int)
b. Кол-во месяцев (int)
Вывести в консоль количество дней за это время. Считать, что в каждом месяце 29 дней.
"""
def day_count(num_1:int=0,num_2:int=0):
    num_1=(int(input('\n Введите произвольное количество лет:')))
    num_2 = (int(input('\n Введите произвольное количество месяцев:')))
    return print('В указанном периоде содержится ',(num_1*12+num_2)*29,' дней')
day_count()

