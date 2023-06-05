def main():
    n,k = map(int,input().split())
    a = []
    for i in range(n):
        a.append(list(map(int,input().split())))
    ans = 10**9
    for i in range(n-k+1):
        for j in range(n-k+1):
            b = []
            for p in range(k):
                for q in range(k):
                    b.append(a[i+p][j+q])
            b.sort()
            ans = min(ans,b[k*k//2])
    print(ans)

if __name__ == '__main__':
    main()