#!/usr/bin/python3
# -*- coding: utf-8 -*-
import sys
import csv

from calcoohija import CalculadoraHija


calc = CalculadoraHija()

if __name__ == "__main__":
    with open('fichero.csv', newline='') as File:
        reader = csv.reader(File)
        for row in reader:
            if row[0] == "suma":
                plus = 0
                word_Position = 0
                for word in row:
                    if word_Position != 0:
                        plus = calc.suma(plus, int(row[word_Position]))
                    word_Position = word_Position+1
            elif row[0] == "resta":
                minum = 0
                word_Position = 0
                for word in row:
                    if word_Position != 0 and word_Position != 1:
                        minum = calc.resta(minum, int(row[word_Position]))
                    elif word_Position == 1:
                        minum = calc.suma(minum, int(row[1]))
                    word_Position = word_Position+1
            elif row[0] == "multiplica":
                mult = 1
                word_Position = 0
                for word in row:
                    if word_Position != 0:
                        mult = calc.multiplicar(mult, int(row[word_Position]))
                    word_Position = word_Position+1
            elif row[0] == "divide":
                div = 0
                word_Position = 0
                for word in row:
                    if word_Position != 0 and word_Position != 1:
                        try:
                            div = calc.dividir(div, int(row[word_Position]))
                        except ZeroDivisionError:
                            sys.exit("Division by zero is not allowed")
                    elif word_Position == 1:
                        div = calc.suma(div, int(row[1]))
                    word_Position = word_Position+1
print(plus)
print(minum)
print(mult)
print(div)
