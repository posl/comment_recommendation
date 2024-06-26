def main():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    ans = 0
    for i in range(n - m + 1):
        ans = max(ans, sum([j * a[i + j] for j in range(m)]))
    print(ans)

if __name__ == '__main__':
    main()