def printCSV(matrix: list) -> None:
    '''
    write input matrix to the standard output
    '''
    rows = []
    for row in matrix:
        line = ",".join(row)
        line += '\n'
        rows.append(line)
    print(''.join(rows))
    
    return