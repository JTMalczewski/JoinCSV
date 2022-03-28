
from numpy import NaN
import numpy as np


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
        arguments.append("inner")
        print("unspeciffy join type, process with type \"inner\"")
    elif len(arguments) != 5:
        print("wrong number of arguments")

    return arguments


def findMatchingRows(matrix_one: list, matrix_two: list, join_by: str) -> list:
    '''
    find row indexes with matching records between two columns with the same name in two databases
    '''

    key_index_one = np.where(matrix_one[0] == join_by)
    key_index_two = np.where(matrix_two[0] == join_by)

    matching_index_one = []
    matching_index_two = [] 
    matching_index = []

    for record_one in range(len(matrix_one.T[key_index_one][0])):
        record_two = np.where(matrix_two.T[key_index_two][0] == matrix_one.T[key_index_one][0][record_one])

        if record_two[0].size != 0:
            matching_index_one = record_one 
            matching_index_two = record_two[0][0]
        elif record_two[0].size == 0:
            matching_index_one = record_one
            matching_index_two = ''
        matching_index.append([matching_index_one,matching_index_two])
    return matching_index

