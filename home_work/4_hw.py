"""
1. создайте класс прямоугольника.
a. атрибуты - прямоугольнику можно задать ширину и высоту
b. методы - реализуйте 2 метода:
i. расчет площади прямоугольника
ii. расчет периметра прямоугольника
c. создайте 3 объекта, рассчитайте площадь и периметр для каждого.
Результаты выводить в консоль.
"""
# Создаем класс "прямоугольник"
class Rectangle:
    # Создаем атрибуты в классе "прямоугольник"
    def __init__(self,width,height):
        self.width=width # Ширина прямоугольника
        self.height=height # Длина прямоугольника
# Создаем экземпляр класса "прямоугольник №1"
Rec1=Rectangle(input('\nУкажите ширину прямоугольника №1 (целое число ед.): '),input('\nУкажите длину прямоугольника №1 (целое число ед.): '))
# Реализуем методы: - 1) расчет площади прямоугольника 2) расчет периметра прямоугольника
print(f'\nПлощадь прямоугольника №1 шириной {Rec1.width} ед. и длиной {Rec1.height} ед. равна: ',int(Rec1.width)*int(Rec1.height),'кв.ед.')
print(f'\nПериметр прямоугольника №1 шириной {Rec1.width} ед. и длиной {Rec1.height} ед. равен: ',(int(Rec1.width)+int(Rec1.height))*2,'ед.')
# Создаем экземпляр класса "прямоугольник №2"
Rec2=Rectangle(input('\nУкажите ширину прямоугольника №2 (целое число ед.): '),input('\nУкажите длину прямоугольника №2 (целое число ед.): '))
# Реализуем методы: - 1) расчет площади прямоугольника 2) расчет периметра прямоугольника
print(f'\nПлощадь прямоугольника №2 шириной {Rec2.width} ед. и длиной {Rec2.height} ед. равна: ',int(Rec2.width)*int(Rec2.height),'кв.ед.')
print(f'\nПериметр прямоугольника №2 шириной {Rec2.width} ед. и длиной {Rec2.height} ед. равен: ',(int(Rec2.width)+int(Rec2.height))*2,'ед.')
# Создаем экземпляр класса "прямоугольник №3"
Rec3=Rectangle(input('\nУкажите ширину прямоугольника №3 (целое число ед.): '),input('\nУкажите длину прямоугольника №3 (целое число ед.): '))
# Реализуем методы: - 1) расчет площади прямоугольника 2) расчет периметра прямоугольника
print(f'\nПлощадь прямоугольника №3 шириной {Rec3.width} ед. и длиной {Rec3.height} ед. равна: ',int(Rec3.width)*int(Rec3.height),'кв.ед.')
print(f'\nПериметр прямоугольника №3 шириной {Rec3.width} ед. и длиной {Rec3.height} ед. равен: ',(int(Rec3.width)+int(Rec3.height))*2,'ед.')

"""
2. Создайте класс Math.
a. Создайте два атрибута — a и b.
b. Напишите методы
i. addition — сложение,
ii. multiplication — умножение,
iii. division — деление,
iv. subtraction — вычитание.
При передаче в методы параметров a и b с ними нужно 
производить соответствующие действия и печатать ответ.
"""

#Вариант 1 - Примитивный
# Создаем класс Math
class Math:
    # Создаем атрибуты в классе Math
    def __init__(self,a,b):
        self.a=a # Число а
        self.b=b # Число b
# Создаем экземпляр класса Math
addition=Math(1,2)
multiplication=Math(3,4)
division=Math(9,3)
subtraction=Math(10,1)

# Реализуем методы: 1) Сложение 2) Умножение 3) Деление 4) Вычитание
print('\nОТВЕТ:\n')
print(f'\nРезультат сложения числа {addition.a} с числом {addition.b} равен: ',addition.a+addition.b)
print(f'\nРезультат умножения числа {multiplication.a} на число {multiplication.b} равен: ',multiplication.a*multiplication.b)
print(f'\nРезультат деления числа {division.a} на число {division.b} равен: ',division.a/division.b)
print(f'\nРезультат вычитания из числа {subtraction.a} числа {subtraction.b} равен: ',subtraction.a-subtraction.b)


