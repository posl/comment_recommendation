def main():
    N, A, B, C = map(int, input().split())
    l = [int(input()) for _ in range(N)]
    ans = 10**9
    for i in range(4**N):
        tmp = i
        mp = 0
        a = A
        b = B
        c = C
        for j in range(N):
            if tmp % 4 == 1:
                mp += 10
                a -= l[j]
            elif tmp % 4 == 2:
                mp += 10
                b -= l[j]
            elif tmp % 4 == 3:
                mp += 10
                c -= l[j]
            tmp //= 4
        if a <= 0 and b <= 0 and c <= 0:
            ans = min(ans, mp)
    print(ans)

if __name__ == '__main__':
    main()