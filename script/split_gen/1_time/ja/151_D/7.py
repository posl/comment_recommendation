def solve():
    h,w = map(int,input().split())
    s = [input() for _ in range(h)]
    ans = 0
    for i in range(h):
        for j in range(w):
            if i == 0 and j == 0:
                continue
            if i == 0 and j == w-1:
                continue
            if i == h-1 and j == 0:
                continue
            if i == h-1 and j == w-1:
                continue
            if s[i][j] == '.':
                ans += 1
    print(ans*2)
