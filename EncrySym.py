#! Палкин А.Е. 331 группа Шифратор
from tkinter import *
from tkinter.filedialog import *
import tkinter.messagebox
from tkinter import ttk

CryptMode = "caesar"
alphabet_rus = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"
alphabet_eng = "abcdefghijklmnopqrstuvwxyz"
current_language = alphabet_rus
dragonDict = ["\\", "/", "_"] # \ => 0, / => 1, _ => ""

#Цвета
frame_bg = "grey7"
bd_color = "#1B1"
label_fg = "#1B1"

#Кейс с виджетами
keysWidgets = []
#Режим шифра
def SetMode(mode):
    global CryptMode
    CryptMode = mode

#Функция проверки для шифровки
def Encrypt(text):
    mode = CaseInsensitive(CryptMode)
    result = ""
    if mode == "caesar":
        result = EncryptCaesar(text)
    elif mode == "viginer":
        result = EncryptVigener(text)
    elif mode == "dragon":
        result = DragonCrypt(text)
    return result

#Функция проверки для расшифровки
def Decrypt(text):
    mode = CaseInsensitive(CryptMode)
    if mode == "caesar":
        result = DecryptCaesar(text)
    elif mode == "viginer":
        result = DecryptVigener(text)
    elif mode == "dragon":               
        result = DragonDecrypt(text)
    return result

# Возвращает выбранный язык
def GetLanguage():
    return Combo_language.get()

# Возвращает выбранный ключ
def GetKey():
    key = ""
    if CryptMode == "caesar":
        key = Combo_key.get()
    elif CryptMode == "viginer":
        key = entryKey.get()
    return key
def aboutAuthor():
    tkinter.messagebox.showinfo('Об авторе','Разработчик: Палкин А.Е.\n'
                                'курсант ТАТК ГА 331 группы\n'
                                'Почта для связи: docfire69@gmail.com')
def program():#о программе
    tkinter.messagebox.showinfo('О программе','Программа - Шифратор\n'
                                'Шифрует/дешифрует вводимый текст пользователем\n'
                                'Version 1.0\n\n'
                                "Автор: Палкин Андрей\n"
                                "курсант ТАТК ГА 331 группы")
    
def infoProgram():
    tkinter.messagebox.showinfo('Инструкция','Смена режима шифра - "Система => Шифр". '
                                'В выпадном поле "Язык", можно выбрать язык шифрования'
                                '\nP.s - Не забудьте сменить свою раскладку на клавиатуре! '
                                '\nПри смене шифра будут появляться или исчезать необходимые поля.\n'
                                '\nВ шифре Цезаря также можно указать ключ, с которым вводимое сообщение'
                                'будет сдвигаться по выбранному ключу.\n'
                                '\nВ шифре Вижинера - ключ нужно вписывать самому.'
                                '\nP.s - ключ не должен быть больше сообщения!\n'
                                '\nВ шифре Дракона - при дешифровке, необходимо учитывать, что нужно6'
                                'писать особыми символами!(см. информацию о данном шифре по кнопке "Info")')
    
def infoCaesar():
	tkinter.messagebox.showinfo('Цезарь','Шифр Цезаря, также известный как шифр сдвига, '
		'код Цезаря или сдвиг Цезаря — один из самых простых и наиболее широко известных методов шифрования.\n'
		'\nШифр Цезаря — это вид шифра подстановки, в котором каждый символ в открытом тексте заменяется символом, '
		'находящимся на некотором постоянном числе позиций левее или правее него в алфавите.'
		'Например, в шифре со сдвигом вправо на 3, А была бы заменена на Г, Б станет Д, и так далее.\n'
		'\nТочно также происходит и дешифровка.')