# Вариант 2 - Красивый
# Создаем класс Math
class Math:
    # Создаем атрибуты в классе Math
    def __init__(self,a,b,c):
        self.a=a # Число а
        self.b=b # Число b
        self.c=c # Математическое действие
# Создаем экземпляр класса Math
Calc=Math(float(input('\nВведите первое произвольное число: ')),float(input('\nВведите второе произвольное число: ')),input('\nУкажите математическое действие:\n1-Сложение\n2-Умножение\n3-Деленине\n4-Вычитание :'))
# Реализуем методы: 1) Сложение 2) Умножение 3) Деление 4) Вычитание
print('\nОТВЕТ:\n')
if Calc.c=='1':
    print(f'\nРезультат сложения числа {Calc.a} с числом {Calc.b} равен: ',Calc.a+Calc.b)
elif Calc.c=='2':
    print(f'\nРезультат умножения числа {Calc.a} на число {Calc.b} равен: ',Calc.a*Calc.b)
elif Calc.c=='3':
    print(f'\nРезультат деления числа {Calc.a} на число {Calc.b} равен: ',Calc.a/Calc.b)
elif Calc.c=='4':
    print(f'\nРезультат вычитания из числа {Calc.a} числа {Calc.b} равен: ',Calc.a-Calc.b)
else:
    print('\nВведено недопустимое математическое действие')


"""
3. откройте страницу https://demoqa.com/text-box
На странице присутствует сайдбар (меню слева)
a. Создайте объекты для каждой кнопки 2-го уровня вложенности (“Text Box” и т.п.)
Для этого опишите класс.
Каждый объект должен содержать в себе:
- текст кнопки (пример: “Text Box”)
- тип - одинаковый для всех “Кнопка”
- локатор - не заполнять, сделать по умолчанию пустой строкой
Также на кнопку можно нажать - реализуйте метод. Метод возвращает текст “Клик по кнопке { ТЕКСТ КНОПКИ }”
b. выведите текст для каждой кнопки
c. вызовите “Клик” для каждой кнопки
"""
# создаем класс
class ButtonSideBar:
    def __init__(self,text,type,loc):
        self.text = text
        self.type = type
        self.loc = loc
    def click(self):
        return '\n Кликните по кнопке - {}'.format(self.loc)
