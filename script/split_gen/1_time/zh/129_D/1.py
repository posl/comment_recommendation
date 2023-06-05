def main():
    h, w = map(int, input().split())
    s = [input() for _ in range(h)]
    ans = 0
    for i in range(h):
        for j in range(w):
            if s[i][j] == '#':
                continue
            t = 0
            k = i
            while k >= 0 and s[k][j] == '.':
                t += 1
                k -= 1
            k = i
            while k < h and s[k][j] == '.':
                t += 1
                k += 1
            k = j
            while k >= 0 and s[i][k] == '.':
                t += 1
                k -= 1
            k = j
            while k < w and s[i][k] == '.':
                t += 1
                k += 1
            t -= 3
            ans = max(ans, t)
    print(ans)
