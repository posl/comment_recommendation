def main():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort()
    a = [0] + a
    d = [0] * n
    for i in range(n):
        d[i] = (a[i+1] - a[i]) % m
    d.sort()
    ans = sum(d[:-1])
    print(ans)
main()

if __name__ == '__main__':
    main()