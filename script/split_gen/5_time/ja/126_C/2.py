def main():
    n, k = map(int, input().split())
    ans = 0
    for i in range(1, n+1):
        score = i
        p = 1 / n
        while score < k:
            score *= 2
            p /= 2
        ans += p
    print(ans)
