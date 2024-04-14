"""input1 - пример, который можно решить
input2 - пример, который решить нельзя (для проверки изменить файл в строке - 78, переменная put)"""

def file(a):#вывод данных из файла
     with open(a, "r") as file1:
        mas = []
        masm = []
        while True:
            line = file1.readline().strip()
            if not line:
                break
            masm = line.split(' ')
            for i in range(0, len(masm)):
                masm[i] = int(masm[i])
            mas.append(masm)
        return mas

def vivod(mas):
    """вывод данных на консоль"""
    for i in range(0, len(mas)):
        string = str(mas[i])
        print(string[0:8] + ' | ' + string[10:17] + ' | ' + string[19:])
        if i+1 != 0 and (i+1) % 3 == 0 and i != 8:
            print('-----------------------------')

def zapis(mas):
    """вывод данных в файл"""
    f = open('output.txt', 'w')
    f.close()
    with open("output.txt", "a") as file1:
        i = 0
        for i in range(0, len(mas)):
            string = str(mas[i]).replace(',', '')
            file1.write(string[1:6] + ' | ' + string[7:12] + ' | ' + string[13:-1])
            if i + 1 != 0 and (i + 1) % 3 == 0 and i != 8:
                file1.write('\n')
                file1.write('---------------------')
            file1.write('\n')

def osn(mas):
    """основная часть"""
    indnull = index_null(mas)
    if indnull == None:
        return True
    else:
        r, c = indnull
    for n in range(1,10):
        if prov(mas,n, (r,c)):
            mas[r][c] = n
            if osn(mas):
                return True
            mas[r][c] = 0
    return False

def prov(mas, n, ind):
    """проверка цифр по горизонтали/вертикали/в "ящичке" 3*3"""
    for i in range(len(mas[0])):
        if mas[i][ind[1]] == n and ind[0] != i:
            return False
    for i in range(len(mas[0])):
        if mas[ind[0]][i] == n and ind[1] != i:
            return False
    y = ind[0] // 3
    x = ind[1] // 3
    for i in range(y*3, y*3 + 3):
        for j in range(x*3, x*3 + 3):
            if mas[i][j] == n and (i, j) != ind:
                return False
    return True

def index_null(mas):
    """просматриваем индексы нулей"""
    for i in range(len(mas)):
        for j in range(len(mas[0])):
            if mas[i][j] == 0:
                return i,j
    return None
put = "input2.txt"
sudi = file(put)
sud = file(put)
osn(sudi)

if sudi == sud:
    file1 = open('output.txt', 'w')
    file1.write('А тут ничегошеньки(')
    file1.close()
    print('Impossible') #ждать придётся дольше, чем если решить реально
else:
    zapis(sudi)
    print('See the file "output.txt"')