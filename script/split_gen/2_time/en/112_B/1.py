def main():
    N, T = map(int, input().split())
    c = [0] * N
    t = [0] * N
    for i in range(N):
        c[i], t[i] = map(int, input().split())
    ans = 1001
    for i in range(N):
        if t[i] <= T:
            ans = min(ans, c[i])
    if ans == 1001:
        print("TLE")
    else:
        print(ans)
