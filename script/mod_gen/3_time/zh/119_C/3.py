def main():
    N, A, B, C = map(int, input().split())
    l = [int(input()) for _ in range(N)]
    ans = float('inf')
    for i in range(4 ** N):
        a, b, c = 0, 0, 0
        mp = 0
        for j in range(N):
            if i >> 2 * j & 3 == 0:
                continue
            elif i >> 2 * j & 3 == 1:
                mp += 10
                if a != 0:
                    mp += abs(a - l[j])
                a += l[j]
            elif i >> 2 * j & 3 == 2:
                mp += 10
                if b != 0:
                    mp += abs(b - l[j])
                b += l[j]
            elif i >> 2 * j & 3 == 3:
                mp += 10
                if c != 0:
                    mp += abs(c - l[j])
                c += l[j]
        if min(a, b, c) > 0:
            mp += abs(a - A) + abs(b - B) + abs(c - C)
            ans = min(ans, mp)
    print(ans)

if __name__ == '__main__':
    main()