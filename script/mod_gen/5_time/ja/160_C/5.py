def solve():
    K, N = map(int, input().split())
    A = list(map(int, input().split()))
    A.append(A[0] + K)
    print(K - max(A[i + 1] - A[i] for i in range(N)))

if __name__ == '__main__':
    solve()