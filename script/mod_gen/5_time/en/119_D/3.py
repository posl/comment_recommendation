def main():
    A, B, Q = map(int, input().split())
    s = [0] * (A + 2)
    t = [0] * (B + 2)
    x = [0] * Q
    for i in range(A):
        s[i + 1] = int(input())
    for i in range(B):
        t[i + 1] = int(input())
    s[A + 1] = 10 ** 11
    t[B + 1] = 10 ** 11
    for i in range(Q):
        x[i] = int(input())
    for i in range(Q):
        j = 1
        k = 1
        while x[i] > s[j] and j <= A:
            j += 1
        while x[i] > t[k] and k <= B:
            k += 1
        ans = 10 ** 11
        for l in range(2):
            for m in range(2):
                d1 = abs(x[i] - s[j - 1 + l]) + abs(s[j - 1 + l] - t[k - 1 + m])
                d2 = abs(x[i] - t[k - 1 + m]) + abs(t[k - 1 + m] - s[j - 1 + l])
                ans = min(ans, d1, d2)
        print(ans)

if __name__ == '__main__':
    main()