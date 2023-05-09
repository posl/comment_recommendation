def main():
    h, w = map(int, input().split())
    s = [list(input()) for _ in range(h)]
    ans = 0
    for i in range(h):
        for j in range(w):
            if s[i][j] == '#':
                if i == 0 or i == h-1 or j == 0 or j == w-1:
                    ans = 2
                else:
                    ans = 4
    print(ans)
