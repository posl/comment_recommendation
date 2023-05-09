def main():
    n = int(input())
    p = list(map(int, input().split()))
    ans = 0
    for i in range(1, n):
        ans = max(ans, f(i, p))
    print(ans)
