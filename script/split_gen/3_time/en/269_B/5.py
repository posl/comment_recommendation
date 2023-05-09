def main():
    S = []
    for i in range(10):
        S.append(input())
    for i in range(10):
        S[i] = list(S[i])
    #print(S)
    for i in range(10):
        for j in range(10):
            if S[i][j] == "#":
                S[i][j] = "O"
    #print(S)
    A = 0
    B = 0
    C = 0
    D = 0
    for i in range(10):
        for j in range(10):
            if S[i][j] == "O":
                A = i+1
                break
        if A != 0:
            break
    for i in range(9, -1, -1):
        for j in range(9, -1, -1):
            if S[i][j] == "O":
                B = i+1
                break
        if B != 0:
            break
    for j in range(10):
        for i in range(10):
            if S[i][j] == "O":
                C = j+1
                break
        if C != 0:
            break
    for j in range(9, -1, -1):
        for i in range(9, -1, -1):
            if S[i][j] == "O":
                D = j+1
                break
        if D != 0:
            break
    print(A, B)
    print(C, D)
