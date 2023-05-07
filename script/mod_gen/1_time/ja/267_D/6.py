def main():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    ans = 0
    for i in range(n):
        b = a[i:i+m]
        if len(b) == m:
            ans = max(ans, sum([j * b[j-1] for j in range(1, m+1)]))
    print(ans)

if __name__ == '__main__':
    main()