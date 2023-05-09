def solve():
    S = []
    for _ in range(10):
        S.append(input())
    for i in range(10):
        if '#' in S[i]:
            break
    A = i + 1
    for i in range(10):
        if '#' in S[9-i]:
            break
    B = 10 - i
    for i in range(10):
        if '#' in [S[j][i] for j in range(10)]:
            break
    C = i + 1
    for i in range(10):
        if '#' in [S[j][9-i] for j in range(10)]:
            break
    D = 10 - i
    print(A, B)
    print(C, D)

if __name__ == '__main__':
    solve()