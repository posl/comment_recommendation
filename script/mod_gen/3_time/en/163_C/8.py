def main():
    n = int(input())
    a = [0] + list(map(int, input().split()))
    ans = [0 for _ in range(n+1)]
    for i in range(2, n+1):
        ans[a[i]] += 1
    for i in range(1, n+1):
        print(ans[i])

if __name__ == '__main__':
    main()