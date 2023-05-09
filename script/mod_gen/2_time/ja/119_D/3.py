def main():
    a,b,q = map(int, input().split())
    s = [int(input()) for _ in range(a)]
    t = [int(input()) for _ in range(b)]
    x = [int(input()) for _ in range(q)]
    for i in range(q):
        ans = 10**18
        for j in range(a):
            for k in range(b):
                d = abs(x[i] - s[j])
                d += abs(s[j] - t[k])
                if d < ans:
                    ans = d
                d = abs(x[i] - t[k])
                d += abs(t[k] - s[j])
                if d < ans:
                    ans = d
        print(ans)

if __name__ == '__main__':
    main()