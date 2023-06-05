def main():
    n, k = map(int, input().split())
    c = list(map(int, input().split()))
    # print(n, k, c)
    # n, k = 7, 3
    # c = [1, 2, 1, 2, 3, 3, 1]
    # n, k = 5, 5
    # c = [4, 4, 4, 4, 4]
    # n, k = 10, 6
    # c = [304621362, 506696497, 304621362, 506696497, 834022578, 304621362, 414720753, 304621362, 304621362, 414720753]
    # print(n, k, c)
    # print(max([len(set(c[i:i+k])) for i in range(n-k+1)]))
    d = {}
    for i in range(k):
        d[c[i]] = d.get(c[i], 0) + 1
    # print(d)
    ans = len(d)
    for i in range(n-k):
        d[c[i]] -= 1
        if d[c[i]] == 0:
            del d[c[i]]
        d[c[i+k]] = d.get(c[i+k], 0) + 1
        # print(d)
        ans = max(ans, len(d))
    print(ans)
