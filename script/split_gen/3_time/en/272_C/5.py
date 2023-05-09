def main():
    N = int(input())
    A = list(map(int, input().split()))
    A.sort(reverse=True)
    for i in range(0, N):
        for j in range(i + 1, N):
            if A[i] % 2 == 0:
                if A[i] == A[j] * 2:
                    print(A[i])
                    return
            else:
                if A[i] == A[j] * 2 + 1:
                    print(A[i])
                    return
    print(-1)
