def main():
    n = int(input())
    a = []
    b = []
    for i in range(n):
        ai, bi = map(int, input().split())
        a.append(ai)
        b.append(bi)
    #print(a)
    #print(b)
    d = [0] * (10 ** 9 + 2)
    for i in range(n):
        d[a[i]] += 1
        d[a[i] + b[i]] -= 1
    #print(d)
    for i in range(1, 10 ** 9 + 2):
        d[i] += d[i - 1]
    #print(d)
    ans = [0] * (n + 1)
    for i in range(10 ** 9 + 2):
        ans[d[i]] += 1
    #print(ans)
    for i in range(1, n + 1):
        print(ans[i], end = " ")
    print()
