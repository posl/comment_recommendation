def main():
    N = int(input())
    h = list(map(int, input().split()))
    ans = 0
    for i in range(max(h)):
        for j in range(N):
            if h[j] > 0:
                l = j
                break
        for j in range(N-1, -1, -1):
            if h[j] > 0:
                r = j
                break
        ans += 1
        for j in range(l, r+1):
            h[j] -= 1
    print(ans)
