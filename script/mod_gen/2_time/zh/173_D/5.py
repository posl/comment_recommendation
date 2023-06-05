def main():
    h, w, k = map(int, input().split())
    c = [list(input()) for _ in range(h)]
    ans = 0
    for i in range(2 ** h):
        for j in range(2 ** w):
            black = 0
            for k in range(h):
                for l in range(w):
                    if i >> k & 1 and j >> l & 1 and c[k][l] == '#':
                        black += 1
            if black == k:
                ans += 1
    print(ans)

if __name__ == '__main__':
    main()