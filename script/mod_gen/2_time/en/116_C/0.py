def solve():
    N = int(input())
    h = list(map(int, input().split()))
    ans = 0
    for i in range(N-1):
        if h[i] > h[i+1]:
            ans += h[i] - h[i+1]
            h[i+1] = h[i]
    return ans
print(solve())

if __name__ == '__main__':
    solve()