def infoViginer():
	tkinter.messagebox.showinfo('Виженер','В шифре Цезаря каждая буква алфавита сдвигается на несколько позиций;'
		'например в шифре Цезаря при сдвиге +3, A стало бы D, B стало бы E и так далее. Шифр Виженера состоит из последовательности'
		'нескольких шифров Цезаря с различными значениями сдвига. Для зашифровывания может использоваться таблица алфавитов,'
		'называемая tabula recta или квадрат (таблица) Виженера.\n\nПрименительно к латинскому алфавиту таблица Виженера составляется'
		'из строк по 26 символов, причём каждая следующая строка сдвигается на несколько позиций.'
		'Таким образом, в таблице получается 26 различных шифров Цезаря. На каждом этапе шифрования используются различные алфавиты,'
		'выбираемые в зависимости от символа ключевого слова.'
		'\n\nНапример, предположим, что исходный текст имеет такой вид:'
		'\n             ATTACKATDAWN\n'
		'Человек, посылающий сообщение, записывает ключевое слово («LEMON») циклически до тех пор, пока его длина не будет'
		'соответствовать длине исходного текста:'
		'\n             LEMONLEMONLE\n'
		'Первый символ исходного текста ("A") зашифрован последовательностью L, которая является первым символом ключа.'
		'Первый символ зашифрованного текста ("L") находится на пересечении строки L и столбца A в таблице Виженера.'
		'Точно так же для второго символа исходного текста используется второй символ ключа; то есть второй символ'
		'зашифрованного текста ("X") получается на пересечении строки E и столбца T. Остальная часть исходного текста '
		'шифруется подобным способом.'
		'\nИсходный текст:       ATTACKATDAWN'
		'\nКлюч:                          LEMONLEMONLE'
		'\nЗашифрованный текст:  LXFOPVEFRNHR'
		'\n\nРасшифровывание производится следующим образом: находим в таблице Виженера строку, соответствующую первому символу'
		'ключевого слова; в данной строке находим первый символ зашифрованного текста. Столбец, в котором находится данный'
		'символ, соответствует первому символу исходного текста. Следующие символы зашифрованного текста расшифровываются '
		'подобным образом.')

def infoDragon():
	tkinter.messagebox.showinfo('Дракон','В шифре дракона, каждый символ вводимого сообщения, переводится свой номер юникода'
		'после чего, полученное число юникода, переводится в двоичный код(0 и 1).\n'
		'После этого, нулям и единицам присваиваются свои символы\n( \\ => 0, / => 1, _ => "")\n\n'
		'Расшифровка происходит в обратном порядке.')
    
def schemCaesar():
    os.system("Caesar.png")
    
def schemVigener():
    os.system("Vigener.png")
    
def schemDragon():
    os.system("Dragon.png")
#==========================================================
#==========================Цезарь==========================
#==========================================================

# Шифрование Цезарем
def EncryptCaesar(text):
    global current_language
    encrypt = text
    key = int(GetKey())
    encrypted = ""
    
    if GetLanguage() == "Rus":
        current_language = alphabet_rus
    elif GetLanguage() == "Eng":
        current_language = alphabet_eng

    for letter in encrypt:
        position = current_language.find(letter)
        newPosition = (position + key) % len(current_language)
        if letter in current_language:
            encrypted = encrypted + current_language[newPosition]
        else:
            encrypted = encrypted + letter    
    return encrypted

# Дешифрование Цезарем
def DecryptCaesar(text):
    global current_language
    decrypt = text
    key = -int(GetKey())
    decrypted = ""
    
    if GetLanguage() == "Rus":
        current_language = alphabet_rus
    elif GetLanguage() == "Eng":
        current_language = alphabet_eng
        
    for letter in decrypt:
        position = current_language.find(letter)
        newPosition = (position + key) % len(current_language)
        if letter in current_language:
            decrypted = decrypted + current_language[newPosition]
        else:
            decrypted = decrypted + letter
    return decrypted

