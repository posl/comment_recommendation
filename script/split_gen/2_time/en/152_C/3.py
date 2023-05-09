def main():
    N = int(input())
    p = list(map(int, input().split()))
    ans = 0
    min_p = N + 1
    for i in range(N):
        if p[i] <= min_p:
            ans += 1
            min_p = p[i]
    print(ans)
