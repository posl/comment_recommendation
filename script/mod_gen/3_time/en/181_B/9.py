def main():
    N = int(input())
    AB = [list(map(int, input().split())) for _ in range(N)]
    AB.sort()
    ans = 0
    for a, b in AB:
        ans += (b-a+1)*(a+b)//2
    print(ans%998244353)

if __name__ == '__main__':
    main()