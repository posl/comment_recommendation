def main():
    S = []
    for _ in range(10):
        S.append(input())
    A = 1
    B = 10
    C = 1
    D = 10
    for i in range(10):
        if S[i].count('#') == 0:
            A += 1
        else:
            break
    for i in range(10):
        if S[9-i].count('#') == 0:
            B -= 1
        else:
            break
    for i in range(10):
        if S[0][i] == '#':
            C += 1
        else:
            break
    for i in range(10):
        if S[0][9-i] == '#':
            D -= 1
        else:
            break
    print(A, B)
    print(C, D)
