def solve():
    K, N = map(int, input().split())
    A = list(map(int, input().split()))
    A.append(K+A[0])
    maxDistance = 0
    for i in range(N):
        maxDistance = max(maxDistance, A[i+1]-A[i])
    print(K-maxDistance)

if __name__ == '__main__':
    solve()