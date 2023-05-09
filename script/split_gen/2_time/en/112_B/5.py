def main():
    N, T = map(int, input().split())
    ans = 10**9+1
    for _ in range(N):
        c, t = map(int, input().split())
        if t <= T:
            ans = min(ans, c)
    if ans == 10**9+1:
        print("TLE")
    else:
        print(ans)
