def main():
    # Read data
    N, T = map(int, input().split())
    ct = [list(map(int, input().split())) for _ in range(N)]
    # Solve
    ans = 1001
    for i in range(N):
        if ct[i][1] <= T:
            ans = min(ans, ct[i][0])
    if ans == 1001:
        print('TLE')
    else:
        print(ans)
