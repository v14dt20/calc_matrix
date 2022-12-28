import math
#ф-ии необходимые для обратной матрицы
def minor(dim, data, i, j): #вычисление минора
    mn = [] #матрица миноров
    for k in range(dim): #цикл для поиска миноров
        r = []
        for q in range(dim):
            if k != i and q != j: #если не первая строка и столбец не совпадает со столбцом минора
                r += [data[k][q]] #то записываем в строку для минора эти элементы
        if r != []:
            mn += [r] #добавляем эту строку в минор если она не пустая
    return determ(mn, dim - 1, dim - 1)
def cofactor(dim, data, i, j): #функция вычисления кофактора
    return math.pow(-1, i + j) * minor(dim, data, i, j)
def cofactor_matrix(dim, data): #функция вычисления кофакторной матрицы
    new_matrix = []
    for i in range(dim):
        new_matrix.append([0] * dim)
    for i in range(dim):
        for j in range(dim):
            new_matrix[i][j] = cofactor(dim, data, i, j)
    return new_matrix
def transpose_matrix(dim, data):#транспонирование матрицы
    new_matrix = []
    for i in range(dim):
        new_matrix.append([0] * dim)
    for  i in range(dim):
        for  j in range(dim):
            new_matrix[j][i] = data[i][j]
    return new_matrix
def adjoint_matrix(data, n, m):#обратная матрица
    det = determ(data, n, m)
    if (det == 'error'):
        return 'error1'
    if (det == 0):
        return 'error2'
    new_matrix = transpose_matrix(n, cofactor_matrix(n, data))
    for i in range(n):
        for j in range(n):
            new_matrix[i][j] *= (1/det)
    return new_matrix


def determ(matrix, n, m):#ф-ия поиска определителя матрицы любой размерности (рекурсия)
    if (n != m):#если матрица не квадратная, возвращаем ложь и заканчиваем выполнение функции
        return 'error'

    match n:
        case 1: #определитель для матрицы размером 1х1
            return matrix[0][0]
        case 2: #определитель для матрицы размером 2х2
            return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
        case n: #определитель для матрицы размером nxn
            s = 0 #сумма
            for i in range(n): #цикл для поиска миноров
                mn = [] #матрица миноров
                for k in range(n): #вложенные циклы для пробегания по всем элементам матрицы 
                    r = [] #строка для матрицы миноров
                    for j in range(n):
                        if k != 0 and j != i: #если не первая строка и столбец не совпадает со столбцом минора
                            r += [matrix[k][j]] #то записываем в строку для минора эти элементы
                    if r != []:
                        mn += [r] #добавляем эту строку в минор если она не пустая
                s += matrix[0][i] * determ(mn, n - 1, m - 1)*(-1)**i #ищем дополнение и записываем в сумму
            return s #возвращаем сумму


def multiple(n1, m1, matrix1, n2, m2, matrix2): #ф-ия нахождения произведения матриц
    if (n1 != m2 and m1 != n2):
        return False
    result = [] #результат
    for i in range(n1): #заполняем 0 матрицу с ответом
        result.append([0] * m2)
    for i in range(n1): #пробегаемся по столбцам матрицы с ответом
        for j in range(m2): #пробегаемся по строкам матрицы с ответом
            for k in range(m1): #пробегаемся по всем элементам 2 матриц
                result[i][j] += matrix1[i][k] * matrix2[k][j] #в каждый элемент матрицы с ответом добавляем произведение
    return result #возвращаем ответ

def plus(n1, m1, matrix1, n2, m2, matrix2):
    if (n1 != n2 or m1 != m2):
        return False
    result = []
    for i in range(n1):
        result.append([0] * m1)
    for i in range(n1):
        for j in range(m1):
            result[i][j] = matrix1[i][j] + matrix2[i][j]
    return result

def print(text1, text2):
    print(text1 + " " + text2)
