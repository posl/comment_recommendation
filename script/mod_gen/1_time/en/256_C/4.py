def solve():
    h = list(map(int, input().split()))
    w = list(map(int, input().split()))
    ans = 0
    for i in range(1, 30):
        for j in range(1, 30):
            for k in range(1, 30):
                if h[0] == i + j + k and h[1] == i + 2 * j + 3 * k and h[2] == i + 3 * j + 6 * k and w[0] == i + 2 * i + 3 * i and w[1] == j + 2 * j + 3 * j and w[2] == k + 2 * k + 3 * k:
                    ans += 1
    print(ans)

if __name__ == '__main__':
    solve()