def main():
    N = int(input())
    C = list(map(int, input().split()))
    C.sort()
    mod = 10**9 + 7
    ans = 1
    for i in range(N):
        ans = (ans * max(0, C[i]-i)) % mod
    print(ans)

if __name__ == '__main__':
    main()