def main():
    N = int(input())
    A = list(map(int,input().split()))
    ans = 0
    for x in range(1,10**5+1):
        tmp = 0
        for a in A:
            if a >= x:
                tmp += x
            else:
                ans = max(ans,tmp)
                tmp = 0
        ans = max(ans,tmp)
    print(ans)

if __name__ == '__main__':
    main()