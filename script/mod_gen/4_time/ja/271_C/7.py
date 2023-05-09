def main():
    N = int(input())
    a = list(map(int,input().split()))
    a.sort()
    ans = 0
    for i in range(N):
        ans += a[i]
        if ans < a[i+1]:
            break
    print(ans)

if __name__ == '__main__':
    main()