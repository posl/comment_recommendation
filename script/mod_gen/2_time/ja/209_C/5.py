def main():
    N = int(input())
    C = [int(x) for x in input().split()]
    mod = 10 ** 9 + 7
    ans = 1
    for i in range(N):
        if i == 0:
            ans *= C[i]
            continue
        if C[i] < C[i-1]:
            print(0)
            return
        elif C[i] == C[i-1]:
            ans *= C[i] - 1
        else:
            ans *= C[i] - i
        ans %= mod
    print(ans)

if __name__ == '__main__':
    main()