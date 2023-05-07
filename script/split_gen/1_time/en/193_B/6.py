def main():
    n = int(input())
    ans = 10**10
    for _ in range(n):
        a, p, x = map(int, input().split())
        if x - a > 0:
            ans = min(ans, p)
    if ans == 10**10:
        ans = -1
    print(ans)
