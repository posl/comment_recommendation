def main():
    n, k = map(int, input().split())
    p = list(map(int, input().split()))
    c = list(map(int, input().split()))
    ans = -10 ** 18
    for i in range(n):
        tmp = 0
        cnt = 0
        while cnt < k:
            tmp += c[p[i] - 1]
            i = p[i] - 1
            cnt += 1
            if i == p[i] - 1:
                break
        if tmp > 0:
            ans = max(ans, tmp * ((k - cnt) // cnt) + max(0, max(c)))
        else:
            ans = max(ans, tmp * ((k - cnt) // cnt) + max(0, max(c[:i + 1])))
    print(ans)
