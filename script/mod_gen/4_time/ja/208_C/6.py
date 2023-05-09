def main():
    n,k = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort()
    ans = [0]*n
    for i in range(n):
        ans[i] = k//n
    k %= n
    for i in range(k):
        ans[i] += 1
    for i in range(n):
        print(ans[a[i]-1])

if __name__ == '__main__':
    main()