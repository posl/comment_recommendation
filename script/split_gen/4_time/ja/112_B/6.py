def main():
    n, t = map(int, input().split())
    ans = 1000
    for _ in range(n):
        c, ti = map(int, input().split())
        if ti <= t and ans > c:
            ans = c
    if ans == 1000:
        print("TLE")
    else:
        print(ans)
