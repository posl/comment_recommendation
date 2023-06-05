def main():
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    c = list(map(lambda x: int(x)-1, input().split()))
    d = {}
    for i in range(n):
        if b[c[i]] in d:
            d[b[c[i]]] += 1
        else:
            d[b[c[i]]] = 1
    ans = 0
    for i in range(n):
        if a[i] in d:
            ans += d[a[i]]
    print(ans)

if __name__ == '__main__':
    main()