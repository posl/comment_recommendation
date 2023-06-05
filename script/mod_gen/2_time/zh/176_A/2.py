def main():
    n, k = map(int, input().split())
    p = list(map(int, input().split()))
    c = list(map(int, input().split()))
    ans = -float('inf')
    for i in range(n):
        x = i
        s = 0
        t = 0
        while True:
            x = p[x] - 1
            s += c[x]
            t += 1
            if x == i:
                break
            if t == k:
                break
        if c[x] > 0:
            u = (k // t - 1) * s
        else:
            u = 0
        for j in range(k % t):
            x = p[x] - 1
            u += c[x]
            ans = max(ans, u)
    print(ans)

if __name__ == '__main__':
    main()