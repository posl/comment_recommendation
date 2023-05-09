def main():
    N = int(input())
    X, Y = map(int, input().split())
    A = []
    B = []
    for i in range(N):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)
    #print(N, X, Y)
    #print(A)
    #print(B)
    ans = -1
    for i in range(N):
        for j in range(N):
            if A[i] + B[j] >= X and A[i] + B[j] >= Y:
                if ans == -1:
                    ans = A[i] + B[j]
                else:
                    ans = min(ans, A[i] + B[j])
    print(ans)
