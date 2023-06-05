def main():
    N = int(input())
    h = list(map(int, input().split()))
    ans = 0
    while sum(h) > 0:
        for i in range(N):
            if h[i] > 0:
                ans += 1
                h[i] -= 1
                while i < N and h[i] > 0:
                    h[i] -= 1
                    i += 1
                break
    print(ans)
