# ！/usr/bin/env python3
# -*- coding: utf-8 -*-


file = open(r'Data/result/datagrand-char-300d.txt')

print(type(file))

print(len(file.readline(1)))
list1 = file.readlines()

print(type(list1))

print(len(list1))
file.close()
