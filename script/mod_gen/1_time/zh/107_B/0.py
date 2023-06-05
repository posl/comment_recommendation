def find_row_white(row):
    for i in range(len(row)):
        if row[i] == '#':
            return False
    return True

if __name__ == '__main__':
    find_row_white()