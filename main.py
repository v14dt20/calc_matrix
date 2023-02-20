# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'calc.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


import random
from program import *
from PyQt5 import Qt, QtCore, QtGui, QtWidgets

matrix1 = []
matrix2 = []
f = open("about.txt", 'r', encoding="utf-8") #файл со справкой

class Window2(QtWidgets.QMainWindow):#окно справки
    def __init__(self):
        super(Window2, self).__init__()
        self.setWindowTitle('Window2')
        self.resize(800, 600)

        self.label = QtWidgets.QLabel(self)
        self.label.setGeometry(QtCore.QRect(10, 10, 600, 800))
        self.label.setAlignment(QtCore.Qt.AlignLeft)
        self.label.setText(f.read())
        self.label.setObjectName("label")
        self.label.show()

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        #self.layout = QtWidgets.QVBoxLayout(self.centralwidget)

        self.scrollArea = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollArea.setGeometry(QtCore.QRect(10, 100, 780, 490))
        #self.layout.addWidget(self.scrollArea)

        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 780, 490))
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        #self.layout = QtWidgets.QHBoxLayout(self.scrollAreaWidgetContents)

        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(10, 70, 75, 23))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(100, 70, 75, 23))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(190, 70, 91, 23))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(290, 70, 111, 23))
        self.pushButton_4.setObjectName("pushButton_4")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 10, 171, 16))
        self.label.setObjectName("label")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(190, 10, 61, 20))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(260, 10, 61, 20))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_3.setGeometry(QtCore.QRect(190, 40, 61, 20))
        self.lineEdit_3.setText("")
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.lineEdit_4 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_4.setGeometry(QtCore.QRect(260, 40, 61, 20))
        self.lineEdit_4.setText("")
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(10, 40, 171, 16))
        self.label_2.setObjectName("label_2")
        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_5.setGeometry(QtCore.QRect(330, 40, 75, 23))
        self.pushButton_5.setObjectName("pushButton_5")
        self.about = QtWidgets.QPushButton(self.centralwidget) #кнопка справки
        self.about.setGeometry(QtCore.QRect(450, 40, 70, 20))
        self.about.setText("Справка")
        self.about.setObjectName("about")
        self.exit = QtWidgets.QPushButton(self.centralwidget) #кнопка справки
        self.exit.setText("Выход")
        self.exit.setGeometry(QtCore.QRect(450, 70, 70, 20))
        self.exit.setObjectName("exit")
        self.random = QtWidgets.QPushButton(self.centralwidget)
        self.random.setText("Рандом")
        self.random.setGeometry(QtCore.QRect(550, 70, 70, 20))
        self.random.setObjectName("random")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.mass1 = [] #массив полей ввода для элементов первой матрицы
        self.mass2 = [] #массив полей ввода для элементов второй матрицы
        self.ans = QtWidgets.QLabel(self.scrollAreaWidgetContents) #ответ
        self.ans.setText("Ответ:")
        self.ans.setFixedHeight(30)
        self.ans.setFixedWidth(100)
        self.ans.hide()
        self.ans_2 = QtWidgets.QLabel(self.scrollAreaWidgetContents) #ответ 2
        self.ans_2.setText("Ответ:")
        self.ans_2.setFixedHeight(30)
        self.ans_2.setFixedWidth(100)
        self.ans_2.hide()
        self.ans_matrix = [] #ответ матрица
        self.ans_matrix_2 = [] #ответ вторая матрица
        self.pushButton_5.clicked.connect(lambda: self.create_matrix(self.lineEdit.text(), self.lineEdit_2.text(), self.lineEdit_3.text(), self.lineEdit_4.text())) #обработчик нажатий на кнопку "создать"
        self.pushButton_3.clicked.connect(lambda: self.det(self.mass1, self.mass2)) #обработчик нажатий для кнопки "определитель"
        self.pushButton.clicked.connect(lambda: self.plus(self.mass1, self.mass2)) #обработчик нажатий для кнопки "сложение"
        self.pushButton_2.clicked.connect(lambda: self.mult(self.mass1, self.mass2)) #обработчик нажатий для кнопки "произведение"
        self.pushButton_4.clicked.connect(lambda: self.obr(self.mass1, self.mass2)) #обработчик нажатий для кнопки "Обратная матрица"
        self.exit.clicked.connect(lambda: self.btnClosed())#обработчик нажатий для кнопки "выход"
        self.about.clicked.connect(lambda: self.show_window_2())#обработчик нажатий для кнопки "справка"
        self.random.clicked.connect(lambda: self.random_matrix(self.lineEdit.text(), self.lineEdit_2.text(), self.lineEdit_3.text(), self.lineEdit_4.text()))#обработчик нажатий для кнопки "рандом"

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "Сложение"))
        self.pushButton_2.setText(_translate("MainWindow", "Умножение"))
        self.pushButton_3.setText(_translate("MainWindow", "Определитель"))
        self.pushButton_4.setText(_translate("MainWindow", "Обратная матрица"))
        self.label.setText(_translate("MainWindow", "Введите размер первой матрицы"))
        self.label_2.setText(_translate("MainWindow", "Введите размер второй матрицы"))
        self.pushButton_5.setText(_translate("MainWindow", "Создать"))
    

    #=========================================================
    # Функция для рандомного заполнения матриц
    #=========================================================
    # НА ВХОД:
    #   self - ф-ия принадлежит данному классу
    #   x - размер 1 матрицы
    #   y - размер 1 матрицы
    #   a - размер 2 матрицы
    #   b - размер 2 матрицы   
    #=========================================================
    def random_matrix(self, x, y, a, b):
        self.hide_elements()
        if (x != '' and y != ''):
            x = int(x)
            y = int(y)
            for i in range(x*y):
                self.mass1[i].setText(str(random.randint(0, 9)))
        if (a != '' and b != ''):
            a = int(a)
            b = int(b)
            for i in range(a*b):
                self.mass2[i].setText(str(random.randint(0, 9)))



    #=========================================================
    # Функция для скрытия всех элементов
    #=========================================================
    # НА ВХОД:
    #   self - ф-ия принадлежит данному классу   
    #=========================================================
    def hide_elements(self):
        self.ans.hide()
        self.ans_2.hide()
        for i in range(len(self.ans_matrix)):
            self.ans_matrix[i].hide()
        for i in range(len(self.ans_matrix_2)):
            self.ans_matrix_2[i].hide()
        matrix1.clear()
        matrix2.clear()
    

    #=========================================================
    # Функция для создания числовой матрицы
    #=========================================================
    # НА ВХОД:
    #   self - ф-ия принадлежит данному классу
    #   output - массив с элементами ввода матрицы, откуда берутся значения
    #   input - конечная матрица
    #   n - размер матрицы
    #   m - размер матрицы
    # НА ВЫХОД:
    #   True - матрица состоит только из чисел
    #   False - в матрице встречаются посторонние символы
    #=========================================================
    def create_number_matrix(self, output, input, n, m):
        k = 0
        for _ in range(n):
            input.append([0] * m)
        for i in range(n):
            for j in range(m):
                try:
                    input[i][j] = float(output[k].text())#преобразуем тип str в тип float
                    k += 1
                except ValueError:#если произошла ошибка при конвертации то возвращаем из ф-ии False
                    return False
        return True


    #=========================================================
    # Функция для отображения окна справки
    #=========================================================
    # НА ВХОД:
    #   self - ф-ия принадлежит данному классу   
    #=========================================================
    def show_window_2(self):
        self.w2 = Window2()
        self.w2.show() #показываем 2 окно
    

    #=========================================================
    # Функция для закрытия главного окна программы
    #=========================================================
    # НА ВХОД:
    #   self - ф-ия принадлежит данному классу   
    #=========================================================
    def btnClosed(self):
        QtCore.QCoreApplication.instance().quit()
    

    #=========================================================
    # Функция для вывода на экран ошибки
    #=========================================================
    # НА ВХОД:
    #   self - ф-ия принадлежит данному классу
    #   ans - объект, который отображает текст ошибки
    #   x_move - координата по x для объекта ans
    #   y_move - координата по y для объекта ans
    #   text - текст ошибки
    #=========================================================
    def print_error(self, ans, x_move, y_move, text):
        ans.setText(text)
        ans.setFixedWidth(500)
        ans.move(x_move, y_move)
        ans.show()
    

    #=========================================================
    # Функция для вывода на экран ответа в виде матрицы
    #=========================================================
    # НА ВХОД:
    #   self - ф-ия принадлежит данному классу
    #   ans - объект, который отображает слово "ответ"
    #   x_move_ans - координата по x для объекта ans
    #   y_move_ans - координата по y для объекта ans
    #   matrix - массив, служащий для отображения ответа в виде матрицы
    #   n - размер массива
    #   m - размер массива
    #   x_move_el_matr - координата по x для каждого элемента массива
    #   y_move_el_matr - координата по y для каждого элемента массива
    #   result - результат, который необходимо вывести
    #=========================================================
    def print_ans_matrix(self, ans, x_move_ans, y_move_ans, matrix, n, m, x_move_el_matr, y_move_el_matr, result):
        for i in range(n*m): #создаём массив с текстовыми полями длиной x*y
            matrix.append(QtWidgets.QLabel(self.scrollAreaWidgetContents))
        ans.move(x_move_ans, y_move_ans)
        ans.setText("Ответ:")
        ans.show()
        k = 0;
        for i in range(n):
            for j in range(m): #пробегаемся по всем элементам массива и отображаем в виде таблицы все поля
                matrix[k].move(j * 50 + x_move_el_matr, i * 30 + y_move_el_matr)
                matrix[k].setFixedWidth(50)
                matrix[k].setFixedHeight(30)
                matrix[k].setText('{0:.2f}'.format(result[i][j]))
                matrix[k].show()
                k += 1


    #=========================================================
    # Функция для вывода ответа обратной матрицы
    #=========================================================
    # НА ВХОД:
    #   self - ф-ия принадлежит данному классу
    #   first - массив с полями для ввода 1 матрицы
    #   second - массив с полями для ввода 2 матрицы
    #=========================================================
    def obr(self, first, second):
        self.hide_elements()

        x = self.lineEdit.text()
        y = self.lineEdit_2.text()
        if (x != '' or y != ''):
            x = int(x)#перобразуем размеры
            y = int(y)
            check = self.create_number_matrix(first, matrix1, x, y)
            if (check == False):#проверяем данную ошибку и выводим
                self.print_error(self.ans, 10 + y * 50 + 20, 10, "Матрица неверно задана")


            if (check):
                result = adjoint_matrix(matrix1, x, y)
                if (result == 'error1'):
                    self.print_error(self.ans, 10 + y * 50 + 20, 10, "Матрица не квадратная")
                elif (result == 'error2'):
                    self.print_error(self.ans, 10 + y * 50 + 20, 10, "Определитель равен 0")
                else:
                    self.print_ans_matrix(
                        self.ans, 10 + y * 50 + 20, 10, 
                        self.ans_matrix, x, y, 10 + y * 50 + 20 + 100, 10, 
                        result)
        

        a = self.lineEdit_3.text()
        b = self.lineEdit_4.text()
        if (a != '' or b != ''):
            a = int(a)#перобразуем размеры
            b = int(b)
            check = self.create_number_matrix(second, matrix2, a, b)
            if (check == False):
                self.print_error(self.ans_2, 10 + b * 50 + 20, 10 + x * 30 + 50, "Матрица неверно задана")


            if (check):
                result = adjoint_matrix(matrix2, a, b)
                if (result == 'error1'):
                    self.print_error(self.ans_2, 10 + b * 50 + 20, 10 + x * 30 + 50, "Матрица не квадратная")

                elif (result == 'error2'):
                    self.print_error(self.ans_2, 10 + b * 50 + 20, 10 + x * 30 + 50, "Определитель равен 0")
                else:
                    self.print_ans_matrix(
                        self.ans_2, 10 + b * 50 + 20, 10 + x * 30 + 50, 
                        self.ans_matrix_2, a, b, 10 + b * 50 + 20 + 100, 10 + x * 30 + 50, 
                        result)


    #=========================================================
    # Функция для вывода ответа умножения
    #=========================================================
    # НА ВХОД:
    #   self - ф-ия принадлежит данному классу
    #   first - массив с полями для ввода 1 матрицы
    #   second - массив с полями для ввода 2 матрицы
    #=========================================================
    def mult(self, first, second):
        self.hide_elements()
        
        x = self.lineEdit.text()
        y = self.lineEdit_2.text()
        check = False
        if (x != '' or y != ''):
            x = int(x)#перобразуем размеры
            y = int(y)
            check = self.create_number_matrix(first, matrix1, x, y)
            if (check == False):#проверяем данную ошибку и выводим
                self.print_error(self.ans, 10 + y * 50 + 20, 10, "Матрица неверно задана")

        a = self.lineEdit_3.text()
        b = self.lineEdit_4.text()
        check2 = False
        if (a != '' or b != ''):
            a = int(a)#перобразуем размеры
            b = int(b)
            check2 = self.create_number_matrix(second, matrix2, a, b)
            if (check2 == False):#проверяем данную ошибку и выводим
                self.print_error(self.ans_2, 10 + b * 50 + 20, 10 + x * 30 + 50, "Матрица неверно задана")

        if (check and check2):
            result = multiple(x, y, matrix1, a, b, matrix2)
            if (result == False):
                self.print_error(self.ans, 10, x * 30 + 10 + a * 30 + 60, "Матрицы не удовлетворяют условию умножения")
            else:
                self.print_ans_matrix(
                    self.ans, 10, x * 30 + 10 + a * 30 + 60,
                    self.ans_matrix, x, b, 10, 10 + x * 30 + a * 30 + 100,
                    result)


    #=========================================================
    # Функция для вывода ответа сложения
    #=========================================================
    # НА ВХОД:
    #   self - ф-ия принадлежит данному классу
    #   first - массив с полями для ввода 1 матрицы
    #   second - массив с полями для ввода 2 матрицы
    #=========================================================
    def plus(self, first, second):#сложение
        self.hide_elements()#скрыть все элементы

        x = self.lineEdit.text()
        y = self.lineEdit_2.text()
        check = False
        if (x != '' or y != ''):
            x = int(x)#перобразуем размеры
            y = int(y)
            check = self.create_number_matrix(first, matrix1, x, y)
            if (check == False):#проверяем данную ошибку и выводим
                self.print_error(self.ans, 10 + y * 50 + 20, 10, "Матрица неверно задана")

        a = self.lineEdit_3.text()
        b = self.lineEdit_4.text()
        check2 = False
        if (a != '' or b != ''):
            a = int(a)#перобразуем размеры
            b = int(b)
            check2 = self.create_number_matrix(second, matrix2, a, b)
            if (check2 == False):#проверяем данную ошибку и выводим
                self.print_error(self.ans_2, 10 + b * 50 + 20, 10 + x * 30 + 50, "Матрица неверно задана")
        
        if (check and check2):
            result = plus(x, y, matrix1, a, b, matrix2)
            if (result == False):
                self.print_error(self.ans, 10, x * 30 + 10 + a * 30 + 60, "Матрицы разных размерностей")
            else:
                self.print_ans_matrix(self.ans, 10, x * 30 + 10 + a * 30 + 60,
                self.ans_matrix, x, y, 10, x * 30 + 100 + a * 30 + 10,
                result)
    

    #=========================================================
    # Функция для вывода ответа определителя
    #=========================================================
    # НА ВХОД:
    #   self - ф-ия принадлежит данному классу
    #   first - массив с полями для ввода 1 матрицы
    #   second - массив с полями для ввода 2 матрицы
    #=========================================================
    def det(self, first, second):
        self.hide_elements()#скрываем все элементы

        #---------------первая матрица--------------------------------------
        x = self.lineEdit.text()
        y = self.lineEdit_2.text()
        if (x != '' or y != ''):
            x = int(x)#перобразуем размеры
            y = int(y)
            check = self.create_number_matrix(first, matrix1, x, y)#создаём матрицу с числами, если матрица неверно задано будет выведена ошибка
            if (check == False):#проверяем данную ошибку и выводим
                self.print_error(self.ans, 10 + y * 50 + 20, 10, "Матрица неверно задана")
            else:
                result = determ(matrix1, x, y)#считаем определитель

                self.ans.move(10, 10 + x * 30 + 10) #выводим ответ в зависимости от ситуации
                self.ans.setFixedHeight(20)
                self.ans.setFixedWidth(1000)
                if (result != 'error'):
                    self.ans.setText("Определитель первой матрицы: " + str(result)) #записываем в ответ определитель матрицы использую функцию determ
                    self.ans.show() #показываем ответ
                else:
                    self.ans.setText("Матрица не квадратная")
                    self.ans.show() #показываем ошибку
        #---------------вторая матрица--------------------------------------
        a = self.lineEdit_3.text()
        b = self.lineEdit_4.text()
        if (a != '' or b != ''):
            a = int(a)#перобразуем размеры
            b = int(b)
            check = self.create_number_matrix(second, matrix2, a, b)#создаём матрицу с числами, если матрица неверно задано будет выведена ошибка
            if (check == False):#проверяем данную ошибку и выводим
                self.print_error(self.ans_2, 10 + b * 50 + 20, 10 + x * 30 + 50, "Матрица неверно задана")
            else:
                result = determ(matrix2, a, b)#считаем определитель

                self.ans_2.move(10, 10 + x * 30 + 50 + a * 30 + 10) #выводим ответ в зависимости от ситуации
                self.ans_2.setFixedHeight(20)
                self.ans_2.setFixedWidth(1000)
                if (result != 'error'):
                    self.ans_2.setText("Определитель второй матрицы: " + str(result)) #записываем в ответ определитель матрицы использую функцию determ
                    self.ans_2.show() #показываем ответ
                else:
                    self.ans_2.setText("Матрица не квадратная")
                    self.ans_2.show() #показываем ошибку


    #=========================================================
    # Функция для создания массивов с полями для ввода матриц
    #=========================================================
    # НА ВХОД:
    #   self - ф-ия принадлежит данному классу
    #   x - размер 1 матрицы
    #   y - размер 1 матрицы
    #   a - размер 2 матрицы
    #   b - размер 2 матрицы
    #=========================================================
    def create_matrix(self, x, y, a, b):
        self.hide_elements()#скрываем все элементы
        for i in range(len(self.mass1)): #также скрываем поля для ввода матриц
            self.mass1[i].hide()
        self.mass1.clear() #чистим массив с полями ввода для матрицы
        for i in range(len(self.mass2)): #аналогично первой
            self.mass2[i].hide()
        self.mass2.clear()

        if (x != '' and y != ''): #если размеры не пустые, то можем создать матрицу
            if (x.isdigit() and y.isdigit()):#если размер число, продолжаем
                x = int(x) #приводим размер к целому числу
                y = int(y)
            else:#если размер не число, выводим ошибку
                self.print_error(self.ans, 340, 3, "Размер задаётся числом")
                return

            for i in range(x*y): #создаём массив с полями ввода длиной x*y
                self.mass1.append(QtWidgets.QLineEdit(self.scrollAreaWidgetContents))
            for i in range(x*y): #пробегаемся по всем элементам массива и отображаем в виде таблицы все поля для ввода
                self.mass1[i].move((i%y) * 50 + 10, (i//y) * 30 + 10)
                self.mass1[i].setFixedWidth(50)
                self.mass1[i].setFixedHeight(30)
                self.mass1[i].show()
        else:
            #если хотя бы один размер пустой, то ничего не создаём
            return
        
        #аналогично первой матрице
        if (a != '' and b != ''):
            if (a.isdigit() and b.isdigit()):
                a = int(a) #приводим размер к целому числу
                b = int(b)
            else:
                self.print_error(self.ans, 340, 3, "Размер задаётся числом")
                return

            for i in range(a*b):
                self.mass2.append(QtWidgets.QLineEdit(self.scrollAreaWidgetContents))
            for i in range(a*b):
                self.mass2[i].move((i%b) * 50 + 10, (i//b) * 30 + 10 + (x * 30) + 50)
                self.mass2[i].setFixedWidth(50)
                self.mass2[i].setFixedHeight(30)
                self.mass2[i].show()
        else:
            return
        
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 780 + x * 30 * 2 + a * 30 + 100, 490 + y * 50 * 2 + b * 50 + 100))




if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())