#==========================================================
#==========================Вижинер=========================
#==========================================================
class Vigener:
    def __init__(self):
        self.down, self.up = 0, 0
        self.alphabet = ""
        self.key = ""
        self.text = ""
        self.table = None
        self.carriage = 0

    # Меняет язык словаря для шифровки
    def ChangeLanguage(self):
        global current_language
        if GetLanguage() == "Rus":
            current_language = alphabet_rus
            self.carriage = 33
            self.down, self.up = 1072, 1104
            self.alphabet = [chr(i) for i in range(self.down, self.up)]
            self.key = self.minusnotletters(self.minusyo(self.key.lower()))
            self.text = self.minusnotletters(self.minusyo(self.text.lower()))
        elif GetLanguage() == "Eng":
            current_language = alphabet_eng
            self.carriage = 27
            self.down, self.up = 97, 123
            self.alphabet = [chr(i) for i in range(self.down, self.up)]
            self.key = self.minusnotletters(self.key.lower())
            self.text = self.minusnotletters(self.text.lower())

        self.CreateTable()
        if not self.KeyNormalization():
            return False
        return True

    #Составляем таблицу Виженера
    def CreateTable(self):
        table = []
        for i in range(self.carriage-1):
            temp = []
            for j in range(self.up+1-self.carriage, self.up):
                temp.append(chr(j))
            for j in range(self.down, self.up+1-self.carriage):
                temp.append(chr(j))
            table.append(temp)
            self.carriage -= 1
        self.table = table
        #for i in table: print(*i)
        

    # Циклически записываем ключевое слово, пока его
    # длина не будет равна длине шифруемого текста
    def KeyNormalization(self):
        if not self.KeyValidation():
            return False
        if len(self.key) == 0:
            return False
        oldkey = self.key
        while len(self.key) < len(self.text):
            if len(self.key) + len(oldkey) > len(self.text):
                temp = list(oldkey)
                for i in range(len(self.text) - len(self.key)):
                    self.key += temp[i]
            else:
                self.key += oldkey
        if len(self.key) > len(self.text):
            return False
        return True

    # Проверка ключа на правлильность ввода по языку
    def KeyValidation(self):
        key = self.key
        for i in key:
            if i not in current_language:
                return False
        return True

    # Убирает все не буквенные символы
    def minusnotletters(self, words):
        words = list(words)
        i = 0
        while i != len(words):
            if words[i] not in self.alphabet:
                del words[i]
            else:
                i += 1
        words = "".join(words)
        return words

    # Заменяет все "ё" на "е"
    def minusyo(self, words):
        words = list(words)
        for i in range(len(words)):
            if words[i] == "ё":
                words[i] = "е"
        words = "".join(words)
        return words

    # Шифрование
    def encrypt(self, key, text):
        self.key = key
        self.text = text
        if not self.ChangeLanguage():
            return text
        text = self.text
        self.text = ""
        for i in range(len(list(text))): 
            self.text += self.table[ord(text[i])-self.down][ord(self.key[i])-self.down]
        return self.text

    # Дешифровка
    def decrypt(self, key, text):
        self.key = key
        self.text = text
        if not self.ChangeLanguage():
            return text
        text = self.text
        self.text = ""
        for i in range(len(list(text))): 
            for j in range(len(list(self.table[0]))):
                if self.table[0][j] == self.key[i]:
                    for k in range(len(self.table[j])):
                        if self.table[j][k] == text[i]:
                            ind = k
                            break
                    break
            self.text += self.table[ind][0]
        return self.text 
_vigener = Vigener()

def EncryptVigener(text):
    key = GetKey()
    result = _vigener.encrypt(key, text)
    return result

def DecryptVigener(text):
    key = GetKey()
    result = _vigener.decrypt(key, text)
    return result
    
#==========================================================
#==========================Дракон==========================
#==========================================================
        
#Шифрование Драконом
def DragonCrypt(text):
    # Переводит биты в символы драгонита
    def Dragoniting(binChars):
        result = ""
        for i in binChars:
            word = ""
            for j in i:
                if j == "0":
                    word += dragonDict[0]
                elif j == "1":
                    word += dragonDict[1]
                    
            if binChars.index(i) != len(binChars) - 1:
                word += dragonDict[2]
            result += word

        if len(result) > 0 and result[-1] == dragonDict[2]:
            result = result[:-1]
        return result
            
    # Шифр слова
    def CryptingWord(word):
        splitedChars = list(word)
        ordedChars = Ording(splitedChars)
        binChars = IntToBinary(ordedChars)
        dragonit = Dragoniting(binChars)
        result = dragonit
        return result

    text = text.replace("\n", " ")
    splitedText = text.split(" ")
    result = ""
    for i in splitedText:
        result += CryptingWord(i) + " "

    result = result.strip()
    return result

# Дешифрование драконом
def DragonDecrypt(text):
    # Переводит биты в символы драгонита
    def Dedragoniting(splitedChars):
        result = ""
        for i in splitedChars:
            word = ""
            for j in i:
                if j == dragonDict[0]:
                    word += "0"
                elif j == dragonDict[1]:
                    word += "1"
                else:
                    raise Exception("Some exception")
     
            charNumber = BinaryToInt(word)
            if charNumber != None:
                cahr = chr(charNumber)
                result += cahr
        return result
            
    # Шифр слова
    def DecryptingWord(word):
        splitedChars = word.split(dragonDict[2])
        word = Dedragoniting(splitedChars)
        result = word
        return result

    text = text.replace("\n", " ")
    splitedWord = text.split(" ")
    result = ""
    for i in splitedWord:
        result += DecryptingWord(i) + " "

    result = result.strip()
    return result


# Сделать текст регистронезависимым
def CaseInsensitive(text):
    result = text.lower()
    return result

