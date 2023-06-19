def main():
    n,k = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort()
    ans = 0
    for i in range(n-k+1):
        if (a[i+k-1] - a[i]) < ans or ans == 0:
            ans = a[i+k-1] - a[i]
    print(ans)

if __name__ == '__main__':
    main()