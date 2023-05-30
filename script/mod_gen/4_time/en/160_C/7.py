def main():
    K, N = map(int, input().split())
    A = list(map(int, input().split()))
    B = [K]
    for i in range(1, N):
        B.append(A[i] - A[i - 1])
    print(K - max(B))
main()
