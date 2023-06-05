def find_row_white(row):
    for i in range(len(row)):
        if row[i] == '#':
            return False
    return True
