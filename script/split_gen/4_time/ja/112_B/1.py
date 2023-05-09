def main():
    N, T = map(int, input().split())
    C = []
    T = []
    for i in range(N):
        c, t = map(int, input().split())
        C.append(c)
        T.append(t)
    ans = 1000
    for i in range(N):
        if T[i] <= T:
            ans = min(ans, C[i])
    if ans == 1000:
        print("TLE")
    else:
        print(ans)