# Получение числа из символов списка
def Ording(chars):
    result = []
    for i in chars:
        result.append(ord(i))
    return result

# Конвертация всего списка из чисел в бинарный код
def IntToBinary(nubmers):
    result = []
    for i in nubmers:
        result.append(format(i, "b"))
    return result

# Конвертация всего списка из бинарного кода в числа
def BinaryToInt(binary):
    if (binary == ""):
        return
    result = int(binary, 2)
    return result

#Функция взятия шифровки
def cript():
    text = text1.get(1.0, END)
    result = Encrypt(text)
    text1.config(bg="grey40")
    text2.delete(1.0, END)
    text2.insert(1.0, result)
   
#Функция взятия дешифровки    
def decript():
    text = text2.get(1.0, END)
    try:
        result = Decrypt(text)
        text2.config(bg="grey40")
        text1.delete(1.0, END)
        text1.insert(1.0, result)
    except:
        text2.config(bg="red")
        
#Проверка выбора шифров    
def get(mode):
    SetMode(mode)
    if mode == "caesar":
        text1.delete(1.0, END)
        text2.delete(1.0, END)
        keysWidgets[0].place(x=5, y=5)
        keysWidgets[1].place(x=370, y=5)
        keysWidgets[2].place(x=600, y=600)
        keysWidgets[3].place(x=50, y=10)
        keysWidgets[4].place(x=600, y=600)
        keysWidgets[5].place(x=600, y=600)
        keysWidgets[6].place(x=230, y=20)
        keysWidgets[7].place(x=600, y=600)
        keysWidgets[8].place(x=600, y=600)
    elif mode == "viginer":
        text1.delete(1.0, END)
        text2.delete(1.0, END)
        keysWidgets[0].place(x=5, y=5)
        keysWidgets[1].place(x=600, y=600)
        keysWidgets[2].place(x=370, y=5)
        keysWidgets[3].place(x=600, y=600)
        keysWidgets[4].place(x=50, y=10)
        keysWidgets[5].place(x=600, y=600)
        keysWidgets[6].place(x=600, y=600)
        keysWidgets[7].place(x=230, y=20)
        keysWidgets[8].place(x=600, y=600)
    elif mode == "dragon":
        text1.delete(1.0, END)
        text2.delete(1.0, END)
        keysWidgets[0].place(x=-100, y=-100)
        keysWidgets[1].place(x=600, y=600)
        keysWidgets[2].place(x=600, y=600)
        keysWidgets[3].place(x=600, y=600)
        keysWidgets[4].place(x=600, y=600)
        keysWidgets[5].place(x=50, y=10)
        keysWidgets[6].place(x=600, y=600)
        keysWidgets[7].place(x=600, y=600)
        keysWidgets[8].place(x=230, y=20)

        
#Нажатие на клавиши    
def keypressEncrypt(event):
    root.after(1, lambda: cript())
    
def keypressDecrypt(event):
    root.after(1, lambda: decript())
    
#==========================================================
#===========================GUI============================
#==========================================================   
root = Tk()
root.title("EncrySym")
root.geometry("1000x500")
root.resizable(False, False)

#Меню
mainmenu = Menu(root)
root.config(menu=mainmenu)
filemenu = Menu(mainmenu, tearoff=0)
submenu = Menu(filemenu)
submenu.add_command(label="Цезаря", command = lambda: get("caesar"))
submenu.add_command(label="Вижинера", command = lambda: get("viginer"))
submenu.add_command(label="Дракона", command = lambda: get("dragon"))

shemmenu = Menu(filemenu)
shemmenu.add_command(label="Цезарь", command = schemCaesar)
shemmenu.add_command(label="Виженер", command = schemVigener)
shemmenu.add_command(label="Дракон", command = schemDragon)

filemenu.add_cascade(label='Шифр', menu=submenu, underline=0)
filemenu.add_command(label="Выход", command=root.destroy)
helpmenu = Menu(mainmenu, tearoff=0)

helpmenu.add_command(label="О программе", command = program)
helpmenu.add_command(label="Об авторе", command = aboutAuthor)
helpmenu.add_command(label="Инструкция", command = infoProgram)
helpmenu.add_cascade(label='Схема шифра', menu=shemmenu, underline=1)

mainmenu.add_cascade(label="Система", menu=filemenu)
mainmenu.add_cascade(label="Справка", menu=helpmenu)

#Фреймы
frame1 = Frame(root, width=500, height=500, highlightthickness=3,
               bg=frame_bg, highlightbackground=bd_color)
