def main():
    N = int(input())
    C = list(map(int, input().split()))
    C.sort()
    ans = 1
    for i in range(N):
        ans *= (C[i]-i) % (10**9+7)
        ans %= (10**9+7)
    print(ans)

if __name__ == '__main__':
    main()