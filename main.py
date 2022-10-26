import random
from multiprocessing import Process, cpu_count
import os
from typing import List
from RandomWordGenerator import RandomWord


def createfile(quantity, y):
    quantity_random_word = RandomWord(max_word_size=10, constant_word_size=False)  # создаём объект библиотеки
    file_name = f"./files/Process-{y}-{os.getpid()}.txt"  # задаём название переменной
    try:
        with open(file_name, "a") as file:  # пока файл открыт пишем в него "слова"

            for i in range(quantity):
                file.write(f'{quantity_random_word.generate()}\n')  # записываем слова в файл
        post_analysis_step(file_name)
    except:
        print("Error")


def post_analysis_step(file): #анализ файла
    list_read = counter_vowels_consonants(file)
    print(f"********************************************************\n"
                 f"  Аналитика для файла {file}\n"
                 f"********************************************************\n"
                 f"  1. Всего символов --> {all_symbols(file)}\n"
                 f"  2. Максимальная длина слова --> {max_length_word(file)}\n"
                 f"  3. Минимальная длина слова --> {min_length_word(file)}\n"
                 f"  4. Средняя длина слова --> {average_length_word(file)}\n"
                 f"  5. Количество гласных --> {list_read[0]}\n"
                 f"  6. Количсетво согласных --> {list_read[1]}\n"
                 f"  7. Количество повторений слов с одинаковой длиной:\n")
    try:
        list_counter = get_sl(file)
        s: str = ""

        for numb in range(1, len(list_counter)):
            s += f"     * {numb} сим. >> {list_counter[numb]} повтор.\n"
        return print(s)
    except:
        print("Error_Write_Result")


def get_sl(file):# проверка на совпадение слов с одной длиной
    sl1: int = 0
    sl2: int = 0
    sl3: int = 0
    sl4: int = 0
    sl5: int = 0
    sl6: int = 0
    sl7: int = 0
    sl8: int = 0
    sl9: int = 0
    sl10: int = 0
    with open(f'{file}', 'r') as file1:
        for line in file1.readlines():
            match len(line): # в зависимости от длины слова мы присваеваем определённой переменной +1
                case 1:
                    sl1 += 1
                case 2:
                    sl2 += 1
                case 3:
                    sl3 += 1
                case 4:
                    sl4 += 1
                case 5:
                    sl5 += 1
                case 6:
                    sl6 += 1
                case 7:
                    sl7 += 1
                case 8:
                    sl8 += 1
                case 9:
                    sl9 += 1
                case 10:
                    sl10 += 1
    return [sl1, sl2, sl3, sl4, sl5, sl6, sl6, sl7, sl8, sl9, sl10]


def counter_vowels_consonants(file):
    vowels: int = 0
    consonants: int = 0
    symbols: list = ['a', 'e', 'i', 'o', 'u', 'y']
    with open(f'{file}', 'r') as files:
        for line in files.readlines():
            line.lower()
            for str in line:
                if str in symbols: #пока в сторке присутсвуют символы из списка symbols ведёстя счет гласных, если же символ в строке не выдаёт совпадение в списке то +1 к согасным
                    vowels += 1
                else:
                    consonants += 1
    return [vowels, consonants]


def all_symbols(file):
    try:
        file = open(f"{file}")
        file_words = file.read()
        symbol_quantity: int = len(file_words)  # считаем количество элементов
        return symbol_quantity
    except:
        print("Error")


def max_length_word(file):
    try:
        with open(f'{file}', 'r') as file1:
            m: str = max(file1, key=len) #обрашаемяся к файлу с параметром расматривать объекты по их длине - считаем макс. длину строки
        return len(m) - 1
    except:
        print("Error")


def min_length_word(file):
    try:
        file = open(f"{file}")
        file_words = file.read()
        kk = min(len(w) for w in file_words) #обрашаемяся к файлу через цикл с параметром расматривать объекты по их длине и вичислением минимальной длины строки - считаем мин. длину строки
        return kk
    except:
        print("Error")


def average_length_word(file):
    try:
        file = open(f'{file}', 'r')
        file_words = file.read()
        words = file_words.split()
        number = len(file_words)
        average = number / len(words)
        return average
    except:
        print("Error")


if __name__ == "__main__":
    try:
        list_proc: List[Process] = []  # создаём список процессов

        for n in range(1, cpu_count()+1):  # создаём цикл равный количетву нашему потоков +1 так как цикл заканчивайтся когда значение равно краю интервала
            name_process: str = f"Process-{n}"  # задание названия документа
            quantity_word: int = random.randint(100000, 5000000)  # задание количество слов
            process = Process(target=createfile, args=(quantity_word, n), name=name_process)  # создание процесса
            list_proc.append(process)  # заносим процессы в список
            process.start()  # запускаем ранее созданный процесс

        for i in range(1, cpu_count()+1):  # создаём цикл для ожидания выполнения каждого процесса для избежания тотального кабздеца процессора
            list_proc[i].join()  # ждём завершения каждого процесса
    except:
        print("Error")
