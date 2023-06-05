def main():
    h, w, k = map(int, input().split())
    c = []
    for _ in range(h):
        c.append(list(input()))
    ans = 0
    for i in range(2 ** h):
        for j in range(2 ** w):
            cnt = 0
            for l in range(h):
                for m in range(w):
                    if (i >> l) & 1 == 0 and (j >> m) & 1 == 0 and c[l][m] == '#':
                        cnt += 1
            if cnt == k:
                ans += 1
    print(ans)
