def main():
    h, w, a, b = map(int, input().split())
    ans = 0
    for i in range(1 << h):
        for j in range(1 << w):
            cnt = 0
            for k in range(h):
                for l in range(w):
                    if (i >> k) & 1 and (j >> l) & 1:
                        cnt += 1
            if cnt == a * b:
                ans += 1
    print(ans)

if __name__ == '__main__':
    main()