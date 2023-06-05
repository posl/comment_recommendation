def main():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort()
    ans = [k // n] * n
    k %= n
    for i in range(k):
        ans[a[i] - 1] += 1
    for i in range(n):
        print(ans[i])

if __name__ == '__main__':
    main()