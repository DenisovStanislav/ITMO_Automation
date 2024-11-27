"""
5. папка python_trening
Создайте файл task_9_checks.py
a. создайте класс Checks, принимающий 1 аргумент при инициализации (loc)
b. создайте для него метод check_text, метод возвращает self.loc
в файле task_9_oop_1.py
c. наследуйте все классы от класса Checks
i. чтобы использовать класс из другого файла его нужно импортировать
from название файла(без расширения) import название класса
d. переделайте все 4 класса в файле task_9_oop_1.py так
 чтоб в объектах можно было использовать методы родительского класса
e. распечатайте в консоль результаты метода .check_text()
вызванного от каждого объекта классов файла task_9_oop_1.py
"""

# импортируем класс Checks из файла task_9_checks
from python_trening.task_9_checks import Checks
# создаем метод check_text
def check_text(self):
    return f'\n Клик по локатору - {self.loc}'
# Создаем экземпляр Класса
check_txt=Checks(' Контрольный текст ')
# Вызываем метод
print(check_txt.check_text())


# from xml.sax.xmlreader import Locator
# импортируем класс Checks из файла task_9_checks
# from python_trening.task_9_checks import Checks
# Пример 1 - Создаем класс
class Button(Checks):
    def __init__(self,text,link):
        self.text = text
        self.link = link
        super().__init__(loc=None)

# Создаем экземпляр класса Button
home=Button('Домой','/home')
catalog_msk=Button('Каталог','/msk/catalog')

# Получаем доступ к атрибутам
#print('\n',home.text)
#print('\n Кнопка "'+home.text+'" имеет ссылку: '+home.link)
#print('\n',catalog_msk.text)
#print('\n Кнопка "'+catalog_msk.text+'" имеет ссылку: '+catalog_msk.link)
print('\nВызываем метод check_text в классе Button(Checks): ',home.check_text())


# Пример 2 - создаем класс
class ButtonTwo(Checks):
    def __init__(self,text,link,loc):
        self.text = text
        self.link = link
        self.loc = loc
        super().__init__(loc=None)
    def click(self):
        return '\n Клик по локатору - {}'.format(self.loc)
# Создаем экземпляр Класса
home_two=ButtonTwo('\n Домой_2 ','/home','Button#home')
# Вызываем метод
#print(home_two.click())
print('\nВызываем метод check_text в классе ButtonTwo(Checks): ',home_two.check_text()*2)

# Практическая задача - создание класса Input, принимающего один аргумент Loc при инициализации
# создание объекта Search, т.е. экземпляра класса Input
# выведение на Консоль значения аргумента Loc объекта Search
class Input(Checks):
    def __init__(self,Loc):
        self.Loc=Loc
        super().__init__(loc=None)

# Создаем экземпляр Класса
Search=Input('\n Input#Search-Input(Checks)')
# Вызываем метод
#print(Search.Loc)
print('\nВызываем метод check_text в классе Input(Checks): ',Search.check_text())

# Практическая задача 1* - Добавить к Классу Input атрибут Объекта text
# создать три Класса - Button, Title, Link, для каждого из которых создать
# произвольные Объекты с произвольными данными
# вывести на Консоль text и loc каждого Класса
class Input2(Checks):
    def __init__(self,Loc, Text):
        self.Loc=Loc
        self.Text=Text
        super().__init__(loc=None)

# Создаем экземпляр Класса
Object_1=Input2('\n Loc_Input2#Object_1','Text_Input2#Object_1 - класс Input2(Checks)')
# Вызываем метод
#print('\n',Object_1.Loc)
#print('\n',Object_1.Text)
#print('\n Loc_Input2#Object_1: '+Object_1.Loc+'\n Text_Input2#Object_1: '+Object_1.Text)
print('\nВызываем метод check_text в классе Input2(Checks): ',Object_1.check_text()*2)

class Button2(Checks):
    def __init__(self,text,loc):
        self.text=text
        self.loc = loc
        super().__init__(loc=None)

# Создаем экземпляр Класса
Object_2=Button2('\n text_Button2#Object_2','loc_Button2#Object_2')
# Вызываем метод
# print('\n text_Button2#Object_2: '+Object_2.text+'\n loc_Button2#Object_2: '+Object_2.loc)
print('\nВызываем метод check_text в классе Button2(Checks): ',Object_2.check_text()*3)
class Title(Checks):
    def __init__(self,text,loc):
        self.text=text
        self.loc = loc
        super().__init__(loc=None)

# Создаем экземпляр Класса
Object_3=Title('\n text_Title#Object_3','loc_Title#Object_3')
# Вызываем метод
# print('\n text_Title#Object_3: '+Object_3.text+'\n loc_Title#Object_3: '+Object_3.loc)
print('\nВызываем метод check_text в классе Title(Checks): ',Object_3.check_text()*3)
class Link(Checks):
    def __init__(self,text,loc):
        self.text=text
        self.loc = loc
        super().__init__(loc=None)

# Создаем экземпляр Класса
Object_4=Link('\n text_Link#Object_4','loc_Link#Object_4')
# Вызываем метод
# print('\n text_Link#Object_4: '+Object_4.text+'\n loc_Link#Object_4: '+Object_4.loc)
print('\nВызываем метод check_text в классе Link(Checks): ',Object_4.check_text()*4)
# Задача 2 - создать Класс Page с одним Аргументом url при инициировании
# реализовать Метод get(), который выводит на печать url
# создать Объект home и вызвать Метод get()
class Page(Checks):
    def __init__(self,url):
        self.url=url
        super().__init__(loc=None)

    def get(self):
            print('\n Адрес: ',self.url)
# Создаем экземпляр Класса
home = Page('\n /alisa.ru')
    # Вызываем метод
home.get()
# Создаем экземпляр Класса
Object_5=Page(' \n url_Link#Object_5 ')
# Вызываем метод
# print('\n url_Link#Object_5: '+Object_5.url)
print('\nВызываем метод check_text в классе Page(Checks): ',Object_5.check_text()*5)

# Создание Класса Soda
class Soda(Checks):
    def __init__(self,top=None):
        self.top=top
        super().__init__(loc=None)

    # Реализация Метода show_my_drink
    def show_my_drink(self):
        if self.top:
            print(f'\nГазировка и {self.top}')
        else:
            print('\nОбычная газировка')

# Апробация Класса Soda
# my_drink=Soda(str(input('Какую газированную воду предпочитаете: Крем-сода, Апельсин, Дюшес, Обычная газировка? ')))
# my_drink1=Soda('Крем-сода')
# my_drink2=Soda()

#my_drink.show_my_drink()
# my_drink1.show_my_drink()
# my_drink2.show_my_drink()
# Создаем экземпляр Класса
Object_6=Soda(' \n тест для определения типа газированной воды')
# Вызываем метод
# print('\n url_Link#Object_5: '+Object_6.top)
print('\n Вызываем метод check_text в классе Soda(Checks): ',Object_6.check_text()*2)

"""
Создать файл task_9_inheritance.py, записать код и запустить

# Создать Класс "Млекопитающие"
class Mammal:
    className='Млекопитающие'
# Создать Подкласс
class Dog(Mammal):
    species='Canis Lupus'
dog=Dog()
print(dog.className) # Млекопитающие




Создать файл task_9_super.py, записать код и запустить

# Создать Класс "A"
class A:
    def __init__(self):
        self.x=10
# Создать Класс "B"
class B(A):
    def __init__(self):
        super().__init__()
        self.y = self.x+5
print(B().x)
b=B()
print(b.y)


"""


