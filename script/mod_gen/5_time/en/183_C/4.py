def solve():
    N, K = map(int, input().split())
    T = [list(map(int, input().split())) for _ in range(N)]
    count = 0
    for perm in itertools.permutations(range(1, N)):
        time = 0
        now = 0
        for next in perm:
            time += T[now][next]
            now = next
        time += T[now][0]
        if time == K:
            count += 1
    print(count)

if __name__ == '__main__':
    solve()