def main():
    N, A, B, C = map(int, input().split())
    l = [int(input()) for _ in range(N)]
    ans = 10 ** 9
    for i in range(4 ** N):
        a, b, c = 0, 0, 0
        mp = 0
        for j in range(N):
            if (i >> (2 * j)) % 4 == 1:
                if a != 0:
                    mp += 10
                a += l[j]
            elif (i >> (2 * j)) % 4 == 2:
                if b != 0:
                    mp += 10
                b += l[j]
            elif (i >> (2 * j)) % 4 == 3:
                if c != 0:
                    mp += 10
                c += l[j]
        if a == 0 or b == 0 or c == 0:
            continue
        mp += abs(a - A) + abs(b - B) + abs(c - C)
        ans = min(ans, mp)
    print(ans)

if __name__ == '__main__':
    main()