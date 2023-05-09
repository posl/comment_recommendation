def main():
    h, w, k = map(int, input().split())
    c = [input() for i in range(h)]
    ans = 0
    for i in range(2**h):
        for j in range(2**w):
            cnt = 0
            for k in range(h):
                for l in range(w):
                    if (i >> k) & 1:
                        continue
                    if (j >> l) & 1:
                        continue
                    if c[k][l] == '#':
                        cnt += 1
            if cnt == k:
                ans += 1
    print(ans)

if __name__ == '__main__':
    main()