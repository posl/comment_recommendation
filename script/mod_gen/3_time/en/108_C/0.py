def main():
    n,k = map(int, input().split())
    ans = 0
    for i in range(1,n+1):
        for j in range(1,n+1):
            for l in range(1,n+1):
                if (i+j)%k == 0 and (j+l)%k == 0 and (l+i)%k == 0:
                    ans += 1
    print(ans)

if __name__ == '__main__':
    main()