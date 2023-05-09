def main():
    # input
    S = [input() for _ in range(10)]
    # compute
    A = B = C = D = 0
    for i in range(10):
        if '#' in S[i]:
            if A == 0:
                A = i+1
            else:
                B = i+1
                break
    for j in range(10):
        if '#' in [S[i][j] for i in range(10)]:
            if C == 0:
                C = j+1
            else:
                D = j+1
                break
    # output
    print(A, B)
    print(C, D)
