def main():
    n, x = map(int, input().split())
    a = []
    b = []
    for _ in range(n):
        ai, bi = map(int, input().split())
        a.append(ai)
        b.append(bi)
    ans = float('inf')
    for i in range(n):
        ans = min(ans, x*i + b[i]*(n-i) + max(0, a[i]-b[i])*i)
    print(ans)

if __name__ == '__main__':
    main()