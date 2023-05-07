def main():
    n, k = map(int, input().split())
    p = list(map(int, input().split()))
    c = list(map(int, input().split()))
    ans = -10**18
    for i in range(n):
        now = i
        tmp = []
        while True:
            now = p[now] - 1
            tmp.append(c[now])
            if now == i:
                break
        if len(tmp) < k:
            m = max(tmp)
            if m <= 0:
                continue
            tmp = tmp * (k // len(tmp))
            tmp += tmp[:k % len(tmp)]
        else:
            tmp = tmp[:k]
        s = sum(tmp)
        if s <= 0:
            ans = max(ans, max(tmp))
        else:
            ans = max(ans, s + (k // len(tmp) - 1) * max(0, max(tmp)))
    print(ans)

if __name__ == '__main__':
    main()