#!bin/bash/python3
# -*- coding: utf-8 -*-

""" Experimentation with Classes and their attributes """

class Example:
    """An example class"""
    def __init__(self, kind, color, weight):
        self.kind = kind
        self.color = color
        self.weight = weight
        
    pi = 3.14159
    
    

class Matrix:
    """ Class for rudimentary matrix functions including transposition, 
    row reduced echelon form, determinates, etc."""
    
    def __init__(self, matrix):
        self.matrix = matrix
        self.columns = len(matrix[0])
        self.rows = len(matrix)
        for i in range(self.rows):
            print(self.matrix[i])
            print('\n')
        #check to see if input is indeed a matrix
        
    def row_swap(self, row1, row2):
        " switches rows 1 & 2 in a matrix "
        
        self.matrix[row1], self.matrix[row2] = self.matrix[row2], self.matrix[row1]
        
    def row_subtract(self, row1, row2, factor):
        "subtracts row2 multiplied by a factor from row1" 
        
        self.matrix[row1] = [self.matrix[row1][i] - self.matrix[row2][i] * factor for i in range(self.columns)]
    
    def row_divide(self, row, factor):
        "divides all elements in a row by a given factor"
        self.matrix[row] = [self.matrix[row][i] / factor for i in range(self.rows)]
    
    def row_reduce(self):
        """Row reduces input matrix"""
        
        sorted_rows = 0
        #counter for rows that have already been reduced
        
        for y in range(self.columns):
            
            x = sorted_rows
            hit = False
            
            while hit is False and x < (self.rows): 
                
                if x < self.rows and self.matrix[x][y] != 0:
                
                    self.row_divide(x, self.matrix[x][y])
                    
                    for i in range(self.rows):
                        
                        if i != x:
                            
                            self.row_subtract(i, x, self.matrix[i][y])
                            
                    
                    self.row_swap(x, sorted_rows)
                    sorted_rows += 1
                    hit = True
                
                else:
                    x += 1
                
        for j in range(self.rows):
            print("\n")
            print(self.matrix[j])
            