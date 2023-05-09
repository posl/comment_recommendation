def main():
    h, w, k = map(int, input().split())
    c = [input() for _ in range(h)]
    ans = 0
    for i in range(2 ** h):
        for j in range(2 ** w):
            cnt = 0
            for y in range(h):
                for x in range(w):
                    if not i >> y & 1 and not j >> x & 1 and c[y][x] == "#":
                        cnt += 1
            if cnt == k:
                ans += 1
    print(ans)
