
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
