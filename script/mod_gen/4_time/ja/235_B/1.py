def main():
    n = int(input())
    h = list(map(int,input().split()))
    ans = h[0]
    for i in range(1,n):
        if ans <= h[i]:
            ans = h[i]
    print(ans)

if __name__ == '__main__':
    main()