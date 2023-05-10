def main():
    K, N = map(int, input().split())
    A = list(map(int, input().split()))
    B = []
    for i in range(N):
        if i == 0:
            B.append(K - A[i] + A[i + 1])
        elif i == N - 1:
            B.append(K - A[i] + A[0])
        else:
            B.append(A[i + 1] - A[i])
    print(K - max(B))
main()
