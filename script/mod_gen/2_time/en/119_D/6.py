def main():
    A, B, Q = map(int, input().split())
    s = [-10**15] + [int(input()) for i in range(A)] + [10**15]
    t = [-10**15] + [int(input()) for i in range(B)] + [10**15]
    x = [int(input()) for i in range(Q)]
    for i in x:
        ans = 10**15
        for j in s:
            if i <= j:
                ans = min(ans, j - i + min(abs(j - k) for k in t))
            else:
                ans = min(ans, i - j + min(abs(j - k) for k in t))
        print(ans)
main()

if __name__ == '__main__':
    main()