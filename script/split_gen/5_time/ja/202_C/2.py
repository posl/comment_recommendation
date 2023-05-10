def main():
    n = int(input())
    a = [int(x) for x in input().split()]
    b = [int(x) for x in input().split()]
    c = [int(x) for x in input().split()]
    d = {}
    for i in range(n):
        if b[c[i]-1] in d:
            d[b[c[i]-1]] += 1
        else:
            d[b[c[i]-1]] = 1
    ans = 0
    for i in range(n):
        if a[i] in d:
            ans += d[a[i]]
    print(ans)
main()
