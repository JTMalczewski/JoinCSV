from package import *
import sys
import numpy as np



argument = read.imput(sys.argv)
data_source_one = argument[1]
data_source_two = argument[2]
collumn_name = argument[3]
join_type = argument[4]

rows_one = np.array(read.openFile(data_source_one))  #exports data from CSV files to numpy 2D array
matrix_one = np.array(read.splitRow(rows_one))
rows_two = np.array(read.openFile(data_source_two))
matrix_two = np.array(read.splitRow(rows_two))

maching_indexes = read.findMatchingRows(matrix_one,matrix_two,collumn_name)

if join_type == 'left':
    matrix_new = join_fun.joinLeft(matrix_one, matrix_two, collumn_name, maching_indexes)
elif join_type == 'right':
    matrix_new = join_fun.joinRight(matrix_one, matrix_two, collumn_name, maching_indexes)
elif join_type == 'inner':
    matrix_new = join_fun.joinInner(matrix_one, matrix_two, collumn_name, maching_indexes)

draw.printCSV(matrix_new)

