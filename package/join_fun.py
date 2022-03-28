
from numpy import NaN
import numpy as np
from package import read


def joinLeft(matrix_one: list, matrix_two: list, join_by: str) -> list:
    '''
    Left join two list
    '''
    index = read.findMatchingRows(matrix_one,matrix_two,join_by)
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



def joinRight(matrix_one: list, matrix_two: list, join_by: str) -> list:
    '''
    Right join two list
    '''
    index = read.findMatchingRows(matrix_two,matrix_one,join_by)

    key_index_one = np.where(matrix_one[0] == join_by)
    matrix_one_less = np.delete(matrix_one.T,key_index_one[0][0],0)
    merged_matrix = []
    len_one = len(matrix_one_less.T[0])

    for i in range(len(matrix_two)):

        if index[i][1] == '':
            merged_matrix.append(
               np.append(len_one*[[NaN]],
               matrix_two[index[i][0]],)
               )
        else: 
            merged_matrix.append(
                np.append(matrix_two[index[i][0]],
                matrix_one_less.T[index[i][1]])
          )

    return merged_matrix



def joinInner(matrix_one: list, matrix_two: list, join_by: str, index: list) -> list:

    return [1,2]