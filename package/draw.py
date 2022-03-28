def printCSV(matrix: list) -> None:
    '''
    write input matrix to the standard output
    '''
    rows = []
    for row in matrix:
        line = ''
        for word in row:
            line += word
            line += ','
        line = line[:-1]
        line += '\n'
        rows.append(line)
    print(''.join(rows))
    return None