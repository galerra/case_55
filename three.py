# !/usr/bin/env python3
# -*- encoding: utf-8 -*-

if __name__ == "__main__":
    day = int(input('Введите день:'))
    month = str(input("Введите месяц:"))
    year = int(input("Введите год:"))
    l = ["январь","февраль","март","апрель","май","июнь","июль","август","сентябрь","октябрь","ноябрь","декабрь"]
    m = l.index(month) + 1
    if day * m  == year - year // 100 * 100:
        print('True')
    else:
        print('False')
