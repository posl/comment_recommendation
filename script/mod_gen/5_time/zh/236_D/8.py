def main():
    n = int(input())
    a = [[0 for i in range(n)] for j in range(n)]
    for i in range(n):
        a[i] = list(map(int,input().split()))
    ans = -float('inf')
    for i in range(2**n):
        b = [0 for j in range(n)]
        for j in range(n):
            if (i >> j) & 1:
                b[j] = 1
        cnt = 0
        for j in range(n):
            for k in range(j+1,n):
                if b[j] == b[k] == 1:
                    cnt += a[j][k]
        ans = max(ans,cnt)
    print(ans)

if __name__ == '__main__':
    main()