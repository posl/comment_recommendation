def solve(h,w):
    print(h*w - h - w + 1)
h,w = map(int, input().split())
solve(h,w)

if __name__ == '__main__':
    solve()