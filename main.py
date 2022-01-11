# !/usr/bin/env python3
# -*- encoding: utf-8 -*-

if __name__ == "__main__":
    n = int(input())
    spisok = set(range(2, n + 1))
    a = 0
    m = []
    while spisok:
        minimum = min(spisok)
        m.append(minimum)
        spisok -= set(range(minimum, n + 1, minimum))
    if n in m:
        print('True')
    else:
        print('False')