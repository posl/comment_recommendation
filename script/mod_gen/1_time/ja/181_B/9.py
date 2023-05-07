def main():
    N = int(input())
    ans = 0
    for i in range(N):
        a, b = map(int, input().split())
        ans += (b-a+1)*(a+b)/2
    print(int(ans%1000000007))

if __name__ == '__main__':
    main()