def main():
    n = int(input())
    cs = list(map(int, input().split()))
    cs.sort()
    ans = 1
    for i in range(n):
        ans *= (cs[i] - i)
        ans %= 1000000007
    print(ans)

if __name__ == '__main__':
    main()