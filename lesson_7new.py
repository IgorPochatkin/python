# -*- coding: utf-8 -*-
"""
Created on Sat Sep 19 15:37:29 2020

@author: Spiderman
"""
# exercise 1. Вывод матриц и сложение 
 
class Matrix: 
     
    def __init__(self, first): 
        self.second = '\n'.join(['\t'.join([str(el) for el in i]) for i in first]) 
        self.first = [[el for el in i] for i in first] 
         
    def __str__(self): 
        self.a = str(self.second) 
        return self.second 
  
 
    def __add__(self, new): 
        for el in range(len(self.first)): 
            for i in range(len(new.first[0])): 
                self.first[el][i] = self.first[el][i] + new.first[el][i] 
            self.result = self.first 
        return Matrix(self.result) 
            
mat1 = Matrix([[1, 2, 3, 4, 5], [1, 2, 3, 4, 5], [1, 2, 3, 4, 5], [1, 2, 3, 4, 5]]) 
mat2 = Matrix([[5, 4, 3, 2, 1], [5, 4, 3, 2, 1], [5, 4, 3, 2, 1], [5, 4, 3, 2, 1]]) 
print(f"Первая матрица:\n{mat1}") 
print() 
print(f"Вторая матрица:\n{mat2}") 
print() 
print(f"Сумма матриц:\n{mat1+mat2}") 
 
 
 
# exercise 2. Расход ткани на одежду 
 
class Clothes: 
    def __init__(self, v, h): 
        self.v = v 
        self.h = h 
     
    @property 
    def calc(self): 
        print(f'Всего необходимо {round(self.v/6.5 + 0.5,2)} метров ткани')      
 
class Coat(Clothes): 
    def __init__(self, ctype, v, h): 
        super().__init__(v, h) 
        self.ctype = ctype 
         
    @property     
    def calc(self): 
        return print(self.v/6.5 + 0.5) 
 
class Suit(Clothes):  
    def __init__(self, ctype, v, h): 
        super().__init__(v, h) 
        self.ctype = ctype 
     
    @property     
    def calc(self): 
        return self.h*2 + 0.3     
total = Clothes(2,3) 
total.calc 
 
 
     
 
# exercise 3. Операции с клетками 
 
class Cell: 
 
    def __init__(self, quantity): 
        self.quantity = quantity 
 
    def __str__(self): 
        return f'Итог операции {self.quantity * "*"}' 
 
    def __add__(self, other): 
        return Cell(self.quantity + other.quantity) 
 
    def __sub__(self, other): 
 
        return f'Итог операции {self.quantity - other.quantity}' if (self.quantity - other.quantity) > 0 else print('Разность количества клаток отрицательна') 
 
 
    def __mul__(self, other): 
         
        return Cell(int(self.quantity * other.quantity)) 
 
    def __truediv__(self, other): 
        return Cell(round(self.quantity // other.quantity)) 
 
 
    def make_order(self, cells_in_row): 
        row = '' 
        for i in range(int(self.quantity / cells_in_row)): 
            row += f'{"*" * cells_in_row} \\n' 
        row += f'{"*" * (self.quantity % cells_in_row)}' 
        return row 
 
cells1 = Cell(2) 
cells2 = Cell(10) 
print(cells1) 
print(cells1 + cells2) 
print(cells2 - cells1) 
print(cells1 - cells2) 
print(cells1 * cells2) 
print(cells1 / cells2) 
print(cells2.make_order(5)) 
print(cells1.make_order(10)) 
print(cells1 / cells2)    
