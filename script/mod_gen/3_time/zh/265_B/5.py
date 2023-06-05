def solve():
    N, M, T = map(int, input().split())
    A = list(map(int, input().split()))
    XY = [list(map(int, input().split())) for _ in range(M)]
    for i in range(N-1):
        A[i] = [A[i], i+1]
    A.sort(reverse=True)
    A.append([0, N])
    now = 1
    time = T
    for a, b in A:
        time -= now - b
        if time <= 0:
            print('No')
            exit(0)
        time += a
        now = b
    print('Yes')

if __name__ == '__main__':
    solve()