def main():
    a, b, q = map(int, input().split())
    s = [int(input()) for _ in range(a)]
    t = [int(input()) for _ in range(b)]
    x = [int(input()) for _ in range(q)]
    for i in range(q):
        ans = 10**18
        for j in range(a):
            for k in range(b):
                ans = min(ans, abs(s[j] - x[i]) + abs(t[k] - s[j]))
                ans = min(ans, abs(t[k] - x[i]) + abs(s[j] - t[k]))
        print(ans)

if __name__ == '__main__':
    main()