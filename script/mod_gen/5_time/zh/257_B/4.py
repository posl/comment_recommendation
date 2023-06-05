def main():
    n, k, q = map(int, input().split())
    a = list(map(int, input().split()))
    l = list(map(int, input().split()))
    ans = [0] * n
    for i in range(k):
        ans[a[i] - 1] += 1
    for i in range(n - 1):
        ans[i + 1] += ans[i]
    for i in range(q):
        print(ans[l[i] - 1])

if __name__ == '__main__':
    main()