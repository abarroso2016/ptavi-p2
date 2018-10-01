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
               plus=0
               j=0
               for i in row:
                   if j != 0:
                       plus=calc.suma(plus,int(row[j]))
                   j=j+1
           elif row[0] == "resta":
               minum=0
               j=0
               for i in row:
                   if j != 0 and j != 1:
                       minum=calc.resta(minum,int(row[j]))
                   elif j == 1:
                       minum=calc.suma(minum,int(row[1]))
                   j=j+1
           elif row[0] == "multiplica":
               multiply=1
               j=0
               for i in row:
                   if j != 0:
                       multiply=calc.multiplicar(multiply,int(row[j]))
                   j=j+1
           elif row[0] == "divide":
               div=0
               j=0
               for i in row:
                   if j != 0 and j != 1:
                       try:
                           div=calc.dividir(div,int(row[j]))
                       except ZeroDivisionError:
                           sys.exit("Division by zero is not allowed")
                   elif j == 1:
                       div=calc.suma(div,int(row[1]))
                   j=j+1
    File.close()
print(plus)
print(minum)
print(multiply)
print(div)
