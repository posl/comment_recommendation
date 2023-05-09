def main():
    #input
    N = int(input())
    A = list(map(int, input().split()))
    #compute
    ans = 0
    for x in range(1, 10**5+1):
        l = 0
        r = 0
        for i in range(N):
            if A[i] >= x:
                r = i
                if l == 0:
                    l = i
                ans = max(ans, (r-l+1)*x)
    #output
    print(ans)

if __name__ == '__main__':
    main()