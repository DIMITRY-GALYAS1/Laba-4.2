#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Поле first — дробное число; поле second — дробное число,
показатель степени. Реализовать метод power() — возведение числа
first в c тепень second. Метод должен правильно работать при любых
допустимых значениях first и second.
"""


class Myclass:

    def __init__(self, first, second):
        self.first = float(first)
        self.second = float(second)
        if self.first == 0:
            raise ValueError()

    def __pow__(self, other):
        z = self.first + self.second
        x = other.first + other.second
        k = z ** x
        return k


if __name__ == '__main__':
    t1 = Myclass(2.2, 0)
    t2 = Myclass(2, 0)
    print(t1 ** t2)
