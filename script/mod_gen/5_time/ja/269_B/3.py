def main():
    S = []
    for i in range(10):
        S.append(input())
    A = 0
    B = 0
    C = 0
    D = 0
    for i in range(10):
        for j in range(10):
            if S[i][j] == '#':
                A = i
                break
        if A != 0:
            break
    for i in range(9,-1,-1):
        for j in range(9,-1,-1):
            if S[i][j] == '#':
                B = i
                break
        if B != 0:
            break
    for i in range(10):
        for j in range(10):
            if S[j][i] == '#':
                C = i
                break
        if C != 0:
            break
    for i in range(9,-1,-1):
        for j in range(9,-1,-1):
            if S[j][i] == '#':
                D = i
                break
        if D != 0:
            break
    print(A+1,B+1)
    print(C+1,D+1)

if __name__ == '__main__':
    main()