def main():
    n = int(input())
    a = list(map(int,input().split()))
    b = [0]*(2*n+1)
    for i in range(n):
        b[a[i]] = i+1
    ans = [0]*(2*n+1)
    for i in range(1,2*n+1):
        j = i
        cnt = 0
        while j > 0:
            cnt += 1
            j //= 2
        ans[i] = cnt-1
    for i in range(1,2*n+1):
        j = i
        cnt = 0
        while j > 0:
            cnt += 1
            j //= 2
        ans[i] = cnt-1
    for i in range(2,2*n+1):
        if ans[i] == 1:
            ans[i] = ans[b[i]]+1
    for i in range(1,2*n+1):
        print(ans[i])

if __name__ == '__main__':
    main()