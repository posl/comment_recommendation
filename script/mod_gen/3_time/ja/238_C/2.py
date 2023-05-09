def main():
    N = int(input())
    ans = 0
    for i in range(1, N+1):
        if len(str(i)) == len(str(N)):
            ans += 1
    print(ans % 998244353)
main()

if __name__ == '__main__':
    main()