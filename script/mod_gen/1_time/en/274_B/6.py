def solve():
    h, w = map(int, input().split())
    c = [list(input()) for _ in range(h)]
    ans = [0] * w
    for i in range(w):
        for j in range(h):
            if c[j][i] == '#':
                ans[i] += 1
    print(' '.join(map(str, ans)))

if __name__ == '__main__':
    solve()