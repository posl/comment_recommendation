def main():
    #input
    s = []
    for i in range(10):
        s.append(input())
    #compute
    a = 0
    b = 0
    c = 0
    d = 0
    for i in range(10):
        if s[i].find('#') == -1:
            continue
        else:
            a = i + 1
            break
    for i in range(9, -1, -1):
        if s[i].find('#') == -1:
            continue
        else:
            b = i + 1
            break
    for i in range(10):
        if s[i].find('#') == -1:
            continue
        else:
            for j in range(10):
                if s[i][j] == '#':
                    c = j + 1
                    break
            break
    for i in range(10):
        if s[i].find('#') == -1:
            continue
        else:
            for j in range(9, -1, -1):
                if s[i][j] == '#':
                    d = j + 1
                    break
            break
    #output
    print(a, b)
    print(c, d)
