def solve():
    N, M = map(int, input().split())
    if M == 0:
        print("Yes")
        return
    if N == 2:
        print("No")
        return
    edges = [set() for _ in range(N)]
    for _ in range(M):
        A, B = map(int, input().split())
        edges[A - 1].add(B - 1)
        edges[B - 1].add(A - 1)
    for i in range(N):
        if len(edges[i]) == N - 1:
            print("No")
            return
    print("Yes")

if __name__ == '__main__':
    solve()