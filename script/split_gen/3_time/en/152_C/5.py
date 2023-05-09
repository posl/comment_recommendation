def main():
    n = int(input())
    p = list(map(int, input().split()))
    ans = 0
    min = n + 1
    for i in range(n):
        if min > p[i]:
            ans += 1
            min = p[i]
    print(ans)
