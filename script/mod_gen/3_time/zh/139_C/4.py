def main():
    n = int(input())
    h = list(map(int,input().split()))
    ans = 0
    cnt = 0
    for i in range(1,n):
        if h[i-1] >= h[i]:
            cnt += 1
        else:
            ans = max(ans,cnt)
            cnt = 0
    ans = max(ans,cnt)
    print(ans)

if __name__ == '__main__':
    main()