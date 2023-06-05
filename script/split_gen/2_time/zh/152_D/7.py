def main():
    n = int(input())
    p = list(map(int, input().split()))
    ans = 0
    m = p[0]
    for i in range(n):
        if p[i] <= m:
            ans += 1
            m = p[i]
    print(ans)
