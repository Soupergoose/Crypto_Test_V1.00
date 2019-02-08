#!bin/bash/python3
# -*- coding: utf-8 -*-

""" Experimentation with Classes and their attributes """

class example:
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
        #check to see if input is indeed a matrix
        
    def row_swap(self, row1, row2):
        self.matrix[row1], self.matrix[row2] = self.matrix[row2], self.matrix[row1]
        
    def row_subtract(self, row1, row2, factor):
        self.matrix[row1] = [self.matrix[row1][i] - self.matrix[row2][i] * factor for i in range(self.columns)]
    
    def row_divide(self, row1, factor):
        self.matrix[row1] = [self.matrix[row1][i] / factor for i in range(self.rows)]
    
    def row_reduce(self):
        """Row reduces input matrix"""
        # sorted counter
        
        sorted_rows = 0
        
        for y in range(self.columns):
            
            for x in range(self.rows):
 
                if self.matrix[x][y] != 0:
                    self.row_divide(x, self.matrix[x,y])
                    
                    for i in range(self.rows):
                        
                        if i != x:
                            
                            self.row_subtract(i, x, self.matrix[i][y])
                            
                    
                    self.row_swap(x, sorted_rows)
                    sorted_rows += 1
                
       