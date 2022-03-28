
import imp
from matplotlib.pyplot import margins
from numpy import append


def openFile(filename: str) -> list:
    '''
    open text file and retun as list with header first
    '''
    rows = []
    with open(filename, 'r') as csvfile:
        for x in csvfile:
            rows.append(x)
    return rows


def splitRow(rows: str) -> list:
    '''
    split string list by commas and convert to 2D string matrix
    '''
    data_matrix = []
    for i in range(len(rows)):
        separated  = rows[i].split(',')
        separated[-1] = separated[-1][0:-1]
        data_matrix.append(separated)
    return data_matrix


def imput(arguments: list) -> list:
    '''
    set default join type and inform about incomplete information
    '''
    if len(arguments) == 4:
        arguments.append("right")
        print("unspeciffy join type, process with type \"right\"")
    elif len(arguments) != 5:
        print("wrong number of arguments")

    return arguments


def find_matching_rows(matrix_one: list, matrix_two: list, join_by: str) -> list:
    '''
    find row indexes with matching records between two columns with the same name in two databases
    '''
    import numpy as np

    kay_index_one = np.where(matrix_one[0] == join_by)
    kay_index_two = np.where(matrix_two[0] == join_by)

    matching_index_one = []
    matching_index_two = [] 
    
    for record_one in range(len(matrix_one.T[kay_index_one][0])):
        record_two = np.where(matrix_two.T[kay_index_two][0] == matrix_one.T[kay_index_one][0][record_one])

        if record_two[0].size != 0:
            matching_index_one.append(record_one)
            matching_index_two.append(record_two[0][0])

    return [matching_index_one, matching_index_two]

