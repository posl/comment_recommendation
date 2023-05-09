def main():
    N = int(input())
    ans = 0
    ans += pow(10, N, 10**9+7)
    ans -= 2*pow(9, N, 10**9+7)
    ans += pow(8, N, 10**9+7)
    print(ans % (10**9+7))

if __name__ == '__main__':
    main()