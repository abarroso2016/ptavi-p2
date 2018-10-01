#!/usr/bin/python3
# -*- coding: utf-8 -*-
import sys
import csv

from calcoohija import CalculadoraHija


calc = CalculadoraHija()
fichero = sys.argv[1]

if __name__ == "__main__":
    with open(fichero, newline='') as File:
        reader = csv.reader(File)
        for row in reader:
            word_Position = 0
            if row[0] == "suma":
                plus = 0
                for word in row:
                    if word_Position != 0:
                        plus = calc.suma(plus, int(row[word_Position]))
                    word_Position += 1
                print(plus)
            elif row[0] == "resta":
                minum = int(row[1])*2
                for word in row:
                    if word_Position != 0:
                        minum = calc.resta(minum, int(row[word_Position]))
                    word_Position += 1
                print(minum)
            elif row[0] == "multiplica":
                mult = 1
                for word in row:
                    if word_Position != 0:
                        mult = calc.multiplicar(mult, int(row[word_Position]))
                    word_Position += 1
                print(mult)
            elif row[0] == "divide":
                div = int(row[1])**2
                error = False
                for word in row:
                    if word_Position != 0:
                        try:
                            div = calc.dividir(div, int(row[word_Position]))
                        except ZeroDivisionError:
                            print("Division by zero is not allowed")
                            error = True
                    word_Position += 1
                if not error:
                    print(div)
