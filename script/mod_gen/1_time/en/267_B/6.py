def is_split(pins):
    if pins[0] == '0':
        return False
    columns = []
    for i in range(1, 11):
        if pins[i-1] == '1':
            columns.append(i)
    for i in range(len(columns)):
        for j in range(i+1, len(columns)):
            if columns[j] - columns[i] == 2:
                return True
    return False

if __name__ == '__main__':
    is_split()