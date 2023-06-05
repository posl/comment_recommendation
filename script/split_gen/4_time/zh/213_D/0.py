def main():
    N = int(input())
    A = []
    B = []
    for i in range(N - 1):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)
    for i in range(N):
        if i == 0:
            print(1, end=' ')
        else:
            if A[i - 1] == 1:
                print(B[i - 1], end=' ')
            else:
                print(A[i - 1], end=' ')
        if i == N - 1:
            print(1, end=' ')
    print()
