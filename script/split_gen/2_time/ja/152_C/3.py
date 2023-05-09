def main():
    n = int(input())
    p = list(map(int, input().split()))
    ans = 0
    min_p = 10**6
    for i in range(n):
        if p[i] <= min_p:
            ans += 1
            min_p = p[i]
    print(ans)