frame1.place(x=0, y=0)
frame2 = Frame(root, width=500, height=500, highlightthickness=3,
                   bg=frame_bg, highlightbackground=bd_color)
frame2.place(x=500, y=0)

frame3 = Frame(root, width = 120, height = 50, bg = frame_bg)
frame3.place(x=5, y=8)
keysWidgets.append(frame3)#0

frame4 = Frame(root, width = 120, height = 50, bg = frame_bg)
frame4.place(x=375, y=8)
keysWidgets.append(frame4)#1

frame5 = Frame(root, width = 120, height = 50, bg = frame_bg)
frame5.place(x=600, y=600)
keysWidgets.append(frame5)#2

frameShifr = Frame(root, width = 200, height = 50, bg = frame_bg)
frameShifr.place(x=150, y=20)

#Метки
label_language = Label(frame3, font="arial 10", bg=frame_bg, fg=label_fg,
                  text="Язык:")
label_language.place(x=2, y=0)
    
label_shag = Label(frame4, font="arial 10", bg=frame_bg, fg=label_fg,
                  text="Ключ:")
label_shag.place(x=0, y=0)

entryKeyLabel = Label(frame5, font="arial 10", bg=frame_bg, fg=label_fg,
                  text="Ключ:")
entryKeyLabel.place(x=0, y=0)
    
label1 = Label(frame1, font="arial 30", bg=frame_bg, fg=label_fg,
                  text="Шифрование")
label1.place(x=120, y=60)

label1 = Label(frame2, font="arial 30", bg=frame_bg, fg=label_fg,
                  text="Дешифрование")
label1.place(x=120, y=60)
    
label2 = Label(frame1, font="arial 18", bg=frame_bg, fg=label_fg,
                  text="Введите текст ниже:")
label2.place(x=20, y=140)
    
label2 = Label(frame2, font="arial 18", bg=frame_bg, fg=label_fg,
                  text="Введите текст ниже:")
label2.place(x=20, y=140)

labelCaesar = Label(frameShifr, font="arial 18", bg=frame_bg, fg=label_fg,
                  text="Цезарь:")
labelCaesar.place(x=50, y=10)
keysWidgets.append(labelCaesar)#3

labelVigener = Label(frameShifr, font="arial 18", bg=frame_bg, fg=label_fg,
                  text="Виженер:")
keysWidgets.append(labelVigener)#4

labelDragon = Label(frameShifr, font="arial 18", bg=frame_bg, fg=label_fg,
                  text="Дракон:")
keysWidgets.append(labelDragon)#5


#комбобокс
vlist_language = ["Rus",
                  "Eng"]
Combo_language = ttk.Combobox(frame3, state="readonly", width = 15, values = vlist_language)
Combo_language.current(0)
Combo_language.place(x=0, y=20)

vlist_key = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10",
          "11","12","13", "14", "15", "16", "17", "18", "19",
          "20", "21","22", "23","24", "25", "26", "27", "28",
          "29", "30", "31", "32", "33"]
Combo_key = ttk.Combobox(frame4, state="readonly", width = 15, values = vlist_key)
Combo_key.current(0)
Combo_key.place(x=0, y=20)

#Поля
text1 = Text(frame1, width=40, height=5, font = "Arial 15",
            bg="grey40", highlightbackground="black",
            highlightthickness=1,fg='white', wrap=WORD)
text1.place(x=20, y=180)
text1.bind("<KeyPress>", keypressEncrypt)

text2 = Text(frame2, width=40, height=5, font = "Arial 15",
            bg="grey40", highlightbackground="black",
            highlightthickness=1,fg='white', wrap=WORD)
text2.place(x=20, y=180)
text2.bind("<KeyPress>", keypressDecrypt)

entryKey = Entry(frame5, width=18)
entryKey.place(x=0, y=20)

#Кнопки
btnInfoCaesar = Button(frame2, width = 10, text='Info', command = infoCaesar,
                       bg=frame_bg, fg=label_fg )
btnInfoCaesar.place(x=230, y=20)
keysWidgets.append(btnInfoCaesar)#6

btnInfoVigener = Button(frame2, width = 10, text='Info', command = infoViginer,
                       bg=frame_bg, fg=label_fg )
keysWidgets.append(btnInfoVigener)#7

btnInfoDragon = Button(frame2, width = 10, text='Info', command = infoDragon,
                       bg=frame_bg, fg=label_fg )
keysWidgets.append(btnInfoDragon)#8
root.mainloop()
