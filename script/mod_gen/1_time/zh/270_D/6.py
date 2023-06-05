def main():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    a.append(n)
    ans = 0
    cur = 0
    for i in range(k+1):
        ans += (a[i]-cur+1)//2
        cur = a[i]
    print(ans)

if __name__ == '__main__':
    main()