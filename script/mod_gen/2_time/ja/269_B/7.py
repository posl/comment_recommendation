def solve():
    S = [input() for _ in range(10)]
    A = B = C = D = 0
    for i in range(10):
        if S[i].count("#") > 0:
            if A == 0:
                A = i + 1
            B = i + 1
            for j in range(10):
                if S[i][j] == "#":
                    if C == 0:
                        C = j + 1
                    D = j + 1
    print(A, B)
    print(C, D)

if __name__ == '__main__':
    solve()