# Создаем экземпляр Класса
#Elements
TextBox=ButtonSideBar('\n Text Box ','Кнопка','Text Box')
CheckBox=ButtonSideBar('\n Check Box ','Кнопка','Check Box')
RadioButton=ButtonSideBar('\n Radio Button ','Кнопка','Radio Button')
WebTables=ButtonSideBar('\n Web Tables ','Кнопка','Web Tables')
Buttons=ButtonSideBar('\n Buttons ','Кнопка','Buttons')
Links=ButtonSideBar('\n Links ','Кнопка','Links')
BrokenLinksImages=ButtonSideBar('\n Broken Links - Images ','Кнопка','Broken Links - Images')
UploadDownload=ButtonSideBar('\n Upload and Download ','Кнопка','Upload and Download')
DynamicProperties=ButtonSideBar('\n Dynamic Properties ','Кнопка','Dynamic Properties')
#Forms
PracticeForm=ButtonSideBar('\n Practice Form ','Кнопка','Practice Form')
#Alerts, Frame & Windows
BrowserWindows=ButtonSideBar('\n Browser Windows ','Кнопка','Browser Windows')
Alerts=ButtonSideBar('\n Alerts ','Кнопка','Alerts')
Frames=ButtonSideBar('\n Frames ','Кнопка','Frames')
NestedFrames=ButtonSideBar('\n Nested Frames ','Кнопка','Nested Frames')
ModalDialogs=ButtonSideBar('\n Modal Dialogs ','Кнопка','Modal Dialogs')
#Widgets
Accordian=ButtonSideBar('\n Accordian ','Кнопка','Accordian')
AutoComplete=ButtonSideBar('\n Auto Complete ','Кнопка','Auto Complete')
DatePicker=ButtonSideBar('\n Date Picker ','Кнопка','Date Picker')
Slider=ButtonSideBar('\n Slider ','Кнопка','Slider')
ProgressBar=ButtonSideBar('\n Progress Bar ','Кнопка','Progress Bar')
Tabs=ButtonSideBar('\n Tabs ','Кнопка','Tabs')
ToolTips=ButtonSideBar('\n Tool Tips ','Кнопка','Tool Tips')
Menu=ButtonSideBar('\n Menu ','Кнопка','Menu')
SelectMenu=ButtonSideBar('\n Select Menu ','Кнопка','Select Menu')
#Interactions
Sortable=ButtonSideBar('\n Sortable ','Кнопка','Sortable')
Selectable=ButtonSideBar('\n Selectable ','Кнопка','Selectable')
Resizable=ButtonSideBar('\n Resizable ','Кнопка','Resizable')
Droppable=ButtonSideBar('\n Droppable ','Кнопка','Droppable')
Dragabble=ButtonSideBar('\n Dragabble ','Кнопка','Dragabble')
#Book Store Application
Login=ButtonSideBar('\n Login ','Кнопка','Login')
BookStore=ButtonSideBar('\n Book Store ','Кнопка','Book Store')
Profile=ButtonSideBar('\n Profile ','Кнопка','Profile')
BookStoreAPI=ButtonSideBar('\n Book Store API ','Кнопка','Book Store API')
# Вызываем метод
#Elements
print(TextBox.text,TextBox.click())
TextBox.click()
print(CheckBox.text,CheckBox.click())
CheckBox.click()
print(RadioButton.text,RadioButton.click())
RadioButton.click()
print(WebTables.text,WebTables.click())
WebTables.click()
print(Buttons.text,Buttons.click())
Buttons.click()
print(Links.text,Links.click())
Links.click()
print(BrokenLinksImages.text,BrokenLinksImages.click())
BrokenLinksImages.click()
print(UploadDownload.text,UploadDownload.click())
UploadDownload.click()
print(DynamicProperties.text,DynamicProperties.click())
DynamicProperties.click()
#Forms
print(PracticeForm.text,PracticeForm.click())
PracticeForm.click()
#Alerts, Frame & Windows
print(BrowserWindows.text,BrowserWindows.click())
BrowserWindows.click()
print(Alerts.text,Alerts.click())
Alerts.click()
print(Frames.text,Frames.click())
Frames.click()
print(NestedFrames.text,NestedFrames.click())
NestedFrames.click()
print(ModalDialogs.text,ModalDialogs.click())
ModalDialogs.click()
#Widgets
print(Accordian.text,Accordian.click())
Accordian.click()
print(AutoComplete.text,AutoComplete.click())
AutoComplete.click()
print(DatePicker.text,DatePicker.click())
DatePicker.click()
print(Slider.text,Slider.click())
Slider.click()
print(ProgressBar.text,ProgressBar.click())
ProgressBar.click()
print(Tabs.text,Tabs.click())
Tabs.click()
print(ToolTips.text,ToolTips.click())
ToolTips.click()
print(Menu.text,Menu.click())
Menu.click()
print(SelectMenu.text,SelectMenu.click())
SelectMenu.click()
#Interactions
print(Sortable.text,Sortable.click())
Sortable.click()
print(Selectable.text,Selectable.click())
Selectable.click()
print(Resizable.text,Resizable.click())
Resizable.click()
print(Droppable.text,Droppable.click())
Droppable.click()
print(Dragabble.text,Dragabble.click())
Dragabble.click()
#Book Store Application
print(Login.text,Login.click())
Login.click()
print(BookStore.text,BookStore.click())
BookStore.click()
print(Profile.text,Profile.click())
Profile.click()
print(BookStoreAPI.text,BookStoreAPI.click())
BookStoreAPI.click()

