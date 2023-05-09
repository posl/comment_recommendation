def main():
    n, k = map(int, input().split())
    v = list(map(int, input().split()))
    ans = 0
    for i in range(min(n, k) + 1):
        for j in range(min(n, k) - i + 1):
            if i + j == 0:
                continue
            tmp = sorted(v[:i] + v[n - j:])
            for l in range(min(i + j, k - i - j)):
                if tmp[l] < 0:
                    tmp[l] = 0
            ans = max(ans, sum(tmp))
    print(ans)
