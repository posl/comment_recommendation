def main():
    n = int(input())
    a = list(map(int, input().split()))
    a.insert(0, 0)
    b = [0 for i in range(200001)]
    c = [0 for i in range(200001)]
    for i in range(1, n+1):
        b[a[i]] += 1
    for i in range(1, 200001):
        if b[i] > 0:
            for j in range(i, 200001, i):
                c[j] += b[i]
            if b[i] > 1:
                c[i] -= b[i]
    ans = 0
    for i in range(1, n+1):
        ans += c[a[i]]
    print(ans)
