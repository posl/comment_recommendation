def main():
    h, w = map(int, input().split())
    s = [input() for _ in range(h)]
    ans = 0
    for i in range(h):
        for j in range(w):
            if s[i][j] == "#":
                continue
            cnt = 0
            for x in range(i, h):
                if s[x][j] == "#":
                    break
                cnt += 1
            for x in range(i, -1, -1):
                if s[x][j] == "#":
                    break
                cnt += 1
            for y in range(j, w):
                if s[i][y] == "#":
                    break
                cnt += 1
            for y in range(j, -1, -1):
                if s[i][y] == "#":
                    break
                cnt += 1
            ans = max(ans, cnt - 3)
    print(ans)
