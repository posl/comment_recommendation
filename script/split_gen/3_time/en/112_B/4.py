def main():
    N, T = map(int, input().split())
    ans = 1000
    for _ in range(N):
        c, t = map(int, input().split())
        if t <= T:
            ans = min(ans, c)
    if ans == 1000:
        print("TLE")
    else:
        print(ans)
