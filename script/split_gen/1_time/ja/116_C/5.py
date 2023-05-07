def main():
    N = int(input())
    h = list(map(int, input().split()))
    ans = 0
    while max(h) > 0:
        l = 0
        r = 0
        for i in range(N):
            if h[i] > 0:
                l = i
                break
        for i in range(N - 1, -1, -1):
            if h[i] > 0:
                r = i
                break
        for i in range(l, r + 1):
            h[i] -= 1
        ans += 1
    print(ans)
