def solve():
    N = int(input())
    h = list(map(int, input().split()))
    ans = 0
    for i in range(N-1):
        if h[i] < h[i+1]:
            ans += h[i+1] - h[i]
    print(ans)

if __name__ == '__main__':
    solve()