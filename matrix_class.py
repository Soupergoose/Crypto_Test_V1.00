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
        """Switches rows 1 & 2 in a matrix""" 
        
        self.matrix[row1], self.matrix[row2] = self.matrix[row2], self.matrix[row1]
        
    def row_subtract(self, row1, row2, factor):
        """Subtracts row2 multiplied by a factor from row1""" 
        
        self.matrix[row1] = [self.matrix[row1][i] - self.matrix[row2][i] * \
                    factor for i in range(self.columns)]
    
    def row_divide(self, row, factor):
        """Divides all elements in a row by a given factor"""
        print(row)
        self.matrix[row] = [self.matrix[row][i] / factor for i in range(self.columns)]
    
    def row_reduce(self):
        """Outputs row-reduced echelon form of the input matrix"""
        
        sorted_rows = 0
        #Counter for rows that have already been reduced
        
        for column in range(self.columns):
            #Loops once for each column
            
            row = sorted_rows
            hit = False
            
            while hit is False and row < (self.rows):
                """With a fixed column, loops over rows until nonzero value is 
                found or until all rows have been searched.""" 
                
                if row < self.rows and self.matrix[row][column] != 0:
                    """If the element is nonzero and x is within the domain of the 
                    rowspace, then the row is divided by the entry value to 
                    normalize the element of focus."""
                    
                    self.row_divide(row, self.matrix[row][column])
                    
                    for i in range(self.rows):
                        
                        if i != row:
                            """Row is subtracted from every row in the matrix
                            except itself"""
                            
                            self.row_subtract(i, row, self.matrix[i][column])
                            
                    self.row_swap(row, sorted_rows)
                    #The rows are then switched so that sorted rows are on top.
                    
                    sorted_rows += 1
                    hit = True
                
                else:
                    row += 1
                
        for j in range(self.rows):
            #returns and prints to screen the row reduced matrix
            
            print("\n")
            print(self.matrix[j])
        return self.matrix