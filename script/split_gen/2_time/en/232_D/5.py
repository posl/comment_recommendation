def main():
    h, w = map(int, input().split())
    c = [input() for i in range(h)]
    print(c)
    ans = 0
    for i in range(h):
        for j in range(w):
            if c[i][j] == '.':
                ans += 1
    print(ans)
