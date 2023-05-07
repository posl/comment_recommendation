def main():
    n = int(input())
    p = list(map(int, input().split()))
    ans = 0
    for i in range(n-1):
        ans = max(ans, p[i])
    print(ans)
