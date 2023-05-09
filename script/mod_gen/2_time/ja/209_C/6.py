def main():
    N = int(input())
    C = list(map(int, input().split()))
    C.sort()
    if C[0] == C[-1]:
        print(0)
        return
    ans = 1
    for i in range(N):
        ans *= C[i] - i
        ans %= 10**9 + 7
    print(ans)
main()

if __name__ == '__main__':
    main()