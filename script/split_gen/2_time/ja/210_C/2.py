def main():
    from collections import Counter
    n, k = map(int, input().split())
    c = list(map(int, input().split()))
    count = Counter(c[:k])
    ans = len(count)
    for i in range(n-k):
        count[c[i]] -= 1
        if count[c[i]] == 0:
            del count[c[i]]
        count[c[i+k]] += 1
        ans = max(ans, len(count))
    print(ans)
