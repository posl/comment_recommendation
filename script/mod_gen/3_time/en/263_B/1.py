def main():
    n = int(input())
    p = list(map(int, input().split()))
    ans = 0
    for i in range(n-1,0,-1):
        ans = max(ans, p[i-1])
    print(ans)

if __name__ == '__main__':
    main()