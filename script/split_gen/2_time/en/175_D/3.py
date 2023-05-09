def main():
    n, k = map(int, input().split())
    p = list(map(int, input().split()))
    c = list(map(int, input().split()))
    ans = -10**18
    for i in range(n):
        tmp = 0
        cnt = 0
        j = i
        while cnt < k:
            j = p[j] - 1
            tmp += c[j]
            cnt += 1
            if j == i:
                break
        if tmp <= 0:
            continue
        if cnt == k:
            ans = max(ans, tmp)
        else:
            ans = max(ans, tmp * ((k - cnt) // cnt) + max(0, max(c[j + 1:] + c[:j + 1])))
    print(ans)
