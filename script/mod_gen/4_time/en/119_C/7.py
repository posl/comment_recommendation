def main():
    N, A, B, C = map(int, input().split())
    L = [int(input()) for _ in range(N)]
    ans = 10 ** 9
    for i in range(4 ** N):
        a, b, c = 0, 0, 0
        cost = 0
        for j in range(N):
            if (i >> (2 * j)) & 3 == 1:
                if a == 0:
                    a = L[j]
                else:
                    a += L[j]
                cost += 10
            elif (i >> (2 * j)) & 3 == 2:
                if b == 0:
                    b = L[j]
                else:
                    b += L[j]
                cost += 10
            elif (i >> (2 * j)) & 3 == 3:
                if c == 0:
                    c = L[j]
                else:
                    c += L[j]
                cost += 10
        if a == 0 or b == 0 or c == 0:
            continue
        cost += abs(A - a) + abs(B - b) + abs(C - c) - 30
        ans = min(ans, cost)
    print(ans)

if __name__ == '__main__':
    main()