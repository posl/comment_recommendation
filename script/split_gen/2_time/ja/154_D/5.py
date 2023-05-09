def main():
    n, k = map(int, input().split())
    p = list(map(int, input().split()))
    p = [i+1 for i in p]
    p = [i/2 for i in p]
    ans = sum(p[:k])
    tmp = ans
    for i in range(k, n):
        tmp += p[i] - p[i-k]
        ans = max(ans, tmp)
    print(ans)
