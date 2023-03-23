vixod = str(input('Введите текст: '))
key_bykv = str(input('Введите ключ: '))

mas = {10000000: "А", 10000001: "Б", 10000010: "В", 10000011: "Г", 10000100: "Д", 10000101: "Е", 10000110: "Ж", 10000111: "З", 10001000: "И", 10001001: "Й", 10001010: "К", 10001011: "Л",
       10001100: "М", 10001101: "Н", 10001110: "О", 10001111: "П", 10010000: "Р", 10010001: "С", 10010010: "Т", 10010011: "У", 10010100: "Ф", 10010101: "Х", 10010110: "Ц", 10010111: "Ч",
       10011000: "Ш", 10011001: "Щ", 10011010: "Ъ", 10011011: "Ы", 10011100: "Ь", 10011101: "Э", 10011110: "Ю", 10011111: "Я", 10100000: " ", 10100001: ".", 10100010: ","
       }

mas_base = {0: "А", 1: "B", 2: "C", 3: "D", 4: "E", 5: "F", 6: "G", 7: "H", 8: "I", 9: "J", 10: "K", 11: "L", 12: "M", 13: "N", 
            14: "O", 15: "P", 16: "Q", 17: "R", 18: "S", 19: "T", 20: "U", 21: "V", 22: "W", 23: "X", 24: "Y", 25: "Z", 26: "a", 27: "b", 
            28: "c", 29: "d", 30: "e", 31: "f", 32: "g", 33: "h", 34: "i", 35: "j", 36: "k", 37: "l", 38: "m", 39: "n", 40: "o", 41: "p", 
            42: "q", 43: "r", 44: "s", 45: "t", 46: "u", 47: "v", 48: "w", 49: "x", 50: "y", 51: "z", 52: "0", 53: "1", 54: "2", 55: "3",
            56: "4", 57: "5", 58: "6", 59: "7", 60: "8", 61: "9", 62: "+", 63: "/"
            }

def nachalo(isxod, mas): # Вводим туда числа или буквы
    otvet = []
    if type(isxod) == str:
        for i in isxod:
            otvet.append(zapis(mas, i))
    else:
        for i in isxod:
            otvet.append(otpis(mas, i))
    return otvet

def zapis(d, value): # Ввели букву
    for kl, val in d.items():
        if value == val:
            return kl

def otpis(mas, isxod): # Ввели Число
    return mas.get(isxod)

posle_nachalo = nachalo(vixod, mas)
key = nachalo(key_bykv, mas)
print(posle_nachalo, 'Сначала цифры')
print(key, "Теперь ключ")

def xor(value, key, mas): # Операция XOR
    s = 0
    new_arr = []
    while len(value) > len(key): # Укорачиваем и удлиняем ключ
        key.append(key[s])
        s += 1
    while len(value) < len(key):
        key.pop(-1)
    
    for v,k in zip(value, key): # Сам Xor
        this_znac = ""
        for per, vto in zip(str(v),str(k)):
            if per == vto:
                this_znac = this_znac + "0"
            else:
                this_znac = this_znac + "1"
        new_arr.append(this_znac)
    
    return new_arr

posle_xor = xor(posle_nachalo, key, mas)
print(posle_xor, "После XoR")

def soed(arr):
    stroka = ""
    for i in arr:
        stroka = stroka + str(i)
    return stroka

posle_soed = soed(posle_xor)

def b64e(s): #кодировка base64
    dlina = len(s)//6
    ostatok = len(s) - dlina * 6
    a = 0
    b = 5
    otvet = []
    for i in range(dlina):
        chis = otpis(mas_base,int(s[a:b+1],2)) 
        print(chis, '<-', str(int(s[a:b+1],2)))
        otvet.append(chis)
        a = a + 6
        b = b + 6
    if ostatok != 0:
        chis = otpis(mas_base,int(s[a:b+1],2))
        print(chis, '<-', str(int(s[a:b+1],2)))
    return otvet

posle_base = b64e(posle_soed)
print(posle_base, "После base")

def from_russia_keyboard(text): # Измена раскладки
    layout = dict(zip(map(ord, '''qwertyuiop[]asdfghjkl;'zxcvbnm,./`QWERTYUIOP{}ASDFGHJKL:"ZXCVBNM<>?~'''),
                               '''йцукенгшщзхъфывапролджэячсмитьбю.ёЙЦУКЕНГШЩЗХЪФЫВАПРОЛДЖЭЯЧСМИТЬБЮ,Ё'''))
    otvet = []
    for i in text:
        otvet.append(i.translate(layout))
    return otvet

posle_keyb = from_russia_keyboard(posle_base)
print(posle_keyb, "Перевод на русккий")

def sort(posle_keyb):
    for i in range(0,len(posle_keyb),2):
        posle_keyb.append(posle_keyb[i])
        posle_keyb.pop(i)
    return posle_keyb 
  
posle_sort = sort(posle_keyb)
print(posle_sort, "После сортировки")

last_soed = soed(posle_sort)
print(last_soed)