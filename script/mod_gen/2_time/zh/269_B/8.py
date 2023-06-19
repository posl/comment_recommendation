def main():
    strs = []
    for i in range(10):
        strs.append(input())
    for i in range(10):
        if strs[i].count('.') == 10:
            strs.pop(i)
            break
    for i in range(len(strs)):
        strs[i] = strs[i].replace('.', ' ')
    for i in range(len(strs)):
        strs[i] = list(strs[i])
    A = 0
    B = 0
    C = 0
    D = 0
    for i in range(10):
        if '#' in strs[i]:
            A = i + 1
            break
    for i in range(9, -1, -1):
        if '#' in strs[i]:
            B = i + 1
            break
    for i in range(10):
        for j in range(10):
            if strs[i][j] == '#':
                C = j + 1
                break
        if C != 0:
            break
    for i in range(9, -1, -1):
        for j in range(10):
            if strs[i][j] == '#':
                D = j + 1
                break
        if D != 0:
            break
    print(str(A) + ' ' + str(B))
    print(str(C) + ' ' + str(D))

if __name__ == '__main__':
    main()