from numpy import NaN
import numpy as np
import sys


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
        separated[-1] = separated[-1][0:-1]             #deletes the line break symbol
        data_matrix.append(separated)
    return data_matrix


def imput(arguments: list) -> list:
    '''
    set default join type and inform about incomplete information
    '''
    if len(arguments) == 4:
        arguments.append("inner")
        print("Wrong number of arguments.\nPossible unspecified join type, process with type \"inner\".\nmake sure to check executed command.\n")
    elif len(arguments) != 5:
        sys.exit("Wrong number of arguments\nScript terminated")

    return arguments


def findMatchingRows(matrix_one: list, matrix_two: list, join_by: str) -> list:
    '''
    find row indexes with matching records between two columns with the same name in two databases
    '''
    key_index_one = np.where(matrix_one[0] == join_by)  #searches for the index of the common column in both data files 
    key_index_two = np.where(matrix_two[0] == join_by)

    if len(key_index_two[0]) == 0 or len(key_index_one[0]) == 0:
        sys.exit("Script terminated. No matching column names, please make sure to check executed command.")

    matching_index_one = []
    matching_index_two = [] 
    matching_index = []
    matrix_lenght = len(matrix_one.T[key_index_one][0])

    #iterates by every line in a common column in the first data file and searches for the same values in the second data file 
    for record_one in range(matrix_lenght):
        record_two = np.where(matrix_two.T[key_index_two][0] == matrix_one.T[key_index_one][0][record_one])

        if record_two[0].size != 0:                     #saves the index of common value for both data files
            matching_index_one = record_one 
            matching_index_two = record_two[0][0]
        elif record_two[0].size == 0:                   #saves the index of not common values, an empty string is used as a mark
            matching_index_one = record_one
            matching_index_two = ''

        matching_index.append([matching_index_one,matching_index_two])

    return matching_index

