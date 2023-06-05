def main():
    A, B, Q = map(int, input().split())
    s = [int(input()) for _ in range(A)]
    t = [int(input()) for _ in range(B)]
    x = [int(input()) for _ in range(Q)]
    s.append(2 * 10 ** 10)
    t.append(2 * 10 ** 10)
    s = [-2 * 10 ** 10] + s
    t = [-2 * 10 ** 10] + t
    for i in range(Q):
        ans = 10 ** 20
        for j in range(A + 1):
            for k in range(B + 1):
                d = min(abs(x[i] - s[j]), abs(x[i] - t[k]))
                d += abs(s[j] - t[k])
                ans = min(ans, d)
        print(ans)

if __name__ == '__main__':
    main()