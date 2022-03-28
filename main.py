from click import argument
from package import *
import sys
import numpy as np

from package.read import *



argument = read.imput(sys.argv)
data_source_one = argument[1]
data_source_two = argument[2]
join_by_collumn_name = argument[3]
join_type = argument[4]

rows_one = np.array(read.openFile(data_source_one))  #exports data from CSV files to numpy 2D array
matrix_one = np.array(read.splitRow(rows_one))
rows_two = np.array(read.openFile(data_source_two))
matrix_two = np.array(read.splitRow(rows_two))

header_one = matrix_one[0]
header_two = matrix_one[0]

print(read.find_matching_rows(matrix_one,matrix_two,join_by_collumn_name))