"""
Черновые материалы к задаче
******************************************************************************************
TextBox=ButtonSideBar('\n Text Box ','Кнопка','Button#TextBox')
CheckBox=ButtonSideBar('\n Check Box ','Кнопка','Button#CheckBox')
RadioButton=ButtonSideBar('\n Radio Button ','Кнопка','Button#RadioButton')
WebTables=ButtonSideBar('\n Web Tables ','Кнопка','Button#WebTables')
Buttons=ButtonSideBar('\n Buttons ','Кнопка','Button#Buttons')
Links=ButtonSideBar('\n Links ','Кнопка','Button#Links')
BrokenLinksImages=ButtonSideBar('\n Broken Links - Images ','Кнопка','Button#BrokenLinksImages')
UploadDownload=ButtonSideBar('\n Upload and Download ','Кнопка','Button#UploadDownload')
DynamicProperties=ButtonSideBar('\n Dynamic Properties ','Кнопка','Button#DynamicProperties')
 
print(TextBox.text, TextBox.click())
print(CheckBox.text, CheckBox.click())
print(RadioButton.text, RadioButton.click())
print(WebTables.text, WebTables.click())
print(Buttons.text, Buttons.click())
print(Links.text, Links.click())
print(BrokenLinksImages.text, BrokenLinksImages.click())
print(UploadDownload.text, UploadDownload.click())
print(DynamicProperties.text, DynamicProperties.click())
**************************************************************************************
"""


"""
4. В отдельном файле напишите программу с классом Car.
a. Создайте конструктор класса Car. 
Создайте атрибуты класса Car — color (цвет), type (тип), year (год).
b. Напишите пять методов.
i. Первый — запуск автомобиля, при его вызове выводится сообщение «Автомобиль заведен».
ii. Второй — отключение автомобиля — выводит сообщение «Автомобиль заглушен».
iii. Третий — присвоение автомобилю года выпуска. 
Четвертый метод — присвоение автомобилю типа.
iv. Пятый — присвоение автомобилю цвета.
"""
# создаем класс
class Car:
    def __init__(self,color=None,type=None,year=None):
        self.color = color
        self.type = type
        self.year = year
# Создаем методы Класса
    def StartCar(self): # 1 - запуск автомобиля
        print('\n«Автомобиль заведен»')
    def StopCar(self): # 2 - отключение автомобиля
        print('\n«Автомобиль заглушен»')
    def YearCar(self): # 3 - присвоение автомобилю года выпуска
        #print('\nУкажите год выпуска Автомобиля:')
        if self.year:
            print(f'\nГод выпуска Автомобиля: {self.year}')
        else:
            print('\nГод выпуска Автомобиля не присвоен')
    def TypeCar(self): # 4 - присвоение автомобилю типа
        #print('\nУкажите год выпуска Автомобиля:')
        if self.type:
            print(f'\nТип Автомобиля: {self.type}')
        else:
            print('\nТип Автомобиля не присвоен')
    def ColorCar(self):  # 5 - присвоение автомобилю цвета
        #print('\nУкажите цвет Автомобиля:')
        if self.color:
            print(f'\nЦвет Автомобиля: {self.color}')
        else:
            print('\nЦвет Автомобиля не присвоен')

my_StartCar=Car()
my_StartCar.StartCar()
my_StopCar=Car()
my_StopCar.StopCar()
my_YearCar=Car(None ,None, input('\nУкажите год выпуска Автомобиля:'))
my_YearCar.YearCar()
my_TypeCar=Car(None, input('\nУкажите тип Автомобиля:'), None)
my_TypeCar.TypeCar()
my_ColorCar=Car(input('\nУкажите цвет Автомобиля:'))
my_ColorCar.ColorCar()



"""
5. папка python_trening
Создайте файл task_9_checks.py
a. создайте класс Checks, принимающий 1 аргумент при инициализации (loc)
b. создайте для него метод check_text, метод возвращает self.loc
в файле task_9_oop_1.py
c. наследуйте все классы от класса Checks
i. чтобы использовать класс из другого файла его нужно импортировать
from название файла(без расширения) import название класса
d. переделайте все 4 класса в файле task_9_oop_1.py так чтоб в объектах можно было использовать методы родительского класса
e. распечатайте в консоль результаты метода .check_text() вызванного от каждого объекта классов файла task_9_oop_1.py
"""

