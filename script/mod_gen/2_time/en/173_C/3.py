def main():
    h, w, k = map(int, input().split())
    c = [list(input()) for _ in range(h)]
    ans = 0
    for i in range(2 ** h):
        for j in range(2 ** w):
            cnt = 0
            for a in range(h):
                for b in range(w):
                    if c[a][b] == '#' and i >> a & 1 == 0 and j >> b & 1 == 0:
                        cnt += 1
            if cnt == k:
                ans += 1
    print(ans)

if __name__ == '__main__':
    main()