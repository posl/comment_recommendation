def main():
    h, w = map(int, input().split())
    c = [input() for _ in range(h)]
    ans = 0
    for i in range(h):
        for j in range(w):
            if c[i][j] == '.':
                ans += 1
    print(ans)
