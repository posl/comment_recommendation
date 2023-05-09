def main():
    n, t = map(int, input().split())
    ans = 1000
    for i in range(n):
        c, ti = map(int, input().split())
        if ti <= t:
            ans = min(ans, c)
    if ans == 1000:
        print("TLE")
    else:
        print(ans)
