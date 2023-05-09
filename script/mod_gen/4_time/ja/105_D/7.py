def main():
    n,m = map(int,input().split())
    a = list(map(int,input().split()))
    a = [i%m for i in a]
    b = [0]
    for i in range(n):
        b.append((b[-1]+a[i])%m)
    from collections import Counter
    c = Counter(b)
    ans = 0
    for i in c:
        ans += c[i]*(c[i]-1)//2
    print(ans)

if __name__ == '__main__':
    main()