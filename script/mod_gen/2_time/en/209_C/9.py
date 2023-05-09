def main():
    #input
    N = int(input())
    Cs = list(map(int, input().split()))
    #count
    if N == 1:
        print(1)
        return
    if N == 2:
        if Cs[0] == Cs[1]:
            print(1)
        else:
            print(2)
        return
    mod = 10**9+7
    ans = 1
    for i in range(1,N):
        if Cs[i-1] != Cs[i]:
            ans *= 2
            ans %= mod
        else:
            if Cs[i-1] == 1 and Cs[i] == 1:
                print(0)
                return
            elif Cs[i-1] == 1 and Cs[i] != 1:
                ans *= 1
                ans %= mod
            elif Cs[i-1] != 1 and Cs[i] == 1:
                ans *= 1
                ans %= mod
            else:
                ans *= 1
                ans %= mod
    print(ans)

if __name__ == '__main__':
    main()