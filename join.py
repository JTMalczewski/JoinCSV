from tools import *
import sys
import numpy as np



arguments = read.input(sys.argv)                                             #naming arguments from command window
data_source_one = arguments[1]
data_source_two = arguments[2]
collumn_name = arguments[3]
join_type = arguments[4]

rows_one = np.array(read.openFile(data_source_one))                         #exports data from CSV files to numpy 2D array
matrix_one = np.array(read.splitRow(rows_one))
rows_two = np.array(read.openFile(data_source_two))
matrix_two = np.array(read.splitRow(rows_two))

if join_type == 'left':                                                     #decides on joining type
    matrix_new = join_fun.joinLeft(matrix_one, matrix_two, collumn_name)
elif join_type == 'right':
    matrix_new = join_fun.joinRight(matrix_one, matrix_two, collumn_name)
elif join_type == 'inner':
    matrix_new = join_fun.joinInner(matrix_one, matrix_two, collumn_name)

draw.printCSV(matrix_new)

