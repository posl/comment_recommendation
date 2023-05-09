def main():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort()
    a.append(0)
    ans = [0] * n
    for i in range(n):
        ans[a[i] - 1] += k // n
    for i in range(n):
        ans[i] -= k // n
    k %= n
    for i in range(k):
        ans[a[i] - 1] += 1
    for i in range(n):
        print(ans[i])

if __name__ == '__main__':
    main()