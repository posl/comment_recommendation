def find_min_max(string):
    a = 0
    b = 0
    c = 0
    d = 0
    for i in range(10):
        if '#' in string[i]:
            a = i+1
            break
    for i in range(9,-1,-1):
        if '#' in string[i]:
            b = i+1
            break
    for i in range(10):
        if '#' in string[i]:
            for j in range(10):
                if string[i][j] == '#':
                    c = j+1
                    break
            break
    for i in range(9,-1,-1):
        if '#' in string[i]:
            for j in range(9,-1,-1):
                if string[i][j] == '#':
                    d = j+1
                    break
            break
    return a, b, c, d
