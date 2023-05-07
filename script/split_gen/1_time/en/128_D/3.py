def main():
    n, k = map(int, input().split())
    v = list(map(int, input().split()))
    ans = 0
    for a in range(min(n, k) + 1):
        for b in range(min(n, k) - a + 1):
            now = v[:a] + v[n - b:]
            now.sort()
            for i in range(k - a - b):
                if i == len(now) or now[i] > 0:
                    break
                now[i] = 0
            ans = max(ans, sum(now))
    print(ans)
