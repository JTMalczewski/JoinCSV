
from numpy import NaN
import numpy as np


def joinLeft(matrix_one: list, matrix_two: list, join_by: str, index: list) -> list:
    '''
    Left join two list
    '''

    key_index_two = np.where(matrix_two[0] == join_by)
    matrix_two_less = np.delete(matrix_two.T,key_index_two[0][0],0)
    merged_matrix = []

    for i in range(len(matrix_one)):

        if index[i][1] == '':
            merged_matrix.append(
               np.append(matrix_one[index[i][0]],
               len(matrix_two_less.T[0])*[[NaN]])
               )
        else: 
            merged_matrix.append(
                np.append(matrix_one[index[i][0]],
                matrix_two_less.T[index[i][1]])
          )

    return merged_matrix

def joinRight(matrix_one: list, matrix_two: list, index: list) -> list:

    return [1,2]


def joinInner(matrix_one: list, matrix_two: list, index: list) -> list:

    return [1,2]