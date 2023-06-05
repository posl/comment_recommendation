def RPS(i,j):
    if i == 'G':
        if j == 'G':
            return 0
        elif j == 'C':
            return 1
        elif j == 'P':
            return -1
    elif i == 'C':
        if j == 'G':
            return -1
        elif j == 'C':
            return 0
        elif j == 'P':
            return 1
    elif i == 'P':
        if j == 'G':
            return 1
        elif j == 'C':
            return -1
        elif j == 'P':
            return 0

if __name__ == '__main__':
    RPS()