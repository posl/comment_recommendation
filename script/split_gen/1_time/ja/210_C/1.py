def main():
    n, k = map(int, input().split())
    c = list(map(int, input().split()))
    count = {}
    for i in range(k):
        if c[i] in count:
            count[c[i]] += 1
        else:
            count[c[i]] = 1
    ans = len(count)
    for i in range(k, n):
        if c[i] in count:
            count[c[i]] += 1
        else:
            count[c[i]] = 1
        if count[c[i-k]] == 1:
            count.pop(c[i-k])
        else:
            count[c[i-k]] -= 1
        ans = max(ans, len(count))
    print(ans)
