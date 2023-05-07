def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort()
    A.append(N + 1)
    if M == 0:
        print(1)
        return
    if M == N:
        print(0)
        return
    dist = []
    for i in range(M):
        if A[i] + 1 < A[i + 1]:
            dist.append(A[i + 1] - A[i] - 1)
    dist.sort(reverse=True)
    ans = dist[0] + 1
    for i in range(1, M):
        ans = max(ans, (dist[i] - 1) // i + 1)
    print(ans)

if __name__ == '__main__':
    main()