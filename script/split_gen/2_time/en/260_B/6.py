def main():
    N, X, Y, Z = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    C = [(A[i] + B[i], A[i], B[i], i + 1) for i in range(N)]
    C.sort(reverse = True)
    for i in range(X + Y + Z):
        if i < X:
            print(C[i][3])
        elif i < X + Y:
            if C[i][1] < C[X - 1][1]:
                print(C[i][3])
        else:
            if C[i][1] < C[X - 1][1] and C[i][2] < C[X + Y - 1][2]:
                print(C[i][3])
