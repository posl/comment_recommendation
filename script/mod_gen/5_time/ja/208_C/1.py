def main():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    ans = [0] * n
    for i in range(n):
        ans[i] = k // n
    k %= n
    b = sorted(a)
    for i in range(k):
        ans[b[i]-1] += 1
    for i in range(n):
        print(ans[i])

if __name__ == '__main__':
    main()