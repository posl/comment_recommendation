def main():
    N, X = map(int, input().split())
    A = []
    B = []
    for _ in range(N):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)
    for i in range(N):
        for j in range(B[i] + 1):
            if A[i] * j == X:
                print('Yes')
                return
            elif A[i] * j > X:
                break
            else:
                X -= A[i]
    print('No')
