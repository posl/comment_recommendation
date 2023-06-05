def main():
    n = int(input())
    v = list(map(int, input().split()))
    d = {}
    for i in range(n):
        if i % 2 == 0:
            if v[i] not in d:
                d[v[i]] = 0
            d[v[i]] += 1
        else:
            if v[i] not in d:
                d[v[i]] = 0
            d[v[i]] -= 1
    d = sorted(d.items(), key=lambda x: x[1], reverse=True)
    ans = 0
    for i in range(len(d)):
        if i == 2:
            break
        ans += d[i][1]
    print(ans)
