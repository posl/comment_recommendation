def main():
    H, W, A, B = map(int, input().split())
    ans = 0
    for i in range(2**H):
        for j in range(2**W):
            cnt = 0
            for k in range(H):
                if (i >> k) & 1 == 1:
                    continue
                for l in range(W):
                    if (j >> l) & 1 == 1:
                        continue
                    cnt += 1
            if cnt == A:
                ans += 1
    print(ans)

if __name__ == '__main__':
    main()